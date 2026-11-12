#!/usr/bin/env python3
"""Rebuild assets/stats.svg from live GitHub data plus a small static config.

Live (GitHub search API): merged PRs in other people's repos, how many of them
are in the Layer5 / CNCF ecosystem, and how many repos they span.
Static (.github/stats-static.json): GSSoC rank and problem-solving numbers,
which GitHub cannot tell us.

Set MOCK=/path/to/list.json (a JSON list of "owner/repo" strings, one per
merged PR) to run without network access.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import Counter
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG = os.path.join(ROOT, ".github", "stats-static.json")
OUT = os.path.join(ROOT, "assets", "stats.svg")


def merged_repos(user, token):
    """One 'owner/repo' entry per merged PR the user authored outside their own repos."""
    if os.environ.get("MOCK"):
        with open(os.environ["MOCK"], encoding="utf-8") as f:
            return json.load(f)
    query = f"author:{user} type:pr is:merged -user:{user}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    repos, page = [], 1
    while page <= 10:
        params = urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        req = urllib.request.Request(f"https://api.github.com/search/issues?{params}", headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        for item in data["items"]:
            repos.append(item["repository_url"].split("/repos/", 1)[1])
        if len(data["items"]) < 100:
            break
        page += 1
    return repos


def short_name(repo):
    _, name = repo.split("/", 1)
    if repo.lower() == "meshery/meshery":
        return "Meshery"
    if name.lower() in ("tells", "blowhorn-tells"):
        return "tells"
    return name


def build_cards(cfg, repos):
    counts = Counter(repos)
    for extra in cfg.get("manual_extra_merged", []):
        if extra["repo"] not in counts:
            counts[extra["repo"]] += extra["count"]
            print(f"note: added manual extra for {extra['repo']}", file=sys.stderr)

    owners = {o.lower() for o in cfg["ecosystem_owners"]}
    eco = {r: n for r, n in counts.items() if r.split("/")[0].lower() in owners}
    top = sorted(eco.items(), key=lambda kv: (-kv[1], short_name(kv[0]).lower()))
    sub = " · ".join(f"{short_name(r)} ×{n}" for r, n in top[:3])
    if len(top) > 3:
        sub += f" · +{len(top) - 3}"

    return [
        (str(sum(counts.values())), "Merged PRs", f"across {len(counts)} repos"),
        (str(sum(eco.values())), "Layer5 / CNCF", sub),
        (cfg["gssoc"]["value"], "GSSoC '26", cfg["gssoc"]["sub"]),
        (cfg["problems"]["value"], "Problems solved", cfg["problems"]["sub"]),
    ]


def render(cards):
    aria = "Key numbers: " + ", ".join(f"{n} {l.lower()}" for n, l, _ in cards)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="140" viewBox="0 0 1000 140" role="img" aria-label="{escape(aria)}">',
        '<defs><linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00D4FF"/><stop offset="1" stop-color="#00B39F"/></linearGradient></defs>',
        "<style>.sans{font-family:'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif}</style>",
    ]
    for i, (num, label, sub) in enumerate(cards):
        x = i * 254
        cx = x + 119
        parts += [
            f'<rect x="{x + 0.5}" y="8.5" width="238" height="123" rx="11" fill="#0d1117" stroke="#30363d"/>',
            f'<rect x="{cx - 18}" y="24" width="32" height="3" rx="1.5" fill="url(#accent)"/>',
            f'<text class="sans" x="{cx}" y="66" text-anchor="middle" fill="#ffffff" font-size="36" font-weight="700">{escape(num)}</text>',
            f'<text class="sans" x="{cx}" y="91" text-anchor="middle" fill="#e6edf3" font-size="13.5" font-weight="600">{escape(label)}</text>',
            f'<text class="sans" x="{cx}" y="111" text-anchor="middle" fill="#8b949e" font-size="10">{escape(sub)}</text>',
        ]
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    with open(CONFIG, encoding="utf-8") as f:
        cfg = json.load(f)
    repos = merged_repos(cfg["user"], os.environ.get("GITHUB_TOKEN"))
    cards = build_cards(cfg, repos)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(cards) + "\n")
    print("wrote", OUT, [c[0] for c in cards])


if __name__ == "__main__":
    main()
