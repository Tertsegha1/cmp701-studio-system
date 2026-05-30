# CMP701 Digital Transformation Studio System

**Ulster University QAHE · Jun 2026 Intake · Module Leader: Dr Tertsegha Anande**

A web-based, gamified, collaborative studio system for CMP701 Digital Transformation. Runs for 12 weeks (1 June – 21 August 2026), embedded in Blackboard Ultra. No external logins, no cloud database — all data lives in `config.js`.

---

## System Overview

| File | Purpose | Audience |
|------|---------|----------|
| `index.html` | Student dashboard — quest briefs, leaderboard, XP, badges | Students (via Blackboard) |
| `moduleleader.html` | Admin panel — week updates, XP, BB links, export config | Module Leader only |
| `tutor.html` | Tutor view — guild overview, XP report builder | Tutors (PIN access) |
| `config.js` | Central data source — updated weekly and redeployed | Edited by scripts |
| `scripts/update_week.py` | CLI weekly update tool | Module Leader |
| `scripts/add_cohort.py` | Add new cohort/campus group | Module Leader |

---

## Quick Start — Each Monday Morning (~10 minutes)

### Option A: Python script (recommended)
```bash
cd studio-system
python scripts/update_week.py
```
Follow the prompts: advance week → enter XP → update links → save → deploy.

### Option B: Admin panel (browser-based)
1. Open `moduleleader.html` in a browser
2. Log in with Module Leader passcode (default: `CMP701@Studio2026`)
3. **Week Update tab** → advance week number
4. **XP Manager tab** → enter XP per guild per seminar group
5. **BB Links tab** → paste this week's Blackboard URLs
6. **Export Config tab** → click "Generate config.js" → Download
7. Upload new `config.js` to Blackboard and push to GitHub

---

## Blackboard Ultra — Hosting Setup

### Initial upload (one-time)

1. In your Blackboard Ultra course, go to **Course Content**
2. Click **"+"** → **"Create"** → **"Folder"** → name it `Studio System`
3. Inside the folder, click **"+"** → **"Upload"** and upload all 4 files:
   - `index.html`
   - `moduleleader.html`
   - `tutor.html`
   - `config.js`
4. For `index.html`: click the three-dot menu → **"Edit"** → toggle **"Visible to students"** → **On**
5. For `moduleleader.html` and `tutor.html`: keep **"Visible to students"** → **Off** (staff only)
6. Copy the URL of `index.html` from Blackboard

### Embedding in the course menu (recommended)
1. In Blackboard Ultra, go to **Course Menu** (left sidebar)
2. Click **"+"** → **"Web Link"**
3. Paste the URL of `index.html`
4. Label it: **"Studio Dashboard"**
5. This gives students a persistent top-level link to the dashboard

### Weekly config.js update
1. In Blackboard, go to **Course Files** → find `config.js`
2. Click the three-dot menu → **"Replace File"**
3. Upload the new `config.js`
4. Students see the update immediately on next page load

---

## GitHub Backup Setup

### First time
```bash
cd "C:\Users\terts\Digital Transformation Studio System\studio-system"
git init
git remote add origin https://github.com/Tertsegha1/cmp701-studio-system.git
git add .
git commit -m "Initial: CMP701 Studio System — Jun 2026"
git push -u origin main
```

### Weekly (after each config.js update)
```bash
git add config.js
git commit -m "Week X update — <date>"
git push
```

### GitHub Pages (optional — for portfolio/profile link)
1. In the GitHub repo → **Settings** → **Pages**
2. Source: **Deploy from branch** → `main` → `/ (root)`
3. Your dashboard will be live at: `https://tertsegha1.github.io/cmp701-studio-system/`
4. This URL can be embedded on `drtertseghaanande.com` (see below)

---

## Connecting to drtertseghaanande.com

Add this iframe snippet to your digital profile website to embed or link the studio:

```html
<!-- Option 1: Direct link (recommended) -->
<a href="https://tertsegha1.github.io/cmp701-studio-system/" target="_blank">
  CMP701 Digital Transformation Studio Dashboard
</a>

<!-- Option 2: Embedded iframe -->
<iframe
  src="https://tertsegha1.github.io/cmp701-studio-system/"
  width="100%" height="700" style="border:none;border-radius:10px"
  title="CMP701 Digital Transformation Studio">
</iframe>
```

Or simply add a portfolio entry linking to the GitHub repo:
`https://github.com/Tertsegha1/cmp701-studio-system`

---

## Access Control

| Role | Access | How |
|------|--------|-----|
| **Module Leader** | Full — all tabs in `moduleleader.html` | Admin password (SHA-256 hashed in config.js) |
| **Tutors** | `tutor.html` — own seminar groups only | PIN (set in config.js > tutors array) |
| **Students** | `index.html` — own guild view + leaderboard filtered to own group | Guild selector (saved in browser localStorage) |

### Default credentials
- **Admin password**: `CMP701@Studio2026` — **change this immediately** via moduleleader.html > Setup tab
- **Tutor PINs**: See `config.js > tutors` array (e.g. `TA2601`, `JO2602`, etc.)

---

## Guild Structure — Jun 2026

| Campus | Seminar Group | Guilds | Tutor(s) |
|--------|--------------|--------|----------|
| London | Group A | 5 (LDN-A-G1 to G5) | John Omokore |
| London | Group C&D | 4 (LDN-CD-G1 to G4) | John Omokore / Parvez Jugon |
| Birmingham | Group A | 6 (BHM-A-G1 to G6) | Tertsegha Anande |
| Birmingham | Group B | 3 (BHM-B-G1 to G3) | Goodluck Oguzie / Tertsegha Anande |
| Birmingham | Group E | 4 (BHM-E-G1 to G4) | Tertsegha Anande / Khadijah Hange |
| Manchester | Group A | 8 (MAN-A-G1 to G8) | Amira Ahmed |
| Manchester | Group B&C | 3 (MAN-BC-G1 to G3) | Amjed Ibraheem |
| **Total** | **7 groups** | **33 guilds** | |

---

## XP System

| Action | XP |
|--------|----|
| Submit artefact on time | 60 |
| Submit artefact late | 30 |
| Complete peer review | 20 |
| Quality — Excellent (≥70%) | +20 |
| Quality — Good (60–69%) | +10 |
| Guild participation | 10 |
| **Weekly maximum** | **110** |

---

## 12-Week Quest Arc

| Week | Date | Quest | Assessment |
|------|------|-------|-----------|
| 1 | 1 Jun | Business Snapshot | CW1 |
| 2 | 8 Jun | Digital Audit | CW1 |
| 3 | 15 Jun | Stakeholder Mapping | CW1 |
| 4 | 22 Jun | Competitor Scan | CW1 |
| **5** | **29 Jun** | **CW1 Video Presentation** | **CW1 DUE (25%)** |
| 6 | 6 Jul | Technology Horizon | CW2 |
| 7 | 13 Jul | Transformation Blueprint | CW2 |
| 8 | 20 Jul | Risk & Ethics | CW2 |
| 9 | 27 Jul | Implementation Roadmap | CW2 |
| 10 | 3 Aug | Change Management | CW2 |
| 11 | 10 Aug | Pitch Deck | CW2 |
| **12** | **17 Aug** | **CW2 Final Report** | **CW2 DUE (75%)** |

---

## Adding a New Cohort (Scalability)

```bash
python scripts/add_cohort.py
```
Follow the prompts to:
1. Enter campus, group label, prefix, tutors
2. Enter student names (or provide a CSV file)
3. Copy the generated JSON blocks into `config.js`
4. Export and redeploy

---

## Privacy & IT Compliance

- All dashboard logic runs in the student's browser — no data leaves Blackboard
- No student names are stored externally (guilds identified by code only, e.g. `BHM-A-G1`)
- No Firebase, no cloud database, no third-party analytics
- `config.js` is served from Blackboard's own servers (`learning.ulster.ac.uk`)
- Business names and XP are not personally identifiable

---

## Support

**Module Leader**: Dr Tertsegha Anande  
**Digital Profile**: https://drtertseghaanande.com/  
**GitHub Repo**: https://github.com/Tertsegha1/cmp701-studio-system  
**Issues / bugs**: Open a GitHub issue or email the Module Leader
