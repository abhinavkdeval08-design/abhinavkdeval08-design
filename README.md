<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&color=0:0a0f1e,50:0d1b2e,100:0a1628&height=200&section=header&text=Abhinav%20Deval&fontSize=52&fontAlignY=45&fontColor=ffffff&desc=Backend%20and%20real-time%20systems%20%E2%80%A2%20Building%20EnclavePDF%20%E2%80%A2%20Contributing%20to%20Layer5%20and%20AsyncAPI&descAlignY=68&descAlign=50&descSize=13&stroke=00D4FF&strokeWidth=2" />

<br/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=17&pause=1000&color=00D4FF&center=true&vCenter=true&width=750&lines=Backend+%26+real-time+systems;Building+EnclavePDF%3A+private+PDF+compression+in+the+browser;Contributing+to+Layer5+(CNCF)+%26+AsyncAPI;Founder+%40+Vibrodo%3A+free+music%2C+cloud+%2B+local;Contributing+to+Cloud+Native+(CNCF)+%26+Event-Driven+Systems;Node.js+%E2%80%A2+TypeScript+%E2%80%A2+React+Native+%E2%80%A2+C%2B%2B20)](https://git.io/typing-svg)

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhinavdeval/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/abhinav_deval07/)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/abhinavkdeval29)
[![Codolio](https://img.shields.io/badge/Codolio-00D4FF?style=for-the-badge&logo=codeforces&logoColor=0a0f1e)](https://codolio.com/profile/Abhinavdeval07)
[![Portfolio](https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=googlechrome&logoColor=00D4FF)](https://abhinavkdeval.vercel.app)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abhinavkdeval08@gmail.com)
[![Profile Views](https://komarev.com/ghpvc/?username=abhinavkdeval08-design&label=Profile+Views&color=00D4FF&style=for-the-badge)](https://github.com/abhinavkdeval08-design)

</div>

---

## ⚡ About

B.Tech ECE at **IIIT Kalyani** (Class of 2029). I build **backend services, real-time WebSocket sync, and browser-side processing** with Web Workers. Currently building **EnclavePDF** (client-side PDF compression) and contributing to **Layer5 / Blowhorn** (blowhorn-site, tells, Sistent, Meshery) and **AsyncAPI**. Founder of **Vibrodo**, a free music app.

**🕒 Availability:** IST (UTC+5:30) · Usually online evenings and weekends · Open to async collaboration

**🎯 Target:** GSoC 2027 with Layer5/Meshery and AsyncAPI, the orgs where I already contribute. Fixed `mesheryctl-axi` provider detection ([#73](https://github.com/meshery-extensions/mesheryctl-axi/issues/73) → [PR #86](https://github.com/meshery-extensions/mesheryctl-axi/pull/86)), approved by maintainers and awaiting CI/merge; next up is Go backend issues in Meshery.

<br/>

<table>
  <tr>
    <td width="20%" align="center">
      <h2>51</h2>
      <b>Merged PRs</b><br/><sub>12 repos · 34 via GSSoC '26<br/>+ 17 Layer5 ecosystem</sub>
    </td>
    <td width="20%" align="center">
      <h2>17</h2>
      <b>Merged (Layer5 ecosystem)</b><br/><sub>blowhorn-site ×13 · tells ×3 · Meshery ×1</sub>
    </td>
    <td width="20%" align="center">
      <h2>5</h2>
      <b>Open PRs</b><br/><sub>blowhorn-site · mesheryctl-axi<br/>Sistent ×2 · AsyncAPI</sub>
    </td>
    <td width="20%" align="center">
      <h2>#137</h2>
      <b>GSSoC '26 Rank</b><br/><sub>of 47,924 · Top 1%</sub>
    </td>
    <td width="20%" align="center">
      <h2>2</h2>
      <b>Projects</b><br/><sub>EnclavePDF · Vibrodo</sub>
    </td>
  </tr>
</table>

---

## 💻 Featured Projects

### 🔒 EnclavePDF: compress PDFs in the browser, the file never leaves the tab

[**Live Demo**](https://enclave-pdf.vercel.app) · [**GitHub**](https://github.com/abhinavkdeval08-design/EnclavePDF)

![React](https://img.shields.io/badge/React_18-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Web Workers](https://img.shields.io/badge/Web_Workers-10b981?style=flat-square)
![OffscreenCanvas](https://img.shields.io/badge/OffscreenCanvas-10b981?style=flat-square)
![pdf-lib](https://img.shields.io/badge/pdf--lib-00D4FF?style=flat-square)
![pdfjs-dist](https://img.shields.io/badge/pdfjs--dist-00D4FF?style=flat-square)

No backend, no account, no analytics. Load the page, switch off Wi-Fi, and it still compresses.

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>⚙️ Pipeline</h4>
      <p>In a Web Worker: image mode (pdf.js → <code>OffscreenCanvas</code> → JPEG → pdf-lib). If not smaller, lossless mode (metadata strip + object-stream repacking). If neither wins, the original file is returned.</p>
    </td>
    <td width="50%" valign="top">
      <h4>🔐 Privacy</h4>
      <p>In-app outbound-request indicator (<code>PerformanceResourceTiming</code>), plus a DevTools Network check, offline test and strict-CSP recipe in the repo README.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>🧠 Memory</h4>
      <p>Input buffer is transferred, not copied. One page bitmap at a time. 16 MP cap per page. Worker terminated after every job.</p>
    </td>
    <td width="50%" valign="top">
      <h4>🛡️ Input handling &amp; typing</h4>
      <p>Binary magic-byte sanitizer for malformed mobile-scanner headers, pdf-lib fallback, password-protected PDF support. Page ↔ worker messages share one union type, so a mismatch is a compile error.</p>
    </td>
  </tr>
</table>

**Measured** (my own test files, one run each: examples, not benchmarks)

| File | Mode | Before | After |
|---|---|---|---|
| 37-page sample PDF | Image · Balanced | 10.1 MB | 4.9 MB (52% smaller) |
| Academic calendar | Image · Balanced | 1.5 MB | 235.7 KB (85% smaller) |
| Course syllabus (mostly text) | Lossless | 696 KB | 695.8 KB |

> **Image mode:** 52–85% smaller on my two image-heavy test files, but pages are rasterized so text is no longer selectable.<br/>
> **Lossless mode:** keeps text selectable, saves little on text-heavy files (696 KB → 695.8 KB).<br/>
> **Next:** per-page text/scan detection and recompressing embedded images only.

<br/>

### 🎧 Vibrodo: a free music app, cloud and local in one queue

[**Instagram**](https://www.instagram.com/vibrodo.music_24/) · <sub>Source is private, architecture walkthrough on request</sub>

![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-7C3AED?style=flat-square)

In the spirit of Spotify and YouTube Music, but it also plays **your own files**. Search the cloud, play local tracks from one queue, and listen to free focus music (lofi for study, gym and more) with no subscription. Built by a team of three across IIIT Kalyani and NIT Durgapur. In development.

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🔀 One queue</h4>
      <p>Cloud tracks (YouTube Data API v3) and local files (FLAC, WAV, ALAC, MP3) in a single playlist. If a local copy matches a cloud result, the local file plays.</p>
    </td>
    <td width="50%" valign="top">
      <h4>🎼 Free background music</h4>
      <p>Curated royalty-free lofi and focus playlists for study, gym and chill. Free to listen.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>👥 Listening rooms</h4>
      <p>Multiple devices play the same track in sync over WebSockets. Playback is a state machine, and each client reconciles drift against server time.</p>
    </td>
    <td width="50%" valign="top">
      <h4>📱 Built for phones</h4>
      <p>Background audio lifecycle handling, local-file indexing, and a MongoDB-backed metadata cache to cut repeat API calls.</p>
    </td>
  </tr>
</table>

### More

<table>
  <tr>
    <td width="100%" valign="top">
      <h3><a href="https://github.com/abhinavkdeval08-design/DSA-Solutions-Vault">⚔️ DSA Solutions Vault</a></h3>
      <p>C++ solutions to LeetCode and Codeforces problems: arrays, hashing, sliding window, DP, graphs. 419 problems solved across platforms, tracked on <a href="https://codolio.com/profile/Abhinavdeval07">Codolio</a>.</p>
      <p>
        <img src="https://img.shields.io/badge/C++20-00599C?style=flat-square&logo=cplusplus&logoColor=white"/>
        <a href="https://leetcode.com/u/abhinav_deval07/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black"/></a>
      </p>
    </td>
  </tr>
</table>

---

## ⚙️ Open Source

### ✅ Merged in the Blowhorn / Layer5 & CNCF Ecosystem

<table>
  <tr>
    <td width="100%" valign="top">
      <h3>🔐 blowhorn-site · <code>internal-worker security &amp; correctness</code></h3>
      <p><a href="https://github.com/blowhorn-ai/blowhorn-site/pull/496">#496</a>: CSV formula injection hardening (OWASP CWE-1236): neutralizes <code>=</code>, <code>+</code>, <code>-</code>, <code>@</code>, tab and CR triggers (including leading whitespace) and quotes bare CRs to stop row splitting.</p>
      <p><a href="https://github.com/blowhorn-ai/blowhorn-site/pull/447">#447</a>: unsubscribe now requires POST, with a separate GET confirmation step.</p>
      <p><a href="https://github.com/blowhorn-ai/blowhorn-site/pull/507">#507</a>: fleet tables sort mixed storage units correctly, using exact byte keys with escaped <code>data-v</code> attributes.</p>
      <p><code>Merged · Reviewed by maintainers</code></p>
    </td>
  </tr>
  <tr>
    <td width="100%" valign="top">
      <h3>🛠️ blowhorn-site &amp; tells · <code>CI, templates and repo hygiene</code></h3>
      <p>Removed legacy Meshery references and made repo templates Blowhorn-specific: <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/250">site #250</a>, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/299">#299</a>, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/315">#315</a>, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/357">#357</a>, and for tells <a href="https://github.com/blowhorn-ai/tells/pull/16">#16</a>, <a href="https://github.com/blowhorn-ai/tells/pull/17">#17</a>, <a href="https://github.com/blowhorn-ai/tells/pull/28">#28</a> (footers and support routed to <code>support@blowhorn.ai</code>, closes <a href="https://github.com/blowhorn-ai/tells/issues/26">#26</a>).</p>
      <p>CI fixes: <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/321">#321</a> upgrade <code>actions/labeler</code> to v5, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/379">#379</a> map labeler paths to the active repo structure, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/330">#330</a> pass <code>TAR_OPTIONS</code> to stop actionlint ownership failures in VMs, <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/332">#332</a> resolve <code>make</code> dynamically and preserve host PATH in <code>MakeTargetTest</code>.</p>
      <p><code>Merged</code></p>
    </td>
  </tr>
  <tr>
    <td width="100%" valign="top">
      <h3>🎨 blowhorn-site · <code>UI &amp; docs</code></h3>
      <p><a href="https://github.com/blowhorn-ai/blowhorn-site/pull/476">#476</a>: softened dark mode ink to an accessible off-white. <a href="https://github.com/blowhorn-ai/blowhorn-site/pull/478">#478</a>: added Open Graph and Twitter card tags to the docs head.</p>
      <p><code>Merged</code></p>
    </td>
  </tr>
  <tr>
    <td width="100%" valign="top">
      <h3>🚢 Meshery · <code>docs</code></h3>
      <p><a href="https://github.com/meshery/meshery/pull/22662">meshery/meshery #22662</a> <sub>(CNCF)</sub></p>
      <p>Added my contributor introduction to the Meshery docs.</p>
      <p><code>Merged · Approved</code></p>
    </td>
  </tr>
</table>

### 🔍 In Review / Open

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🚢 mesheryctl-axi · <code>provider fallback</code></h3>
      <p><a href="https://github.com/meshery-extensions/mesheryctl-axi/pull/86">meshery-extensions/mesheryctl-axi #86</a> <sub>(CNCF · fixes #73)</sub></p>
      <p><code>system status</code> printed <code>provider: null</code>. Now resolves the provider from config context, then the token file (<code>meshery-provider</code> / <code>provider</code>), then the server's <code>/api/provider</code> (3s timeout, auth forwarded), else an explicit <code>Unknown</code>. 104 tests, with host-config isolation.</p>
      <p><code>Approved · Awaiting CI &amp; Merge</code></p>
    </td>
    <td width="50%" valign="top">
      <h3>🔑 blowhorn-site · <code>Access key rotation</code></h3>
      <p><a href="https://github.com/blowhorn-ai/blowhorn-site/pull/513">blowhorn-ai/blowhorn-site #513</a></p>
      <p>Cloudflare Access key rotation caused 403s until the 10-minute cert cache expired. Refetches certs once on an unknown <code>kid</code> and still fails closed. Known limitation (no cooldown) documented.</p>
      <p><code>Open · Reviewed</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🕸️ Sistent · <code>FormHelperText</code></h3>
      <p><a href="https://github.com/layer5io/sistent/pull/1659">layer5io/sistent #1659</a> <sub>(CNCF)</sub></p>
      <p>Base component wrapper with polymorphic ref typing and unit tests.</p>
      <p><code>Under Review · Feedback Addressed</code></p>
    </td>
    <td width="50%" valign="top">
      <h3>🕸️ Sistent · <code>SubscriptionTable</code></h3>
      <p><a href="https://github.com/layer5io/sistent/pull/1660">layer5io/sistent #1660</a> <sub>(CNCF)</sub></p>
      <p>Theme typography tokens, stable keys, accessible labels, tests.</p>
      <p><code>Under Review · Feedback Addressed</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <h3>📡 AsyncAPI CLI · <code>diff</code></h3>
      <p><a href="https://github.com/asyncapi/cli/pull/2313">asyncapi/cli #2313</a></p>
      <p><code>asyncapi diff</code> printed an empty <code>ValidationError</code> on unparsable files. Fixed the error type, stopped double-wrapping, added a fallback for plain-string errors.</p>
      <p><code>Open · Awaiting Review</code></p>
    </td>
  </tr>
</table>

<sub>Both Sistent PRs implement polymorphic ref typing, unit test coverage and theme token alignment, and went through in-depth maintainer review. Also analysing issues in the Meshery ecosystem: why a second `decodeURIComponent` on `router.query` throws `URIError` in a Meshery UI fix ([#22149](https://github.com/meshery/meshery/pull/22149)).</sub>

### ✅ Merged (Backend & Async Services)

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🌾 Agri-Vision <sub>(10 PRs)</sub></h3>
      <p>Redis rate-limiting middleware, Celery worker queues, Swagger/OpenAPI docs.</p>
      <p>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
        <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square"/>
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📅 Eventra <sub>(6 PRs)</sub></h3>
      <p>JWT/OTP auth refactor, module paths, persistence layer.</p>
      <p>
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
        <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white"/>
      </p>
    </td>
  </tr>
</table>

<sub>Contributed through GSSoC '26. Other repos: `ml-capsule` (9 PRs) and 6 more.</sub>

---

## 🏅 Achievements

<table>
  <tr>
    <td width="33%" valign="top" align="center">
      <h3>🏆 GSSoC '26</h3>
      <h2>#137</h2>
      <sub>of 47,924 participants</sub>
      <p>
        <img src="https://img.shields.io/badge/Top_1%25-GSSoC-00D4FF?style=flat-square"/>
        <img src="https://img.shields.io/badge/A--Tier-10b981?style=flat-square"/>
      </p>
      <sub>25,092 pts · active 13 of 13 weeks<br/>Badges: GSSoC Champion · Elite</sub>
    </td>
    <td width="34%" valign="top" align="center">
      <h3>⚔️ Competitive Programming</h3>
      <h2>419</h2>
      <sub>problems solved</sub>
      <p>
        <img src="https://img.shields.io/badge/LeetCode-1709-FFA116?style=flat-square&logo=leetcode&logoColor=black"/>
        <img src="https://img.shields.io/badge/Codeforces-Pupil_1361-1F8ACB?style=flat-square&logo=codeforces&logoColor=white"/>
        <img src="https://img.shields.io/badge/CodeChef_DSA-1137-5B4638?style=flat-square"/>
      </p>
      <sub><b>129</b> Easy · <b>176</b> Med · <b>46</b> Hard</sub><br/>
      <sub>🔥 <b>136-day</b> best streak · <b>209</b> active days · <b>15</b> contests</sub><br/>
      <sub>🎯 <b>Focus:</b> DP · Trees &amp; Graphs · Game Theory · D&amp;C</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <h3>🎓 GFG Campus Mantri</h3>
      <h2>AIR 70</h2>
      <sub>out of 2,500</sub>
      <p><sub>Live sessions with industry engineers<br/>Campus bootcamps · Peer DSA groups</sub></p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Arsenal

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=ts,js,cpp,c,py,linux,redis,react,nextjs,nodejs,express,mongodb,git,github&perline=14)](https://skillicons.dev)

</div>

---

<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://github-readme-stats-fast.vercel.app/api?username=abhinavkdeval08-design&show_icons=true&theme=tokyonight&hide_border=true&title_color=00D4FF&icon_color=10b981&bg_color=0d1117" height="170" alt="GitHub Stats"/>
    </td>
    <td align="center">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=abhinavkdeval08-design&theme=tokyonight&hide_border=true&ring=00D4FF&fire=10b981&currStreakLabel=00D4FF&background=0d1117" height="170" alt="GitHub Streak"/>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username=abhinavkdeval08-design&layout=compact&theme=tokyonight&hide_border=true&title_color=00D4FF&bg_color=0d1117" height="170" alt="Top Languages"/>
    </td>
  </tr>
</table>

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020818,50:0a1628,100:00D4FF&height=110&section=footer&text=Backend+%E2%80%A2+Real-Time+Systems+%E2%80%A2+Open+Source&fontSize=16&fontAlignY=68&fontColor=ffffff" />

</div>
