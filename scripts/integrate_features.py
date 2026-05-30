"""
Integrate missing features from reference design into index.html and moduleleader.html.
Run after editing config.js, before bundle.py.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ── 1. New CSS to inject into index.html ──────────────────────────────────────
NEW_CSS = """
/* ── Announcements ── */
.announce-bar{border-radius:9px;padding:11px 15px;margin-bottom:14px;display:flex;align-items:flex-start;gap:10px;font-size:13px;line-height:1.5}
.announce-info{background:#eff6ff;border:1px solid #bfdbfe;color:#1e40af}
.announce-warn{background:#fef3c7;border:1px solid #fde68a;color:#92400e}
.announce-good{background:#f0fdf4;border:1px solid #bbf7d0;color:#15803d}
.announce-urgent{background:#fee2e2;border:1px solid #fca5a5;color:#991b1b}
.announce-icon{font-size:16px;flex-shrink:0;margin-top:1px}
.announce-pinned{font-weight:700}

/* ── Countdown cards ── */
.countdown-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:14px}
.countdown-card{background:var(--card);border:1.5px solid var(--border);border-radius:9px;padding:13px 15px;text-align:center}
.countdown-num{font-size:28px;font-weight:800;line-height:1;color:var(--navy)}
.countdown-num.urgent{color:var(--red)}
.countdown-label{font-size:11px;color:var(--muted);margin-top:3px;text-transform:uppercase;letter-spacing:.4px}
.countdown-sub{font-size:10px;color:var(--muted);margin-top:2px}

/* ── Contract ── */
.contract-box{background:#f8fafc;border:1px solid var(--border);border-radius:8px;padding:11px 14px;font-size:12.5px;line-height:1.6;color:var(--text);margin-top:10px}
.contract-box strong{color:var(--navy)}

/* ── Submit tab ── */
.submit-field{margin-bottom:12px}
.submit-field label{display:block;font-size:11px;font-weight:600;color:var(--slate);text-transform:uppercase;letter-spacing:.4px;margin-bottom:5px}
.submit-field input,.submit-field textarea,.submit-field select{width:100%;padding:9px 12px;border:1.5px solid var(--border);border-radius:7px;font-size:13px;color:var(--text);background:#fff;font-family:inherit}
.submit-field textarea{resize:vertical;min-height:72px}
.submit-field input:focus,.submit-field textarea:focus{outline:none;border-color:var(--teal);box-shadow:0 0 0 3px rgba(13,115,119,.1)}
.drop-zone{border:2px dashed var(--border);border-radius:8px;padding:20px;text-align:center;font-size:13px;color:var(--muted);cursor:pointer;transition:all .2s;background:#fafafa}
.drop-zone:hover{border-color:var(--teal);background:#f0fdfa}
.drop-zone-icon{font-size:24px;margin-bottom:6px}
.or-divider{text-align:center;color:var(--muted);font-size:12px;margin:10px 0;position:relative}
.or-divider::before,.or-divider::after{content:'';position:absolute;top:50%;width:44%;height:1px;background:var(--border)}
.or-divider::before{left:0}.or-divider::after{right:0}

/* ── Peer review ── */
.star-row{display:flex;gap:6px;margin:6px 0}
.star{font-size:24px;cursor:pointer;opacity:.35;transition:opacity .15s;line-height:1}
.star.active{opacity:1}
.star-label{font-size:12px;color:var(--muted);margin-top:4px;min-height:16px}
.review-target{background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:10px 14px;font-size:13px;margin-bottom:14px}
.review-target strong{color:var(--navy)}

/* ── AI feedback ── */
.ai-header{display:flex;align-items:center;gap:8px;margin-bottom:12px}
.ai-icon{font-size:22px}
.ai-type-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
.ai-type-btn{padding:7px 13px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;border:1.5px solid var(--border);background:#fff;color:var(--muted);transition:all .2s}
.ai-type-btn.active{background:var(--navy);color:#fff;border-color:var(--navy)}
.ai-output{background:#0f172a;color:#e2e8f0;border-radius:8px;padding:14px;font-size:12.5px;line-height:1.7;min-height:80px;white-space:pre-wrap;word-break:break-word;margin-top:12px;display:none}
.ai-output.visible{display:block}
.ai-actions{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}
.ai-note{background:#fef3c7;border:1px solid #fde68a;border-radius:8px;padding:10px 14px;font-size:12px;color:#92400e;line-height:1.5;margin-top:12px}
.ai-prompt-box{background:#f8fafc;border:1px dashed var(--border);border-radius:8px;padding:12px;font-size:12px;font-family:monospace;line-height:1.6;color:var(--text);margin-top:10px;white-space:pre-wrap;max-height:200px;overflow-y:auto;display:none}
.ai-prompt-box.visible{display:block}
.spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .7s linear infinite;vertical-align:middle;margin-right:6px}
@keyframes spin{to{transform:rotate(360deg)}}

/* ── Criteria ── */
.criteria-phase{margin-bottom:20px}
.criteria-phase-title{font-size:13px;font-weight:700;color:var(--navy);border-bottom:2px solid var(--navy);padding-bottom:6px;margin-bottom:12px}
.criteria-row{display:grid;grid-template-columns:1fr auto;align-items:start;gap:10px;padding:9px 0;border-bottom:1px solid var(--border)}
.criteria-row:last-child{border-bottom:none}
.criteria-name{font-size:13px;font-weight:600;color:var(--text)}
.criteria-desc{font-size:11.5px;color:var(--muted);margin-top:2px;line-height:1.5}
.criteria-marks{background:var(--navy);color:#fff;border-radius:12px;padding:3px 9px;font-size:11px;font-weight:700;white-space:nowrap}
.criteria-total{background:var(--amber);color:#1e293b;border-radius:8px;padding:8px 14px;font-size:13px;font-weight:700;text-align:right;margin-top:8px}
"""

# ── 2. New HTML sections to inject into index.html ────────────────────────────

ANNOUNCE_HTML = """
  <!-- Announcements banner -->
  <div id="announcements-section"></div>
"""

COUNTDOWN_HTML = """
  <!-- Countdown to deadlines -->
  <div class="countdown-row" id="countdown-row"></div>
"""

NEW_TABS = '    <div class="tab" onclick="switchTab(\'submit\')">📝 Submit</div>\n    <div class="tab" onclick="switchTab(\'peer\')">🤝 Peer Review</div>\n    <div class="tab" onclick="switchTab(\'ai\')">🤖 AI Feedback</div>\n    <div class="tab" onclick="switchTab(\'criteria\')">📊 Criteria</div>'

# New tab panels
NEW_PANELS = """
  <!-- Tab: Submit -->
  <div class="tab-panel" id="tab-submit">
    <div class="card">
      <div class="card-header">
        <div class="card-title">Submit Your Weekly Artefact</div>
        <div id="submit-phase-tag" class="tag tag-cw1">CW1</div>
      </div>
      <div id="submit-week-desc" style="font-size:13px;color:var(--muted);margin-bottom:14px;line-height:1.5"></div>

      <div class="submit-field">
        <label>Artefact Title</label>
        <input type="text" id="sub-title" placeholder="e.g. Business Snapshot — Netflix">
      </div>

      <div class="submit-field">
        <label>Submission Link (OneDrive / Google Drive / SharePoint)</label>
        <input type="url" id="sub-link" placeholder="Paste your file link here…">
      </div>

      <div class="submit-field">
        <label>Description / Summary <span style="font-weight:400;color:var(--muted)">(what did you produce this week?)</span></label>
        <textarea id="sub-desc" placeholder="Briefly describe your artefact and key findings…"></textarea>
      </div>

      <div class="submit-field">
        <label>Reflection <span style="font-weight:400;color:var(--muted)">(what did you learn? what would you do differently?)</span></label>
        <textarea id="sub-reflect" placeholder="Reflect on your process and learning this week…"></textarea>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px">
        <button class="btn btn-teal" onclick="submitToBlackboard()">📤 Open Blackboard Submission</button>
        <button class="btn btn-ghost" onclick="copySubmissionSummary()">📋 Copy Summary</button>
      </div>
      <div id="submit-confirm" style="display:none;margin-top:10px" class="alert alert-success">
        Summary copied! Paste it into the Blackboard submission comments box.
      </div>

      <div style="margin-top:16px;padding-top:12px;border-top:1px solid var(--border)">
        <div class="section-label">Guild Working Contract</div>
        <div class="contract-box" id="guild-contract-text"></div>
      </div>
    </div>
  </div>

  <!-- Tab: Peer Review -->
  <div class="tab-panel" id="tab-peer">
    <div class="card">
      <div class="card-header">
        <div class="card-title">Peer Review</div>
        <span style="font-size:12px;color:var(--muted)" id="peer-week-label"></span>
      </div>
      <div class="review-target" id="peer-target-box">
        <strong>Reviewing this week:</strong> <span id="peer-target-guild">Loading…</span>
        <div style="font-size:11px;color:var(--muted);margin-top:3px">Rotation is automatic — your guild reviews a different guild each week.</div>
      </div>

      <div class="section-label">Peer Review Prompt</div>
      <div class="peer-prompt" id="peer-prompt-text" style="margin-bottom:14px"></div>

      <div class="submit-field">
        <label>⭐ Overall Quality Rating</label>
        <div class="star-row" id="star-row">
          <span class="star" data-val="1" onclick="setStar(1)">⭐</span>
          <span class="star" data-val="2" onclick="setStar(2)">⭐</span>
          <span class="star" data-val="3" onclick="setStar(3)">⭐</span>
          <span class="star" data-val="4" onclick="setStar(4)">⭐</span>
          <span class="star" data-val="5" onclick="setStar(5)">⭐</span>
        </div>
        <div class="star-label" id="star-label">Click to rate</div>
      </div>

      <div class="submit-field">
        <label>What did they do well? <span style="font-weight:400;color:var(--muted)">(min 50 words)</span></label>
        <textarea id="peer-well" placeholder="Describe specific strengths in their artefact…" style="min-height:90px" oninput="updateWordCount('peer-well','wc-well')"></textarea>
        <div style="font-size:11px;color:var(--muted);margin-top:3px">Words: <span id="wc-well">0</span></div>
      </div>

      <div class="submit-field">
        <label>What could they improve? <span style="font-weight:400;color:var(--muted)">(min 50 words)</span></label>
        <textarea id="peer-improve" placeholder="Give specific, constructive suggestions…" style="min-height:90px" oninput="updateWordCount('peer-improve','wc-improve')"></textarea>
        <div style="font-size:11px;color:var(--muted);margin-top:3px">Words: <span id="wc-improve">0</span></div>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button class="btn btn-teal" onclick="submitPeerReview()">🤝 Submit Peer Review</button>
        <button class="btn btn-ghost" onclick="openPeerReviewBB()">Open Blackboard Form ↗</button>
      </div>
      <div id="peer-confirm" style="display:none;margin-top:10px" class="alert alert-success">
        Peer review prepared! The formatted review has been copied. Paste it into the Blackboard peer review form.
      </div>
    </div>
  </div>

  <!-- Tab: AI Feedback -->
  <div class="tab-panel" id="tab-ai">
    <div class="card">
      <div class="ai-header">
        <div class="ai-icon">🤖</div>
        <div>
          <div class="card-title" style="margin-bottom:2px">AI Formative Feedback</div>
          <div style="font-size:12px;color:var(--muted)">Get instant feedback on your work — formative only, not formal marking</div>
        </div>
      </div>

      <div class="section-label">What are you submitting for feedback?</div>
      <div class="ai-type-row">
        <button class="ai-type-btn active" onclick="setAIType('weekly','Weekly Studio Artefact')">Weekly Artefact</button>
        <button class="ai-type-btn" onclick="setAIType('cw1','CW1 Draft — Video Script / Plan')">CW1 Draft</button>
        <button class="ai-type-btn" onclick="setAIType('cw2','CW2 Draft — Written Report')">CW2 Draft</button>
      </div>

      <div class="submit-field">
        <label>Paste your work text or a description of your artefact</label>
        <textarea id="ai-work-text" placeholder="Paste your draft, notes, outline, or describe what you've produced this week…" style="min-height:120px"></textarea>
      </div>

      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button class="btn btn-primary" id="ai-btn" onclick="getAIFeedback()">⚡ Get AI Feedback</button>
        <button class="btn btn-ghost" onclick="generatePromptOnly()">📋 Copy Prompt for Claude.ai</button>
      </div>

      <div id="ai-output" class="ai-output"></div>
      <div id="ai-actions" class="ai-actions" style="display:none">
        <button class="btn btn-ghost btn-sm" onclick="copyAIOutput()">📋 Copy Feedback</button>
        <button class="btn btn-ghost btn-sm" onclick="clearAIOutput()">✕ Clear</button>
      </div>

      <div class="ai-note">
        <strong>⚡ Using Copy Prompt for Claude.ai?</strong> Click the button, then paste into
        <a href="https://claude.ai" target="_blank" rel="noopener" style="color:#92400e;font-weight:600">claude.ai</a> to get instant feedback — no API key needed.
        <br><span style="opacity:.8">Formative feedback only — your tutor's marking in Blackboard is the official assessment.</span>
      </div>

      <div id="ai-prompt-box" class="ai-prompt-box"></div>
    </div>
  </div>

  <!-- Tab: Criteria -->
  <div class="tab-panel" id="tab-criteria">
    <div class="card">
      <div class="card-header">
        <div class="card-title">Assessment Criteria</div>
        <div style="font-size:12px;color:var(--muted)">CMP701 — 100% Coursework</div>
      </div>

      <div class="criteria-phase">
        <div class="criteria-phase-title">CW1 — Video Presentation (25% of module)</div>
        <div id="cw1-criteria"></div>
        <div class="criteria-total" id="cw1-total"></div>
      </div>

      <div class="criteria-phase">
        <div class="criteria-phase-title">CW2 — Written Report (75% of module)</div>
        <div id="cw2-criteria"></div>
        <div class="criteria-total" id="cw2-total"></div>
      </div>

      <div class="alert alert-info" style="margin-top:16px;font-size:12px">
        <strong>Grade bands:</strong> Excellent ≥70% · Good 60–69% · Satisfactory 50–59% · Poor &lt;50%
        <br>Both courseworks are individual submissions. All submissions go through Turnitin.
      </div>
    </div>
  </div>
"""

# ── 3. New JavaScript to add ──────────────────────────────────────────────────
NEW_JS = r"""
// ── Announcements ────────────────────────────────────────────────────────────
function renderAnnouncements() {
  const section = document.getElementById('announcements-section');
  if (!section) return;
  const all = (C.announcements || []).slice().sort((a,b) => (b.pinned?1:0)-(a.pinned?1:0));
  if (!all.length) { section.innerHTML = ''; return; }
  const typeMap = { info:'announce-info', warn:'announce-warn', good:'announce-good', urgent:'announce-urgent' };
  const iconMap = { info:'ℹ️', warn:'⚠️', good:'✅', urgent:'🔴' };
  section.innerHTML = all.map(a => `
    <div class="announce-bar ${typeMap[a.type]||'announce-info'}">
      <span class="announce-icon">${iconMap[a.type]||'ℹ️'}</span>
      <div>
        <div class="${a.pinned?'announce-pinned':''}">${a.title}</div>
        <div style="margin-top:2px;opacity:.85">${a.message}</div>
        <div style="font-size:10px;opacity:.6;margin-top:3px">${a.date||''}</div>
      </div>
    </div>`).join('');
}

// ── Countdown ────────────────────────────────────────────────────────────────
function renderCountdowns() {
  const row = document.getElementById('countdown-row');
  if (!row) return;
  const now = new Date();
  const cw1 = new Date(C.meta.cw1Deadline);
  const cw2 = new Date(C.meta.cw2Deadline);
  const d1 = Math.max(0, Math.ceil((cw1-now)/86400000));
  const d2 = Math.max(0, Math.ceil((cw2-now)/86400000));
  const fmt = d => d === 0 ? 'TODAY' : d === 1 ? '1 day' : `${d} days`;
  const urgent = d => d <= 7 ? 'urgent' : '';
  row.innerHTML = `
    <div class="countdown-card">
      <div class="countdown-num ${urgent(d1)}">${fmt(d1)}</div>
      <div class="countdown-label">to CW1</div>
      <div class="countdown-sub">${cw1.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'})}</div>
    </div>
    <div class="countdown-card">
      <div class="countdown-num ${urgent(d2)}">${fmt(d2)}</div>
      <div class="countdown-label">to CW2</div>
      <div class="countdown-sub">${cw2.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'})}</div>
    </div>`;
}

// ── Guild contract ────────────────────────────────────────────────────────────
function renderGuildContract() {
  const el = document.getElementById('guild-contract-text');
  if (!el) return;
  el.innerHTML = `<strong>Guild Working Contract</strong><br>${C.guildContract || 'Guild contract not yet set.'}`;
}

// ── Submit tab ────────────────────────────────────────────────────────────────
function renderSubmitTab() {
  const week = C.meta.currentWeek;
  const wData = C.weeks[week-1];
  const el = document.getElementById('submit-week-desc');
  if (el) el.innerHTML = `<strong>Week ${week}: ${wData.title}</strong> — ${wData.cwAlignment}`;
  const tag = document.getElementById('submit-phase-tag');
  if (tag) { tag.textContent = wData.assessmentPhase; tag.className = wData.assessmentPhase.includes('CW1') ? 'tag tag-cw1' : 'tag tag-cw2'; }
}

function submitToBlackboard() {
  const links = C.bbLinks[state.group] || {};
  const url = links.currentAssignment || '';
  if (url) window.open(url, '_blank');
  else alert('Blackboard submission link not yet set — check with your tutor.');
}

function copySubmissionSummary() {
  const week = C.meta.currentWeek;
  const wData = C.weeks[week-1];
  const title = document.getElementById('sub-title').value.trim() || 'Untitled';
  const link = document.getElementById('sub-link').value.trim();
  const desc = document.getElementById('sub-desc').value.trim();
  const reflect = document.getElementById('sub-reflect').value.trim();
  const guild = state.guildId || 'Unknown Guild';
  const summary = [
    `CMP701 Studio — Week ${week} Artefact Submission`,
    `Guild: ${guild} | Quest: ${wData.title}`,
    `Title: ${title}`,
    link ? `Link: ${link}` : '',
    desc ? `\nSummary:\n${desc}` : '',
    reflect ? `\nReflection:\n${reflect}` : '',
  ].filter(Boolean).join('\n');
  navigator.clipboard.writeText(summary).then(() => {
    const conf = document.getElementById('submit-confirm');
    if (conf) { conf.style.display = 'block'; setTimeout(() => conf.style.display = 'none', 4000); }
  });
}

// ── Peer review ───────────────────────────────────────────────────────────────
let _peerStar = 0;
const starLabels = ['','Poor','Needs Improvement','Satisfactory','Good','Excellent'];

function renderPeerReviewTab() {
  const week = C.meta.currentWeek;
  const wData = C.weeks[week-1];
  const el = document.getElementById('peer-week-label');
  if (el) el.textContent = `Week ${week}`;
  const prompt = document.getElementById('peer-prompt-text');
  if (prompt) prompt.textContent = wData.peerReviewPrompt;
  // Rotation: peer reviews guild at offset position in seminar group
  const groupGuilds = C.guilds.filter(g => g.group === state.group);
  const myIdx = groupGuilds.findIndex(g => g.id === state.guildId);
  const offset = (C.bbLinks.peerRotationOffset || {})[state.group] || 1;
  const targetIdx = (myIdx + offset + (week % groupGuilds.length)) % groupGuilds.length;
  const target = groupGuilds[targetIdx === myIdx ? (targetIdx+1) % groupGuilds.length : targetIdx];
  const targetEl = document.getElementById('peer-target-guild');
  if (targetEl && target) targetEl.textContent = `${target.id}${target.business ? ' — ' + target.business : ''}`;
}

function setStar(val) {
  _peerStar = val;
  document.querySelectorAll('.star').forEach((s,i) => s.classList.toggle('active', i < val));
  const lbl = document.getElementById('star-label');
  if (lbl) lbl.textContent = starLabels[val] || '';
}

function updateWordCount(inputId, countId) {
  const text = (document.getElementById(inputId)||{}).value || '';
  const count = text.trim() ? text.trim().split(/\s+/).length : 0;
  const el = document.getElementById(countId);
  if (el) { el.textContent = count; el.style.color = count >= 50 ? 'var(--green)' : 'var(--red)'; }
}

function submitPeerReview() {
  const well = (document.getElementById('peer-well')||{}).value?.trim() || '';
  const improve = (document.getElementById('peer-improve')||{}).value?.trim() || '';
  const wc1 = well ? well.split(/\s+/).length : 0;
  const wc2 = improve ? improve.split(/\s+/).length : 0;
  if (!_peerStar) { alert('Please select a star rating.'); return; }
  if (wc1 < 50) { alert('Please write at least 50 words for "What did they do well?"'); return; }
  if (wc2 < 50) { alert('Please write at least 50 words for "What could they improve?"'); return; }

  const week = C.meta.currentWeek;
  const targetEl = document.getElementById('peer-target-guild');
  const target = targetEl ? targetEl.textContent : 'Unknown';
  const review = `CMP701 Peer Review — Week ${week}\nReviewer: ${state.guildId}\nReviewing: ${target}\nRating: ${starLabels[_peerStar]} (${_peerStar}/5 stars)\n\nStrengths:\n${well}\n\nAreas for improvement:\n${improve}`;

  navigator.clipboard.writeText(review).then(() => {
    const conf = document.getElementById('peer-confirm');
    if (conf) { conf.style.display = 'block'; setTimeout(() => conf.style.display = 'none', 5000); }
    // Open BB peer review form
    const links = C.bbLinks[state.group] || {};
    if (links.peerReviewForm) window.open(links.peerReviewForm, '_blank');
  });
}

function openPeerReviewBB() {
  const links = C.bbLinks[state.group] || {};
  const url = links.peerReviewForm || '';
  if (url) window.open(url, '_blank');
  else alert('Peer review form link not yet set — check with your tutor.');
}

// ── AI Feedback ───────────────────────────────────────────────────────────────
let _aiType = 'weekly';
let _aiTypeLabel = 'Weekly Studio Artefact';

function setAIType(type, label) {
  _aiType = type; _aiTypeLabel = label;
  document.querySelectorAll('.ai-type-btn').forEach((b,i) => {
    const types = ['weekly','cw1','cw2'];
    b.classList.toggle('active', types[i] === type);
  });
}

function buildAIPrompt() {
  const week = C.meta.currentWeek;
  const wData = C.weeks[week-1];
  const guild = C.guilds.find(g => g.id === state.guildId) || {};
  const business = guild.business || state.business || '[your chosen organisation]';
  const workText = (document.getElementById('ai-work-text')||{}).value?.trim() || '';

  const criteriaMap = {
    weekly: `Assessment alignment: ${wData.cwAlignment}\nPeer review criteria: ${wData.peerReviewPrompt}`,
    cw1: `CW1 Assessment Criteria (25% of module):\n- Content Understanding (25 pts): Clear understanding of the assignment task and planned submission\n- Clarity & Engagement (20 pts): Logical flow, engaging delivery\n- Structure & Organisation (20 pts): Coherent outline covering all required sections\n- Visual Aids (20 pts): Professional, relevant slides/visuals\n- Delivery & Time Management (15 pts): Within 7-8 minutes, clear verbal communication`,
    cw2: `CW2 Assessment Criteria (75% of module):\n- Introduction & Content Understanding (15 pts): Clear business overview and current state analysis\n- Critical Analysis (20 pts): Evidence-based, theoretically grounded analysis\n- Digital Transformation Strategy (20 pts): Coherent, feasible, well-justified strategy\n- Documentation & Structure (15 pts): Well-structured 3000-word report\n- Evidence & Literature (15 pts): Min 12 academic sources, IEEE format\n- Artefacts Presentation (15 pts): Professional presentation and communication`,
  };

  const typeContext = {
    weekly: `Week ${week} studio artefact: "${wData.title}" for ${business}`,
    cw1: `CW1 Video Presentation draft/plan for ${business} (7-8 minutes)`,
    cw2: `CW2 Written Report draft for ${business} (3000 words)`,
  };

  return `You are a supportive academic tutor for CMP701 Digital Transformation at Ulster University QAHE. Provide formative (not summative) feedback on a student's work.

Context: ${typeContext[_aiType]}
${criteriaMap[_aiType]}

Student's work / description:
${workText || '[Student has not provided their work text yet]'}

Please provide:
1. **Strengths** (2-3 specific things done well)
2. **Areas to develop** (2-3 specific, actionable suggestions)
3. **Quick win** (one immediate improvement they can make)
4. **Alignment check** (how well this aligns with the assessment criteria above)

Keep feedback constructive, specific, and under 400 words. This is formative feedback only — the formal mark comes from the tutor's Blackboard assessment.`;
}

async function getAIFeedback() {
  const workText = (document.getElementById('ai-work-text')||{}).value?.trim() || '';
  if (!workText) { alert('Please paste your work or a description first.'); return; }

  const apiKey = localStorage.getItem('cmp701_ai_key');
  const outputEl = document.getElementById('ai-output');
  const actionsEl = document.getElementById('ai-actions');
  const btn = document.getElementById('ai-btn');

  if (!apiKey) {
    // Fallback: generate prompt for Claude.ai
    generatePromptOnly();
    return;
  }

  btn.innerHTML = '<span class="spinner"></span>Generating…';
  btn.disabled = true;
  if (outputEl) { outputEl.textContent = ''; outputEl.className = 'ai-output visible'; }

  try {
    const resp = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-direct-browser-access': 'true',
      },
      body: JSON.stringify({
        model: 'claude-opus-4-5',
        max_tokens: 800,
        messages: [{ role: 'user', content: buildAIPrompt() }],
      }),
    });
    const data = await resp.json();
    if (data.error) throw new Error(data.error.message);
    const text = (data.content||[]).map(b=>b.text||'').join('');
    if (outputEl) outputEl.textContent = text;
    if (actionsEl) actionsEl.style.display = 'flex';
  } catch(e) {
    if (outputEl) outputEl.textContent = `Could not reach AI service (${e.message}). Using prompt copy mode instead.`;
    generatePromptOnly();
  } finally {
    btn.innerHTML = '⚡ Get AI Feedback';
    btn.disabled = false;
  }
}

function generatePromptOnly() {
  const prompt = buildAIPrompt();
  const box = document.getElementById('ai-prompt-box');
  if (box) { box.textContent = prompt; box.className = 'ai-prompt-box visible'; }
  navigator.clipboard.writeText(prompt).catch(()=>{});
  const workText = (document.getElementById('ai-work-text')||{}).value?.trim() || '';
  if (!workText) { alert('Add your work text first so the prompt includes it.'); return; }
  // Open Claude.ai with a helpful note
  const note = document.querySelector('.ai-note');
  if (note) { note.style.background = '#f0fdf4'; note.style.borderColor = '#bbf7d0'; note.style.color = '#15803d'; }
}

function copyAIOutput() {
  const text = (document.getElementById('ai-output')||{}).textContent || '';
  navigator.clipboard.writeText(text).then(() => showToastStudent('Feedback copied!'));
}
function clearAIOutput() {
  const o = document.getElementById('ai-output'); if(o){o.className='ai-output';o.textContent='';}
  const a = document.getElementById('ai-actions'); if(a) a.style.display='none';
  const p = document.getElementById('ai-prompt-box'); if(p){p.className='ai-prompt-box';p.textContent='';}
}

function showToastStudent(msg) {
  let t = document.getElementById('student-toast');
  if (!t) { t = document.createElement('div'); t.id='student-toast'; t.style.cssText='position:fixed;bottom:20px;right:20px;background:#1e293b;color:#fff;padding:10px 16px;border-radius:8px;font-size:13px;z-index:9999;box-shadow:0 4px 16px rgba(0,0,0,.3)'; document.body.appendChild(t); }
  t.textContent = msg; t.style.opacity = '1';
  clearTimeout(t._t); t._t = setTimeout(() => t.style.opacity = '0', 2500);
}

// ── Criteria ──────────────────────────────────────────────────────────────────
function renderCriteria() {
  const crit = C.assessmentCriteria || {};
  ['cw1','cw2'].forEach(phase => {
    const el = document.getElementById(`${phase}-criteria`);
    const tot = document.getElementById(`${phase}-total`);
    const items = crit[phase] || [];
    if (!el) return;
    const total = items.reduce((s,c) => s+(c.marks||0), 0);
    el.innerHTML = items.map(c => `
      <div class="criteria-row">
        <div>
          <div class="criteria-name">${c.criterion}</div>
          ${c.desc ? `<div class="criteria-desc">${c.desc}</div>` : ''}
        </div>
        <div class="criteria-marks">${c.marks} pts</div>
      </div>`).join('');
    if (tot) tot.textContent = `Total: ${total} points`;
  });
}
"""

# ── Now apply changes to index.html ──────────────────────────────────────────
fpath = ROOT / "index.html"
html = fpath.read_text(encoding="utf-8")

# a) Inject new CSS before </style>
html = html.replace("</style>", NEW_CSS + "\n</style>", 1)

# b) Inject announcements + countdown after <div class="container">
html = html.replace(
    '<div class="container">',
    '<div class="container">\n' + ANNOUNCE_HTML + COUNTDOWN_HTML,
    1
)

# c) Add new tabs after the badges tab
html = html.replace(
    "    <div class=\"tab\" onclick=\"switchTab('badges')\">🎖 Badges</div>",
    NEW_TABS + "\n    <div class=\"tab\" onclick=\"switchTab('badges')\">🎖 Badges</div>"
)

# d) Inject new tab panels before </div>\n\n<!-- Business edit modal -->
html = html.replace(
    "\n<!-- Business edit modal -->",
    "\n" + NEW_PANELS + "\n<!-- Business edit modal -->"
)

# e) Update switchTab to include new tabs
old_switch = """function switchTab(id) {
  document.querySelectorAll('.tab').forEach((t,i) => {
    const ids = ['quest','leaderboard','actions','badges'];
    t.classList.toggle('active', ids[i] === id);
  });
  document.querySelectorAll('.tab-panel').forEach(p => {
    p.classList.toggle('active', p.id === 'tab-' + id);
  });
}"""
new_switch = """function switchTab(id) {
  const ids = ['quest','leaderboard','actions','submit','peer','ai','criteria','badges'];
  document.querySelectorAll('.tab').forEach((t,i) => t.classList.toggle('active', ids[i] === id));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('active', p.id === 'tab-' + id));
}"""
html = html.replace(old_switch, new_switch)

# f) Call new render functions inside renderAll()
old_render_end = "  // Badges\n  renderBadges(guild);"
new_render_end = """  // Badges
  renderBadges(guild);
  // New features
  renderAnnouncements();
  renderCountdowns();
  renderGuildContract();
  renderSubmitTab();
  renderPeerReviewTab();
  renderCriteria();"""
html = html.replace(old_render_end, new_render_end)

# g) Inject new JS before closing </script>
html = html.replace("\n</script>\n</body>", "\n" + NEW_JS + "\n</script>\n</body>")

fpath.write_text(html, encoding="utf-8")
print("  updated: index.html")

# ── 4. Update moduleleader.html: add Announcements tab + AI key setup ─────────
mpath = ROOT / "moduleleader.html"
ml = mpath.read_text(encoding="utf-8")

# a) Add Announcements tab button
ml = ml.replace(
    '<div class="tab" onclick="switchTab(\'setup\')">⚙️ Setup</div>',
    '<div class="tab" onclick="switchTab(\'announce\')">📢 Announcements</div>\n    <div class="tab" onclick="switchTab(\'setup\')">⚙️ Setup</div>'
)

# b) Add Announcements tab panel before Setup tab panel
ANNOUNCE_PANEL = """
  <!-- ── Tab: Announcements ── -->
  <div class="tab-panel" id="tab-announce">
    <div class="card">
      <div class="card-title">Post Announcement to Students</div>
      <div class="alert alert-info" style="margin-bottom:14px">
        Announcements appear at the top of the student dashboard. Update config.js and re-upload to publish.
      </div>
      <div class="grid-2">
        <div>
          <div class="field"><label>Title</label><input type="text" id="ann-title" placeholder="e.g. Week 2 Now Live!"></div>
          <div class="field"><label>Message</label><textarea id="ann-msg" style="min-height:80px" placeholder="Write your announcement…"></textarea></div>
          <div class="field">
            <label>Type</label>
            <select id="ann-type">
              <option value="info">ℹ Info</option>
              <option value="good">✅ Good News</option>
              <option value="warn">⚠ Important</option>
              <option value="urgent">🔴 Urgent</option>
            </select>
          </div>
          <div class="field">
            <label>Pin to top?</label>
            <select id="ann-pin"><option value="false">No</option><option value="true">Yes — show at top</option></select>
          </div>
          <button class="btn btn-primary" onclick="addAnnouncement()">📢 Add Announcement</button>
        </div>
        <div>
          <div style="font-size:12px;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px">Current Announcements</div>
          <div id="ann-list" style="font-size:13px;color:var(--muted)">Loading…</div>
          <button class="btn btn-ghost btn-sm" style="margin-top:10px" onclick="clearAllAnnouncements()">Clear All</button>
        </div>
      </div>
    </div>
  </div>

"""

ml = ml.replace(
    "  <!-- ── Tab: Setup ── -->",
    ANNOUNCE_PANEL + "  <!-- ── Tab: Setup ── -->"
)

# c) Add AI key setup inside Setup tab
AI_SETUP_HTML = """
    <div class="card">
      <div class="card-title">AI Formative Feedback — API Key</div>
      <div class="alert alert-warn" style="margin-bottom:14px">
        The API key is stored in <strong>browser localStorage only</strong> — it is never embedded in config.js or uploaded to Blackboard. Each device where you want AI feedback to work needs the key set here.
      </div>
      <div class="grid-2">
        <div>
          <div class="field"><label>Anthropic API Key</label><input type="password" id="ai-key-input" placeholder="sk-ant-…"></div>
          <div style="display:flex;gap:8px">
            <button class="btn btn-primary" onclick="saveAIKey()">Save API Key</button>
            <button class="btn btn-ghost" onclick="clearAIKey()">Clear Key</button>
          </div>
          <div id="ai-key-status" style="font-size:12px;color:var(--muted);margin-top:8px"></div>
        </div>
        <div style="font-size:12px;color:var(--muted);line-height:1.6">
          <strong style="color:var(--text)">How AI feedback works:</strong><br>
          Students paste their work into the AI Feedback tab → get instant formative feedback aligned to CW1/CW2 criteria.<br><br>
          Without an API key, students still get a <strong>copy-to-Claude.ai prompt</strong> which works in any browser.<br><br>
          Get an API key at <strong>console.anthropic.com</strong>
        </div>
      </div>
    </div>
"""

ml = ml.replace(
    "    <div class=\"card\">\n      <div class=\"card-title\">Tutor PINs Reference</div>",
    AI_SETUP_HTML + "\n    <div class=\"card\">\n      <div class=\"card-title\">Tutor PINs Reference</div>"
)

# d) Update switchTab in moduleleader.html
ml = ml.replace(
    "    const ids = ['week','xp','links','cohort','export','setup'];",
    "    const ids = ['week','xp','links','cohort','export','announce','setup'];"
)

# e) Add announcement JS functions before closing </script>
ANNOUNCE_JS = """
// ── Announcements ────────────────────────────────────────────────────────────
function renderAnnList() {
  const el = document.getElementById('ann-list');
  if (!el) return;
  const items = (mlConfig && mlConfig.announcements) ? mlConfig.announcements : (window.STUDIO_CONFIG.announcements || []);
  if (!items.length) { el.innerHTML = '<em>No announcements yet</em>'; return; }
  const typeIcon = { info:'ℹ️', warn:'⚠️', good:'✅', urgent:'🔴' };
  el.innerHTML = items.map((a,i) => `
    <div style="display:flex;align-items:flex-start;gap:8px;padding:8px 0;border-bottom:1px solid var(--border)">
      <span>${typeIcon[a.type]||'ℹ️'}</span>
      <div style="flex:1"><strong>${a.title}</strong>${a.pinned?'  📌':''}
        <div style="font-size:11px;color:var(--muted)">${a.message.slice(0,80)}${a.message.length>80?'…':''}</div>
      </div>
      <button class="btn btn-ghost btn-sm" onclick="deleteAnnouncement(${i})" style="padding:3px 8px;font-size:11px">✕</button>
    </div>`).join('');
}
function addAnnouncement() {
  const title = (document.getElementById('ann-title')||{}).value?.trim();
  const msg   = (document.getElementById('ann-msg')||{}).value?.trim();
  if (!title || !msg) { showToast('Enter a title and message.'); return; }
  if (!mlConfig) mlConfig = JSON.parse(JSON.stringify(window.STUDIO_CONFIG));
  if (!mlConfig.announcements) mlConfig.announcements = [];
  mlConfig.announcements.push({
    id: Date.now(), title, message: msg,
    type: (document.getElementById('ann-type')||{}).value || 'info',
    pinned: (document.getElementById('ann-pin')||{}).value === 'true',
    date: new Date().toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'}),
  });
  document.getElementById('ann-title').value = '';
  document.getElementById('ann-msg').value = '';
  renderAnnList();
  showToast('Announcement added. Export config to deploy.');
}
function deleteAnnouncement(idx) {
  if (!mlConfig || !mlConfig.announcements) return;
  mlConfig.announcements.splice(idx, 1);
  renderAnnList();
  showToast('Announcement removed. Export config to deploy.');
}
function clearAllAnnouncements() {
  if (!mlConfig) return;
  mlConfig.announcements = [];
  renderAnnList();
  showToast('All announcements cleared.');
}

// ── AI Key ────────────────────────────────────────────────────────────────────
function saveAIKey() {
  const key = (document.getElementById('ai-key-input')||{}).value?.trim();
  if (!key || !key.startsWith('sk-')) { showToast('Enter a valid Anthropic API key (starts with sk-).'); return; }
  localStorage.setItem('cmp701_ai_key', key);
  document.getElementById('ai-key-status').textContent = 'API key saved to this browser. AI feedback now active.';
  document.getElementById('ai-key-input').value = '';
  showToast('API key saved.');
}
function clearAIKey() {
  localStorage.removeItem('cmp701_ai_key');
  const el = document.getElementById('ai-key-status');
  if (el) el.textContent = 'API key cleared.';
  showToast('API key cleared.');
}
"""

ml = ml.replace(
    "\n// ── Toast ────────────",
    "\n" + ANNOUNCE_JS + "\n// ── Toast ────────────"
)

# f) Call renderAnnList() inside initAdmin()
ml = ml.replace(
    "  renderTutorTable();\n  renderBadgeSelectors();",
    "  renderTutorTable();\n  renderBadgeSelectors();\n  renderAnnList();\n  // Show saved AI key status\n  const aiKeyStatus = document.getElementById('ai-key-status');\n  if (aiKeyStatus) aiKeyStatus.textContent = localStorage.getItem('cmp701_ai_key') ? 'API key is configured on this device.' : 'No API key set — AI feedback uses prompt-copy mode.';"
)

mpath.write_text(ml, encoding="utf-8")
print("  updated: moduleleader.html")
print("\nDone. Run bundle.py next.")
