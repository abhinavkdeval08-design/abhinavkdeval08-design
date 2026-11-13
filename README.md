<div align="center">

<img src="assets/header.svg?v=4" alt="Abhinav Deval, backend and real-time systems" width="100%"/>

<br/><br/>

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abhinavkdeval08@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhinavdeval/)
[![Portfolio](https://img.shields.io/badge/Portfolio-1f2937?style=for-the-badge&logo=googlechrome&logoColor=00D4FF)](https://abhinavkdeval.vercel.app)
[![Meshery](https://img.shields.io/badge/Meshery-v1.0.77-00B39F?style=for-the-badge)](https://github.com/meshery/meshery/releases/tag/v1.0.77)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/abhinav_deval07/)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/abhinavkdeval29)
[![Codolio](https://img.shields.io/badge/Codolio-00D4FF?style=for-the-badge&logo=codeforces&logoColor=0a0f1e)](https://codolio.com/profile/Abhinavdeval07)

<br/>

<sub><b>CONTRIBUTING TO</b></sub>

<br/><br/>

<a href="https://github.com/layer5io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/layer5io/layer5/master/.github/assets/images/layer5/layer5-light-no-trim.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/layer5io/layer5/master/.github/assets/images/layer5/layer5-no-trim.svg">
    <img src="https://raw.githubusercontent.com/layer5io/layer5/master/.github/assets/images/layer5/layer5-no-trim.svg" alt="Layer5" height="40">
  </picture>
</a>
&nbsp;&nbsp;&nbsp;
<a href="https://github.com/meshery"><img src="https://github.com/meshery.png?size=80" height="40" alt="Meshery" /></a>
&nbsp;&nbsp;
<a href="https://github.com/blowhorn-ai"><img src="https://github.com/blowhorn-ai.png?size=80" height="40" alt="Blowhorn" /></a>
&nbsp;&nbsp;
<a href="https://www.cncf.io/"><img src="https://github.com/cncf.png?size=80" height="40" alt="CNCF" /></a>
&nbsp;&nbsp;
<a href="https://github.com/asyncapi"><img src="https://github.com/asyncapi.png?size=80" height="40" alt="AsyncAPI" /></a>

</div>

<br/>

---

## 👋 About

Second-year B.Tech ECE student at **IIIT Kalyani** (Class of 2029). I build **backend services, real-time systems, and browser-side processing**, and contribute to **Meshery (CNCF)**, **Layer5 / Blowhorn**, and **AsyncAPI**, fixing security, reliability, and CI bugs with tests.

- 🚢 Two fixes shipped in **[Meshery v1.0.77](https://github.com/meshery/meshery/releases/tag/v1.0.77)** release notes: one in Go (`mesheryctl`) and one in the UI.
- 🧩 Merged a provider-resolution fix in Meshery's `mesheryctl-axi` extension ([#86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86)), closing a user-reported bug.
- 🔐 Fixed a CSV formula-injection vulnerability and a Cloudflare Access key-rotation bug (valid tokens returning 403) in a production worker.
- 🏆 Ranked **#137 of 47,924** in GSSoC '26 (top 0.3%).

> **🎯 Looking for:** Backend or real-time systems internships, and a GSoC 2027 slot with Layer5/Meshery or AsyncAPI.  
> **🕒 Availability:** IST (UTC+5:30) · online evenings and weekends · async-friendly

<br/>

<div align="center">

<img src="assets/stats.svg?v=3" alt="Key numbers: merged PRs, Layer5 and CNCF contributions, GSSoC rank and problems solved" width="100%"/>

</div>

<br/>

---

## 💼 Open-source experience

<table>
<tr>
<td width="80" align="center" valign="top">
  <a href="https://github.com/meshery"><img src="https://github.com/meshery.png?size=112" width="56" alt="Meshery" /></a>
</td>
<td valign="top">

**Open-Source Contributor · Meshery (CNCF / Layer5)** &nbsp;·&nbsp; *2026*<br/>
<sub>mesheryctl · Meshery UI · mesheryctl-axi · Sistent</sub>

- Two fixes in the official **v1.0.77** release: three `mesheryctl environment view` panics (Go, [#23365](https://github.com/meshery/meshery/pull/23365)) and an endless UI spinner on empty component schemas ([#23357](https://github.com/meshery/meshery/pull/23357))
- Merged the `system status` `provider: null` fix in `mesheryctl-axi` ([#86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86)): config, then token file, then server probe with a 3s timeout, then `Unknown`, covered by tests
- In review: schema hardening follow-up ([#23363](https://github.com/meshery/meshery/pull/23363)) and two Sistent components ([#1659](https://github.com/layer5io/sistent/pull/1659), [#1660](https://github.com/layer5io/sistent/pull/1660))

</td>
</tr>
<tr>
<td width="80" align="center" valign="top">
  <a href="https://github.com/blowhorn-ai"><img src="https://github.com/blowhorn-ai.png?size=112" width="56" alt="Blowhorn" /></a>
</td>
<td valign="top">

**Open-Source Contributor · Blowhorn** &nbsp;·&nbsp; *2026*<br/>
<sub>#4 human contributor · 28 commits · 14 PRs merged · Cloudflare Worker security and CI</sub>

- Closed a CSV formula-injection hole in the signups export ([#496](https://github.com/blowhorn-ai/blowhorn-site/pull/496)) and made unsubscribe links safe from mail scanners ([#447](https://github.com/blowhorn-ai/blowhorn-site/pull/447))
- Fixed Cloudflare Access key rotation rejecting valid tokens with 403 ([#513](https://github.com/blowhorn-ai/blowhorn-site/pull/513))
- Cleaned up CI, labeler, templates and legacy references across `blowhorn-site` and `tells`

</td>
</tr>
<tr>
<td width="80" align="center" valign="top">
  <a href="https://github.com/asyncapi"><img src="https://github.com/asyncapi.png?size=112" width="56" alt="AsyncAPI" /></a>
</td>
<td valign="top">

**Open-Source Contributor · AsyncAPI** &nbsp;·&nbsp; *2026*<br/>
<sub>AsyncAPI CLI</sub>

- `asyncapi diff` printed an empty `ValidationError` on unparsable files; fix is in review ([#2313](https://github.com/asyncapi/cli/pull/2313))

</td>
</tr>
</table>

<br/>

---

## ⭐ Selected work

| Focus | Engineering Impact & Proof |
| :--- | :--- |
| **CSV Formula Injection** | Neutralized `=`, `+`, `-`, `@`, tab, and CR triggers (including after leading whitespace) and quoted bare CRs to prevent row splitting per OWASP CWE-1236. Merged with tests in [blowhorn-site #496](https://github.com/blowhorn-ai/blowhorn-site/pull/496). |
| **Access Key-Rotation Bug** | Refetched Cloudflare signing certs once on an unknown `kid` instead of failing valid tokens with 403 until the 10-minute cache expired, while still failing closed on invalid keys. Merged in [blowhorn-site #513](https://github.com/blowhorn-ai/blowhorn-site/pull/513). |
| **`mesheryctl` Runtime Panics** | Fixed three panics in `environment view` (nil API response, empty slice, `TotalCount` mismatch) with table-driven Go unit tests. Shipped in **Meshery v1.0.77** via [meshery #23365](https://github.com/meshery/meshery/pull/23365). |
| **Provider Resolution** | `system status` printed `provider: null` for Local-provider logins. Added a fail-soft chain (config, token file, `/api/provider` probe with a 3s timeout, `Unknown`) that forwards the auth cookie and is covered by token-file, fallback and timeout tests. Merged in [mesheryctl-axi #86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86). |
| **Mail-Scanner Unsubscribes** | Split unsubscribe links so `GET` renders a confirmation page and only `POST` mutates state, preventing email security scanners from unsubscribing users. Merged in [blowhorn-site #447](https://github.com/blowhorn-ai/blowhorn-site/pull/447). |

<br/>

**What maintainers said**
> *"Nice, targeted fix for the key-rotation 403s."* — maintainer review on [blowhorn-site #513](https://github.com/blowhorn-ai/blowhorn-site/pull/513)  
> *"Nice fix — the fallback hierarchy in resolveProvider is easy to follow, failing soft at each step instead of leaking a raw null into status output…"* — maintainer review on [mesheryctl-axi #86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86)  
> *"Nice cleanup — this does exactly what it says."* — maintainer review on [tells #28](https://github.com/blowhorn-ai/tells/pull/28)

<br/>

---

## 🚀 Featured projects

<table>
<tr>
<td width="50%" valign="top">

### [🔒 EnclavePDF](https://github.com/abhinavkdeval08-design/EnclavePDF)
Zero-egress in-browser PDF compression. No backend, no account, no analytics: turn off Wi-Fi and it still compresses.

- Web Worker pipeline: `pdf.js` → `OffscreenCanvas` → JPEG → `pdf-lib`, with a lossless fallback and the original file returned if nothing shrinks
- **52% smaller** on a 37-page sample (10.1 MB → 4.9 MB), **85% smaller** on an academic calendar (1.5 MB → 235.7 KB)
- ArrayBuffers are transferred, not copied, and workers terminate after each job

<sub>Tested on local files, single run each. Image mode rasterizes pages, so text is no longer selectable.</sub>

![React](https://img.shields.io/badge/React_18-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Web Workers](https://img.shields.io/badge/Web_Workers-10b981?style=flat-square) ![pdf-lib](https://img.shields.io/badge/pdf--lib-00D4FF?style=flat-square)

[**Live demo →**](https://enclave-pdf.vercel.app)

</td>
<td width="50%" valign="top">

### 🎧 Vibrodo
Unified cloud and local audio streaming, built with a team of three across IIIT Kalyani and NIT Durgapur.

- Cloud tracks (YouTube Data API v3) and local FLAC, WAV, ALAC and MP3 files in a single queue
- **Listening rooms** keep devices in sync over WebSockets by reconciling playback drift against server time

<sub>Application code is private. The [architecture write-up](https://github.com/abhinavkdeval08-design/Vibrodo) is public and I am happy to walk through it.</sub>

![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![WebSockets](https://img.shields.io/badge/WebSockets-7C3AED?style=flat-square)

[**Architecture →**](https://github.com/abhinavkdeval08-design/Vibrodo)

</td>
</tr>
</table>

<br/>

---

## 🛠️ Tech stack

**Languages**<br/>
<img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" /> <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" />

**Backend & Cloud**<br/>
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" /> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" /> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" /> <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white" /> <img src="https://img.shields.io/badge/WebSockets-7C3AED?style=for-the-badge" /> <img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />

**Frontend & Mobile**<br/>
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" /> <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />

**Tooling**<br/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" /> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/Make-6D00CC?style=for-the-badge&logo=gnu&logoColor=white" />

<br/>

---

<details>
<summary><b>📂 All open-source work (click to expand)</b></summary>

<br/>

### 🎺 Blowhorn / Layer5 / Meshery (21 merged)

| Area | Impact | PRs |
| :--- | :--- | :--- |
| 🔐 **Security & reliability** | CSV formula injection closed, unsubscribe made safe from mail scanners, Access key rotation no longer returns 403, fleet tables sort correctly | [#496](https://github.com/blowhorn-ai/blowhorn-site/pull/496) · [#447](https://github.com/blowhorn-ai/blowhorn-site/pull/447) · [#513](https://github.com/blowhorn-ai/blowhorn-site/pull/513) · [#507](https://github.com/blowhorn-ai/blowhorn-site/pull/507) |
| 🚢 **Meshery (CNCF)** | Three `mesheryctl environment view` panics fixed and an endless UI spinner on empty component schemas (both in v1.0.77); `mesheryctl-axi system status` no longer prints `provider: null` | [#23365](https://github.com/meshery/meshery/pull/23365) · [#23357](https://github.com/meshery/meshery/pull/23357) · [axi #86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86) |
| ⚙️ **CI & tooling** | Labeler v5 mapped to the real repo layout, CI fixes for unprivileged VMs and non-standard `make` paths, label-commenter cleaned up | [#321](https://github.com/blowhorn-ai/blowhorn-site/pull/321) · [#379](https://github.com/blowhorn-ai/blowhorn-site/pull/379) · [#330](https://github.com/blowhorn-ai/blowhorn-site/pull/330) · [#332](https://github.com/blowhorn-ai/blowhorn-site/pull/332) · [#357](https://github.com/blowhorn-ai/blowhorn-site/pull/357) |
| 🧹 **Templates & community health** | Legacy Meshery references removed, orphan template deleted, support routed to `support@blowhorn.ai` | [site #250](https://github.com/blowhorn-ai/blowhorn-site/pull/250) · [#299](https://github.com/blowhorn-ai/blowhorn-site/pull/299) · [#315](https://github.com/blowhorn-ai/blowhorn-site/pull/315) · [tells #16](https://github.com/blowhorn-ai/tells/pull/16) · [#17](https://github.com/blowhorn-ai/tells/pull/17) · [#28](https://github.com/blowhorn-ai/tells/pull/28) |
| 🎨 **UI & docs** | Accessible dark-mode ink, Open Graph and Twitter cards on docs pages, intro added to Meshery docs | [#476](https://github.com/blowhorn-ai/blowhorn-site/pull/476) · [#478](https://github.com/blowhorn-ai/blowhorn-site/pull/478) · [meshery #22662](https://github.com/meshery/meshery/pull/22662) |

### 🔍 In review

- **Meshery** · [#23363](https://github.com/meshery/meshery/pull/23363) (CNCF): follow-up to #23357 applying reviewer notes (shallow copy of fetched schema and its `properties` map, plus an `Array.isArray` guard). Review feedback addressed, awaiting re-review.
- **Sistent** · [#1659](https://github.com/layer5io/sistent/pull/1659) FormHelperText, [#1660](https://github.com/layer5io/sistent/pull/1660) SubscriptionTable (CNCF).
- **AsyncAPI CLI** · [#2313](https://github.com/asyncapi/cli/pull/2313): `asyncapi diff` printed an empty `ValidationError` on unparsable files.

### 🌾 Backend work through GSSoC '26 (34 merged)

- **Agri-Vision** (10 PRs): Redis rate limiting and response caching, Celery task queue, Swagger docs, thread-safe model manager.
- **ML-CaPsule** (9 PRs) and **Eventra** (6 PRs): JWT/OTP auth refactor, persistence layer, performance and UI work.
- Plus 9 PRs across Amplitron, DevPath-Web, The-Leetcode-City, Clinical-Insight-Engine, NexaSphere, and Auto-Fill-Tool.

### 🧪 How I work

- Every fix starts from a linked issue and ships as a **small, focused PR** with tests.
- Commits are **DCO signed**, and review feedback lands as follow-up commits.
- When a fix has a known limitation, I document it directly in the PR description.

</details>

<br/>

---

## 🏅 Achievements

<table>
  <tr>
    <td width="33%" valign="top" align="center">
      <h3>🏆 GSSoC '26</h3>
      <h2>#137</h2>
      <sub>of 47,924 participants · 25,092 pts · active 13 of 13 weeks</sub>
    </td>
    <td width="34%" valign="top" align="center">
      <h3>⚔️ Competitive Programming</h3>
      <h2>420</h2>
      <sub><b>130</b> Easy · <b>176</b> Med · <b>46</b> Hard</sub><br/>
      <sub>LeetCode 1710 · Codeforces Pupil 1361 · CodeChef 1137</sub><br/>
      <sub>🔥 136-day best streak · 209 active days · 15 contests</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <h3>🎓 GFG Campus Mantri</h3>
      <h2>AIR 70</h2>
      <sub>out of 2,500</sub>
    </td>
  </tr>
</table>

<br/>

---

## 📫 Let's talk

The fastest way to reach me is [email](mailto:abhinavkdeval08@gmail.com) or [LinkedIn](https://www.linkedin.com/in/abhinavdeval/). Happy to walk through any PR above or the Vibrodo architecture.
