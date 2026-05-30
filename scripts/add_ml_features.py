"""
Add Students, Timeline, and Formative Feedback tabs to moduleleader.html.
Also adds student names from CSV to config.js.
"""
import json, re, csv
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ── 1. Read students from CSV ─────────────────────────────────────────────────
csv_path = ROOT.parent / "cmp701_jun26_studio_import.csv"
students = []
if csv_path.exists():
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            name = (row.get('Name') or '').strip()
            if name:
                students.append({
                    "name": name,
                    "campus": (row.get('Campus') or '').strip(),
                    "guild": (row.get('Guild') or '').strip(),
                    "business": (row.get('Business') or '').strip(),
                    "weeksSubmitted": 0,
                })
    print(f"  Read {len(students)} students from CSV")
else:
    print("  WARNING: CSV not found — using empty students array")

# ── 2. Add students to config.js ──────────────────────────────────────────────
config_path = ROOT / "config.js"
config_text = config_path.read_text(encoding="utf-8")

students_json = json.dumps(students, indent=2, ensure_ascii=False)

if "  students: [" not in config_text:
    config_text = config_text.replace(
        "  aiEnabled: true,",
        f"  aiEnabled: true,\n\n  // ── Student roster (used by Students tab in ML panel) ─────────────────────\n  students: {students_json},"
    )
    config_path.write_text(config_text, encoding="utf-8")
    print(f"  Added {len(students)} students to config.js")
else:
    print("  Students already in config.js — skipping")

# ── 3. New CSS for new ML tabs ────────────────────────────────────────────────
ML_CSS = """
/* Students tab */
.student-search-bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
.student-search-bar input,.student-search-bar select{padding:7px 11px;border:1.5px solid var(--border);border-radius:7px;font-size:13px;color:var(--text);background:#fff}
.student-search-bar input{flex:1;min-width:180px}
.student-table{width:100%;border-collapse:collapse;font-size:13px}
.student-table th{background:var(--navy);color:#fff;padding:8px 10px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.4px}
.student-table td{padding:8px 10px;border-bottom:1px solid var(--border);vertical-align:middle}
.student-table tr:hover td{background:#f8fafc}
.student-table tr:last-child td{border-bottom:none}
.ws-bar{display:flex;align-items:center;gap:6px}
.ws-track{width:60px;height:6px;background:var(--border);border-radius:3px;overflow:hidden;flex-shrink:0}
.ws-fill{height:100%;border-radius:3px;background:var(--teal)}
.campus-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px;flex-shrink:0}
.campus-ldn{background:#1b3a6b}.campus-bhm{background:#0d7377}.campus-man{background:#7c3aed}

/* Timeline tab */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:18px}
@media(max-width:700px){.kpi-row{grid-template-columns:1fr 1fr}}
.kpi-card{background:var(--card);border:1px solid var(--border);border-radius:9px;padding:14px;text-align:center}
.kpi-num{font-size:30px;font-weight:800;line-height:1;color:var(--navy)}
.kpi-num.urgent{color:var(--red)}
.kpi-num.teal{color:var(--teal)}
.kpi-label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.4px;margin-top:3px}
.milestone-timeline{margin-bottom:20px}
.milestone-item{display:flex;align-items:flex-start;gap:14px;padding:12px 0;border-bottom:1px solid var(--border);position:relative}
.milestone-item:last-child{border-bottom:none}
.m-icon{font-size:20px;width:36px;text-align:center;flex-shrink:0}
.m-body{flex:1}
.m-title{font-weight:700;font-size:13px;color:var(--navy)}
.m-date{font-size:12px;color:var(--muted);margin-top:2px}
.m-days{font-size:11px;font-weight:600;margin-top:3px}
.m-days.future{color:var(--teal)}.m-days.urgent{color:var(--red)}.m-days.past{color:var(--muted)}
.week-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin-top:12px}
@media(max-width:900px){.week-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:500px){.week-grid{grid-template-columns:repeat(2,1fr)}}
.week-tile{border:1.5px solid var(--border);border-radius:8px;padding:10px;font-size:11px;cursor:default;transition:box-shadow .15s}
.week-tile:hover{box-shadow:0 3px 10px rgba(0,0,0,.08)}
.week-tile.current{border-color:var(--amber);background:#fffbeb}
.week-tile.past{background:#f8fafc;opacity:.7}
.week-tile.milestone{border-color:var(--teal)}
.wt-num{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:var(--muted);margin-bottom:3px}
.wt-title{font-weight:700;color:var(--text);line-height:1.3;margin-bottom:3px}
.wt-phase{font-size:10px;color:var(--muted)}
.now-badge{display:inline-block;background:var(--amber);color:#1e293b;font-size:9px;font-weight:700;border-radius:8px;padding:1px 5px;margin-left:3px;vertical-align:middle}

/* Formative Feedback ML tab */
.ff-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:700px){.ff-grid{grid-template-columns:1fr}}
.ff-panel-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;color:#fff;background:var(--purple,#7c3aed);border-radius:7px 7px 0 0;padding:9px 14px;margin:-16px -16px 14px}
.ff-card{border:1.5px solid var(--border);border-radius:9px;padding:16px;background:var(--card)}
.ff-output{background:#1e293b;color:#e2e8f0;border-radius:8px;padding:14px;font-size:12.5px;line-height:1.7;min-height:160px;white-space:pre-wrap;word-break:break-word;font-family:'Segoe UI',sans-serif}
"""

# ── 4. New tab buttons ────────────────────────────────────────────────────────
NEW_TAB_BUTTONS = """    <div class="tab" onclick="switchTab('students')">👥 Students</div>
    <div class="tab" onclick="switchTab('timeline')">📅 Timeline</div>
    <div class="tab" onclick="switchTab('ff')">🤖 AI Feedback</div>"""

# ── 5. New tab panels HTML ────────────────────────────────────────────────────
NEW_PANELS_HTML = """
  <!-- ── Tab: Students ── -->
  <div class="tab-panel" id="tab-students">
    <div class="card">
      <div class="card-title">Student Roster — <span id="stu-count" style="font-weight:400;color:var(--muted)">Loading…</span></div>
      <div class="student-search-bar">
        <input type="text" id="stu-search" placeholder="Search student name…" oninput="renderStudentTable()">
        <select id="stu-campus" onchange="renderStudentTable()">
          <option value="">All Campuses</option>
          <option value="London">London</option>
          <option value="Birmingham">Birmingham</option>
          <option value="Manchester">Manchester</option>
        </select>
        <select id="stu-guild" onchange="renderStudentTable()">
          <option value="">All Guilds</option>
        </select>
      </div>
      <div style="overflow-x:auto">
        <table class="student-table" id="student-table">
          <thead><tr>
            <th>Name</th><th>Campus</th><th>Guild</th><th>Business</th><th>Weeks Submitted</th><th>Actions</th>
          </tr></thead>
          <tbody id="student-tbody"></tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- ── Tab: Timeline ── -->
  <div class="tab-panel" id="tab-timeline">
    <div class="card">
      <div class="card-title">Semester Timeline</div>
      <div class="kpi-row" id="tl-kpis"></div>
      <div class="milestone-timeline" id="tl-milestones"></div>
    </div>
    <div class="card">
      <div class="card-title">Week-by-Week Topics & Quests</div>
      <div class="week-grid" id="week-grid"></div>
    </div>
  </div>

  <!-- ── Tab: AI Formative Feedback (Tutor Tool) ── -->
  <div class="tab-panel" id="tab-ff">
    <div class="alert alert-warn" style="margin-bottom:14px;font-size:13px">
      <strong>Formative feedback only</strong> — this tool generates AI feedback on student work to support development. Formal CW1/CW2 marking is done in Blackboard Gradebook, not here.
    </div>
    <div class="ff-grid">
      <div class="ff-card">
        <div class="ff-panel-title">Formative Feedback — Input</div>
        <div class="field"><label>Feedback Type</label>
          <select id="ff-type">
            <option value="weekly">Weekly Studio Artefact</option>
            <option value="cw1">CW1 Draft — Video Script / Plan</option>
            <option value="cw2">CW2 Draft — Written Report</option>
          </select>
        </div>
        <div class="field"><label>Student Name</label><input type="text" id="ff-student" placeholder="e.g. Jane Smith"></div>
        <div class="field"><label>Business Chosen</label><input type="text" id="ff-business" placeholder="e.g. Netflix"></div>
        <div class="field"><label>Studio Week</label>
          <select id="ff-week">
            <option value="1">Week 1</option><option value="2">Week 2</option><option value="3">Week 3</option>
            <option value="4">Week 4</option><option value="5">Week 5</option><option value="6">Week 6</option>
            <option value="7">Week 7</option><option value="8">Week 8</option><option value="9">Week 9</option>
            <option value="10">Week 10</option><option value="11">Week 11</option><option value="12">Week 12</option>
          </select>
        </div>
        <div class="field">
          <label>Submission Text / Transcript <span style="font-weight:400;color:var(--muted)">(or describe the artefact)</span></label>
          <textarea id="ff-text" style="min-height:130px" placeholder="Paste the student's submission text, video transcript, or artefact description here…"></textarea>
        </div>
        <button class="btn btn-primary btn-full" id="ff-btn" onclick="generateMLFeedback()" style="background:#7c3aed;border-color:#7c3aed">
          ⚡ Generate Formative Feedback
        </button>
      </div>
      <div class="ff-card">
        <div class="ff-panel-title">Formative Feedback — Output</div>
        <div id="ff-output" class="ff-output" style="min-height:220px;color:#64748b;font-style:italic">AI feedback will appear here after you submit…</div>
        <div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap">
          <button class="btn btn-ghost btn-sm" onclick="copyFeedback()">📋 Copy</button>
          <button class="btn btn-ghost btn-sm" onclick="clearFeedback()">✕ Clear</button>
        </div>
      </div>
    </div>

    <!-- Assessment criteria reference -->
    <div class="card" style="margin-top:14px">
      <div class="card-title">CW Assessment Criteria Reference <span style="font-size:11px;font-weight:400;color:var(--muted)">— formal marking done in Blackboard Gradebook</span></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
        <div>
          <div style="font-weight:700;color:var(--navy);font-size:12px;margin-bottom:8px">CW1 — Video Presentation (100 pts)</div>
          <div id="ml-cw1-criteria"></div>
        </div>
        <div>
          <div style="font-weight:700;color:var(--navy);font-size:12px;margin-bottom:8px">CW2 — Written Report (100 pts)</div>
          <div id="ml-cw2-criteria"></div>
        </div>
      </div>
    </div>
  </div>

"""

# ── 6. New JS functions ───────────────────────────────────────────────────────
NEW_ML_JS = r"""
// ── Students tab ─────────────────────────────────────────────────────────────
function initStudentGuildFilter() {
  const sel = document.getElementById('stu-guild');
  if (!sel) return;
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const guilds = [...new Set((cfg.guilds||[]).map(g=>g.id))].sort();
  guilds.forEach(g => { const o = document.createElement('option'); o.value=g; o.textContent=g; sel.appendChild(o); });
}

function renderStudentTable() {
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const students = cfg.students || [];
  const q = (document.getElementById('stu-search')||{}).value?.toLowerCase() || '';
  const campus = (document.getElementById('stu-campus')||{}).value || '';
  const guild  = (document.getElementById('stu-guild')||{}).value || '';

  const filtered = students.filter(s =>
    (!q || s.name.toLowerCase().includes(q)) &&
    (!campus || s.campus === campus) &&
    (!guild || s.guild === guild)
  );

  const campusClass = c => c==='London'?'campus-ldn':c==='Birmingham'?'campus-bhm':'campus-man';
  const maxWk = 12;
  const tbody = document.getElementById('student-tbody');
  if (!tbody) return;
  tbody.innerHTML = filtered.map((s,i) => {
    const pct = Math.round((s.weeksSubmitted||0)/maxWk*100);
    return `<tr>
      <td style="font-weight:600">${s.name}</td>
      <td><span class="campus-dot ${campusClass(s.campus)}"></span>${s.campus}</td>
      <td style="font-family:monospace;font-size:12px;font-weight:600;color:var(--navy)">${s.guild}</td>
      <td style="color:${s.business?'var(--text)':'var(--muted)'};font-style:${s.business?'normal':'italic'}">${s.business||'Not chosen'}</td>
      <td>
        <div class="ws-bar">
          <div class="ws-track"><div class="ws-fill" style="width:${pct}%"></div></div>
          <span style="font-size:12px;font-weight:600">${s.weeksSubmitted||0}/${maxWk}</span>
        </div>
      </td>
      <td><button class="btn btn-ghost btn-sm" onclick="editStudent(${i})">Edit</button></td>
    </tr>`;
  }).join('');

  const countEl = document.getElementById('stu-count');
  if (countEl) countEl.textContent = `${filtered.length} of ${students.length} students`;
}

function editStudent(idx) {
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const s = (cfg.students||[])[idx];
  if (!s) return;
  const biz = prompt(`Update business for ${s.name}:`, s.business||'');
  if (biz !== null) {
    if (!mlConfig) mlConfig = JSON.parse(JSON.stringify(window.STUDIO_CONFIG));
    mlConfig.students[idx].business = biz.trim();
    renderStudentTable();
    showToast('Updated. Export config to deploy.');
  }
}

// ── Timeline tab ──────────────────────────────────────────────────────────────
function renderTimeline() {
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const week = cfg.meta.currentWeek;
  const now = new Date();
  const cw1 = new Date(cfg.meta.cw1Deadline);
  const cw2 = new Date(cfg.meta.cw2Deadline);
  const start = new Date(cfg.meta.startDate);
  const d1 = Math.ceil((cw1-now)/86400000);
  const d2 = Math.ceil((cw2-now)/86400000);
  const weeksLeft = 12 - week;

  // KPIs
  const kpis = document.getElementById('tl-kpis');
  if (kpis) kpis.innerHTML = `
    <div class="kpi-card"><div class="kpi-num${d1<=7?' urgent':''}">${Math.max(0,d1)}</div><div class="kpi-label">Days to CW1</div></div>
    <div class="kpi-card"><div class="kpi-num${d2<=14?' urgent':''}">${Math.max(0,d2)}</div><div class="kpi-label">Days to CW2</div></div>
    <div class="kpi-card"><div class="kpi-num teal">${week}</div><div class="kpi-label">Current Week</div></div>
    <div class="kpi-card"><div class="kpi-num">${weeksLeft}</div><div class="kpi-label">Weeks Remaining</div></div>`;

  // Milestone timeline
  const milestones = [
    { icon:'🎓', title:'Semester Start', date: start, label:'Semester begins' },
    { icon:'📹', title:'CW1 Submission', date: cw1, label:'Video Presentation (25%)' },
    { icon:'📄', title:'CW2 Submission', date: cw2, label:'Written Report (75%)' },
  ];
  const mEl = document.getElementById('tl-milestones');
  if (mEl) mEl.innerHTML = milestones.map(m => {
    const diff = Math.ceil((m.date-now)/86400000);
    const cls = diff < 0 ? 'past' : diff <= 7 ? 'urgent' : 'future';
    const txt = diff < 0 ? `${Math.abs(diff)} days ago` : diff === 0 ? 'Today' : `${diff} days away`;
    return `<div class="milestone-item">
      <div class="m-icon">${m.icon}</div>
      <div class="m-body">
        <div class="m-title">${m.title}</div>
        <div class="m-date">${m.date.toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'})}</div>
        <div class="m-days ${cls}">${txt}</div>
      </div>
    </div>`;
  }).join('');

  // Week grid
  const grid = document.getElementById('week-grid');
  if (grid) grid.innerHTML = (cfg.weeks||[]).map((w,i) => {
    const wk = i+1;
    const isPast = wk < week;
    const isCur = wk === week;
    const isMile = w.isMilestone;
    return `<div class="week-tile${isPast?' past':''}${isCur?' current':''}${isMile?' milestone':''}">
      <div class="wt-num">WEEK ${wk}${isCur?'<span class="now-badge">NOW</span>':''}</div>
      <div class="wt-title">${w.title}</div>
      <div class="wt-phase">${w.phase}</div>
    </div>`;
  }).join('');
}

// ── ML Formative Feedback tab ─────────────────────────────────────────────────
function renderMLCriteria() {
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const crit = cfg.assessmentCriteria || {};
  ['cw1','cw2'].forEach(phase => {
    const el = document.getElementById(`ml-${phase}-criteria`);
    if (!el) return;
    const items = crit[phase] || [];
    const total = items.reduce((s,c)=>s+(c.marks||0),0);
    el.innerHTML = `<table class="xp-table" style="font-size:12px">
      <thead><tr><th>Criterion</th><th style="text-align:right">Pts</th></tr></thead>
      <tbody>${items.map(c=>`<tr><td>${c.criterion}</td><td style="text-align:right;font-weight:700;color:var(--amber)">${c.marks}</td></tr>`).join('')}
      <tr style="background:#1b3a6b"><td style="color:#fff;font-weight:700">Total</td><td style="color:var(--amber);font-weight:800;text-align:right">${total}</td></tr>
      </tbody></table>`;
  });
}

async function generateMLFeedback() {
  const apiKey = localStorage.getItem('cmp701_ai_key');
  const type = (document.getElementById('ff-type')||{}).value || 'weekly';
  const student = (document.getElementById('ff-student')||{}).value?.trim() || 'Student';
  const business = (document.getElementById('ff-business')||{}).value?.trim() || '[not specified]';
  const weekNum = parseInt((document.getElementById('ff-week')||{}).value||'1');
  const text = (document.getElementById('ff-text')||{}).value?.trim() || '';
  const cfg = mlConfig || window.STUDIO_CONFIG;
  const wData = (cfg.weeks||[])[weekNum-1] || {};

  if (!text) { showToast('Paste the student submission text first.'); return; }

  const typeCtx = { weekly: `Week ${weekNum} studio artefact: "${wData.title||''}"`, cw1:'CW1 Video Presentation draft/script', cw2:'CW2 Written Report draft' };
  const prompt = `You are an academic tutor for CMP701 Digital Transformation (Ulster University QAHE). Generate formative (not summative) feedback for a student.

Student: ${student}
Business: ${business}
Submission type: ${typeCtx[type]||type}
${wData.cwAlignment ? 'Assessment alignment: ' + wData.cwAlignment : ''}

Student's submission:
${text}

Provide structured formative feedback with:
1. **Strengths** — 2-3 specific things done well
2. **Development areas** — 2-3 specific, actionable improvements
3. **Quick win** — one immediate action to improve this piece
4. **Assessment alignment** — how well this aligns with CMP701 assessment criteria

Keep it under 350 words. Be constructive and specific. This is formative feedback only.`;

  const outEl = document.getElementById('ff-output');
  const btn = document.getElementById('ff-btn');
  if (btn) { btn.innerHTML = '<span class="spinner"></span>Generating…'; btn.disabled = true; }

  if (!apiKey) {
    navigator.clipboard.writeText(prompt).catch(()=>{});
    if (outEl) outEl.textContent = 'No API key set.\n\nPrompt has been copied to your clipboard — paste it into Claude.ai for instant feedback.\n\n──────────\n' + prompt;
    if (btn) { btn.textContent = '⚡ Generate Formative Feedback'; btn.disabled = false; }
    return;
  }
  try {
    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method:'POST',
      headers:{'Content-Type':'application/json','x-api-key':apiKey,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},
      body: JSON.stringify({ model:'claude-opus-4-5', max_tokens:600, messages:[{role:'user',content:prompt}] })
    });
    const data = await resp.json();
    if (data.error) throw new Error(data.error.message);
    if (outEl) outEl.textContent = (data.content||[]).map(b=>b.text||'').join('');
  } catch(e) {
    navigator.clipboard.writeText(prompt).catch(()=>{});
    if (outEl) outEl.textContent = `Could not connect to AI (${e.message}).\n\nPrompt copied to clipboard — paste into Claude.ai.\n\n──────────\n${prompt}`;
  } finally {
    if (btn) { btn.textContent = '⚡ Generate Formative Feedback'; btn.disabled = false; }
  }
}
function copyFeedback() { navigator.clipboard.writeText((document.getElementById('ff-output')||{}).textContent||'').then(()=>showToast('Feedback copied!')); }
function clearFeedback() { const o=document.getElementById('ff-output'); if(o){o.textContent='AI feedback will appear here after you submit…';o.style.color='#64748b';o.style.fontStyle='italic';} }
"""

# ── Apply all changes to moduleleader.html ────────────────────────────────────
ml_path = ROOT / "moduleleader.html"
ml = ml_path.read_text(encoding="utf-8")

# a) Inject new CSS
ml = ml.replace("</style>", ML_CSS + "\n</style>", 1)

# b) Add new tab buttons before the first existing tab
ml = ml.replace(
    '    <div class="tab active" onclick="switchTab(\'week\')">',
    NEW_TAB_BUTTONS + '\n    <div class="tab active" onclick="switchTab(\'week\')">'
)

# c) Add new tab panels before closing </div> of container
ml = ml.replace(
    "\n</div>\n\n<script>",
    "\n" + NEW_PANELS_HTML + "\n</div>\n\n<script>"
)

# d) Update switchTab IDs to include new tabs
ml = ml.replace(
    "    const ids = ['week','xp','links','cohort','export','announce','setup'];",
    "    const ids = ['students','timeline','ff','week','xp','links','cohort','export','announce','setup'];"
)

# e) Inject new JS before closing </script>
ml = ml.replace(
    "\n// ── Toast ────────────",
    "\n" + NEW_ML_JS + "\n// ── Toast ────────────"
)

# f) Call new render functions at the end of initAdmin()
ml = ml.replace(
    "  renderAnnList();\n  // Show saved AI key status",
    "  renderAnnList();\n  initStudentGuildFilter();\n  renderStudentTable();\n  renderTimeline();\n  renderMLCriteria();\n  // Show saved AI key status"
)

ml_path.write_text(ml, encoding="utf-8")
print("  Updated moduleleader.html with Students, Timeline, AI Feedback tabs")
print("\nDone. Run bundle.py next.")
