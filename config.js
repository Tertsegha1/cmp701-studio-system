// ═══════════════════════════════════════════════════════════════════════════
//  CMP701 Digital Transformation Studio — Central Configuration
//  Update this file each week and re-upload to Blackboard + GitHub.
//  Run: python scripts/update_week.py  to generate a new config.js
// ═══════════════════════════════════════════════════════════════════════════

const STUDIO_CONFIG = {

  // ── Module metadata ─────────────────────────────────────────────────────
  meta: {
    module: "CMP701",
    title: "Digital Transformation Studio",
    institution: "Ulster University QAHE",
    moduleLeader: "Dr Tertsegha Anande",
    cohort: "Jun2026",
    startDate: "2026-06-01",
    currentWeek: 1,
    cw1Deadline: "2026-07-03",   // Friday end of Week 5 — confirm with registry
    cw2Deadline: "2026-08-21",   // Friday end of Week 12 — confirm with registry
    // SHA-256 hash of Module Leader passcode. Default: CMP701@Studio2026
    // Run moduleleader.html > Setup tab to generate a new hash after changing password.
    mlPassword: "CMP701@Studio2026",
    version: "1.0.0",
    lastUpdated: "2026-06-01",
  },

  // ── Tutor access (PIN-based) ─────────────────────────────────────────────
  // Each tutor sees only their assigned seminar groups.
  tutors: [
    { name: "Tertsegha Anande",  pin: "MLP0701", role: "moduleleader",  groups: ["BHM-A","BHM-B","BHM-E"] },
    { name: "John Omokore",      pin: "JO0701", role: "tutor",  groups: ["LDN-A","LDN-CD"] },
    { name: "Parvez Jugon",      pin: "PJ0701", role: "tutor",  groups: ["LDN-CD"] },
    { name: "Goodluck Oguzie",   pin: "GO0701", role: "tutor",  groups: ["BHM-B"] },
    { name: "Khadijah Hange",    pin: "KH0701", role: "tutor",  groups: ["BHM-E"] },
    { name: "Amira Ahmed",       pin: "AA0701", role: "tutor",  groups: ["MAN-A"] },
    { name: "Najm Us Sama",      pin: "NS0701", role: "tutor",  groups: ["MAN-BC"] },
  ],

  // ── Seminar group definitions ────────────────────────────────────────────
  seminarGroups: {
    "LDN-A":  { label: "London Group A",       campus: "London",     tutors: ["John Omokore"],                          color: "#1b3a6b", guildCount: 5 },
    "LDN-CD": { label: "London Group C&D",     campus: "London",     tutors: ["John Omokore","Parvez Jugon"],           color: "#1b3a6b", guildCount: 4 },
    "BHM-A":  { label: "Birmingham Group A",   campus: "Birmingham", tutors: ["Tertsegha Anande"],                     color: "#0d7377", guildCount: 6 },
    "BHM-B":  { label: "Birmingham Group B",   campus: "Birmingham", tutors: ["Goodluck Oguzie","Tertsegha Anande"],   color: "#0d7377", guildCount: 3 },
    "BHM-E":  { label: "Birmingham Group E",   campus: "Birmingham", tutors: ["Tertsegha Anande","Khadijah Hange"],    color: "#0d7377", guildCount: 4 },
    "MAN-A":  { label: "Manchester Group A",   campus: "Manchester", tutors: ["Amira Ahmed"],                          color: "#7c3aed", guildCount: 8 },
    "MAN-BC": { label: "Manchester Group B&C", campus: "Manchester", tutors: ["Najm Us Sama"],                         color: "#7c3aed", guildCount: 3 },
  },

  // ── All 33 Guilds ────────────────────────────────────────────────────────
  // xp: total accumulated XP  |  weeklyXP: array[12] of XP earned per week
  // badges: earned badge IDs  |  business: chosen organisation name
  guilds: [
    // ── London Group A (5 guilds) ──
    { id:"LDN-A-G1",  group:"LDN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-A-G2",  group:"LDN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-A-G3",  group:"LDN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-A-G4",  group:"LDN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-A-G5",  group:"LDN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── London Group C&D (4 guilds) ──
    { id:"LDN-CD-G1", group:"LDN-CD", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-CD-G2", group:"LDN-CD", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-CD-G3", group:"LDN-CD", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"LDN-CD-G4", group:"LDN-CD", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── Birmingham Group A (6 guilds) ──
    { id:"BHM-A-G1",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-A-G2",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-A-G3",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-A-G4",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-A-G5",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-A-G6",  group:"BHM-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── Birmingham Group B (3 guilds) ──
    { id:"BHM-B-G1",  group:"BHM-B",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-B-G2",  group:"BHM-B",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-B-G3",  group:"BHM-B",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── Birmingham Group E (4 guilds) ──
    { id:"BHM-E-G1",  group:"BHM-E",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-E-G2",  group:"BHM-E",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-E-G3",  group:"BHM-E",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"BHM-E-G4",  group:"BHM-E",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── Manchester Group A (8 guilds) ──
    { id:"MAN-A-G1",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G2",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G3",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G4",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G5",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G6",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G7",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-A-G8",  group:"MAN-A",  xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    // ── Manchester Group B&C (3 guilds) ──
    { id:"MAN-BC-G1", group:"MAN-BC", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-BC-G2", group:"MAN-BC", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
    { id:"MAN-BC-G3", group:"MAN-BC", xp:0, weeklyXP:[0,0,0,0,0,0,0,0,0,0,0,0], badges:[], business:"" },
  ],

  // ── Badge definitions ────────────────────────────────────────────────────
  badges: [
    { id:"first_submit",    icon:"🚀", label:"Launchpad",          desc:"First guild in your group to submit Week 1" },
    { id:"streak3",         icon:"🔥", label:"On Fire",            desc:"Submitted 3 consecutive weeks on time" },
    { id:"streak6",         icon:"⚡", label:"Unstoppable",        desc:"Submitted 6 consecutive weeks on time" },
    { id:"streak12",        icon:"💎", label:"Diamond Run",        desc:"Submitted all 12 weeks on time" },
    { id:"peer_pro",        icon:"🤝", label:"Peer Review Pro",    desc:"Completed all peer reviews" },
    { id:"cw1_top",         icon:"🏆", label:"Discovery Champion", desc:"Top XP in seminar group after Week 5" },
    { id:"cw2_top",         icon:"👑", label:"Transformation Titan",desc:"Top XP in seminar group at Week 12" },
    { id:"quality_star",    icon:"⭐", label:"Quality Star",       desc:"Received 'Excellent' quality bonus 3+ times" },
    { id:"innovation",      icon:"💡", label:"Innovation Award",   desc:"Highest quality score in Weeks 6–12" },
    { id:"comeback",        icon:"📈", label:"Comeback Kid",       desc:"Rose 2+ places in leaderboard in one week" },
  ],

  // ── XP rules ─────────────────────────────────────────────────────────────
  xpRules: {
    submission_ontime:  60,
    submission_late:    30,
    peer_review:        20,
    quality_excellent:  20,
    quality_good:       10,
    quality_satisfactory: 0,
    participation:      10,
    // Max per week (all earned): 110
    weeklyMax: 110,
  },

  // ── 12-Week Quest Briefs ─────────────────────────────────────────────────
  weeks: [
    {
      week: 1,
      date: "2026-06-01",
      title: "Business Snapshot",
      phase: "Discovery Phase",
      assessmentPhase: "CW1",
      questBrief: "Your guild has been commissioned as a digital transformation consultancy. This week, you select your client organisation and build a comprehensive Business Snapshot — the foundation of your entire Discovery Report.",
      missionObjective: "Produce a 1-page Business Snapshot of your chosen organisation (approx. 500 words + supporting visuals).",
      deliverables: [
        "Organisation name, sector, size, ownership model, and geographic reach",
        "Current digital footprint (website, apps, social media, digital channels)",
        "2–3 key strategic challenges relevant to digital transformation",
        "A brief rationale for why this organisation needs a digital transformation strategy"
      ],
      organisations: ["Zara (Retail)","Mayo Clinic (Healthcare)","JPMorgan Chase (Finance)","General Electric (Manufacturing)","Tesla (Automotive)","Verizon (Telecommunications)","Netflix (Entertainment)","Marriott International (Hospitality)","Coursera (Education)","FedEx (Logistics)","Or discuss your own choice with your tutor"],
      cwAlignment: "CW1 — Introduction: Business Overview & Current State Analysis",
      learningOutcomes: ["LO1: Research digital disruption in industries","LO2: Develop digital transformation proposals"],
      peerReviewPrompt: "Review your assigned guild's Business Snapshot. Is the organisation well-chosen for a DT analysis? Are the strategic challenges relevant and clearly articulated? Provide 2 strengths and 1 constructive suggestion.",
      resources: ["Week 1 Lecture: Introduction to Digital Transformation","Week 1 Seminar: Practical Lab 01"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Choose an organisation you can research easily. Public companies or well-known global firms have the most available data. Discuss your choice with your tutor if unsure.",
    },
    {
      week: 2,
      date: "2026-06-08",
      title: "Digital Audit",
      phase: "Discovery Phase",
      assessmentPhase: "CW1",
      questBrief: "Every great transformation begins with an honest audit. This week, your guild conducts a structured assessment of your chosen organisation's current digital maturity across five key dimensions.",
      missionObjective: "Produce a Digital Maturity Assessment using a recognised framework, with supporting visualisation.",
      deliverables: [
        "Apply a digital maturity framework (e.g. IDC MaturityScape, Gartner Digital Business Model Maturity, or MIT CISR)",
        "Rate maturity across 5 dimensions: Infrastructure, Data & Analytics, Processes, Culture & People, Customer Experience",
        "Create a spider/radar diagram visualising current maturity scores",
        "Write a 300-word narrative interpreting the results and identifying the weakest dimension"
      ],
      cwAlignment: "CW1 — Current State Analysis & Digital Maturity Assessment",
      learningOutcomes: ["LO1: Evaluate digital maturity and disruption","LO4: Critically reflect on digital transformation theory"],
      peerReviewPrompt: "Review the guild's Digital Maturity Assessment. Is the framework applied correctly? Are the five dimension scores justified with evidence? Is the radar diagram clear and accurate? Suggest one improvement.",
      resources: ["Week 2 Lecture: Digital Maturity Frameworks","Week 2 Seminar: Practical Lab 02"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "The IDC MaturityScape is particularly well-evidenced in academic literature. Use publicly available annual reports, press releases, and news articles as your evidence base.",
    },
    {
      week: 3,
      date: "2026-06-15",
      title: "Stakeholder Mapping",
      phase: "Discovery Phase",
      assessmentPhase: "CW1",
      questBrief: "Digital transformation fails or succeeds because of people. This week, your guild identifies and analyses all key stakeholders — mapping their power, interest, and readiness for change.",
      missionObjective: "Produce a comprehensive Stakeholder Map with targeted engagement strategies for at least 6 stakeholder groups.",
      deliverables: [
        "Identify minimum 6 internal and external stakeholder groups",
        "Plot stakeholders on a Power/Interest grid (4 quadrants)",
        "For each quadrant, define a tailored engagement strategy (manage closely / keep satisfied / keep informed / monitor)",
        "Identify 2 stakeholders most likely to resist transformation and explain why"
      ],
      cwAlignment: "CW1 — Impact Analysis: Stakeholders, Structure & People",
      learningOutcomes: ["LO3: Justify organisational and people capabilities for DT","LO1: Evaluate industry disruption dynamics"],
      peerReviewPrompt: "Does the Power/Interest grid feel accurate for this organisation? Are the engagement strategies specific and actionable? Is the identification of likely resistors well-reasoned? Provide 2 strengths and 1 recommendation.",
      resources: ["Week 3 Lecture: Stakeholder Management in DT","Week 3 Seminar: Practical Lab 03"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Think beyond internal staff — regulators, customers, suppliers, investors, and technology vendors are all stakeholders in a digital transformation. Include external parties.",
    },
    {
      week: 4,
      date: "2026-06-22",
      title: "Competitor Scan",
      phase: "Discovery Phase",
      assessmentPhase: "CW1",
      questBrief: "Understanding the competitive digital landscape is essential for any transformation strategy. This week, your guild analyses how 2–3 competitors are leveraging digital technologies and identifies strategic opportunities for your client.",
      missionObjective: "Produce a Competitive Digital Intelligence report with a structured comparison matrix and gap analysis.",
      deliverables: [
        "Select 2–3 direct competitors or digital leaders in the same sector",
        "Create a comparison matrix across 5+ digital dimensions (e.g. AI adoption, platform model, data strategy, customer experience, automation)",
        "Identify 2–3 key digital capability gaps in your client organisation relative to competitors",
        "Propose 1–2 'quick win' digital opportunities based on the gap analysis"
      ],
      cwAlignment: "CW1 — Industry Structure, Case Studies & Industry Convergence",
      learningOutcomes: ["LO1: Research digital disruption and competitive pressures","LO2: Develop digital transformation proposals"],
      peerReviewPrompt: "Are the competitors well-chosen and genuinely comparable? Is the comparison matrix structured and evidence-based? Are the identified gaps realistic and strategically significant? Rate clarity (1–5) and provide 1 suggestion.",
      resources: ["Week 4 Lecture: Competitive Strategy in the Digital Age","Week 4 Seminar: Practical Lab 04"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Use Porter's Five Forces alongside your digital comparison matrix for extra depth. Look at competitors' digital annual reports, tech stack job postings, and press releases for evidence.",
    },
    {
      week: 5,
      date: "2026-06-29",
      title: "CW1 — Video Presentation",
      phase: "Discovery Phase",
      assessmentPhase: "CW1 SUBMISSION",
      questBrief: "This is it — your Discovery Phase culminates in your CW1 Video Presentation. Your guild compiles the four weeks of research into a compelling 7–8 minute video that showcases your understanding of the digital transformation landscape for your chosen organisation.",
      missionObjective: "Record and submit a 7–8 minute video presentation covering all Discovery Phase elements. Submit via Blackboard by the CW1 deadline.",
      deliverables: [
        "Introduction: Chosen organisation and why it needs digital transformation (1 min)",
        "Projected Document Outline: Structure of your planned CW2 report (1 min)",
        "Literature Review highlights: 2–3 key DT theories/frameworks applied to your case (2 min)",
        "Current State Analysis: Digital maturity findings and stakeholder landscape (2 min)",
        "Competitive scan: Key gaps and opportunities identified (1 min)",
        "Planned methodology and any initial data/prototypes (1 min)"
      ],
      cwAlignment: "CW1 — Full submission (25% of module mark)",
      learningOutcomes: ["LO1: Research digital disruption","LO2: Develop DT proposals"],
      peerReviewPrompt: "Watch your assigned guild's CW1 video. Is the chosen organisation a strong case for DT? Is the document outline logical? Are the DT frameworks correctly applied? Provide written feedback (150 words) covering 2 strengths and 2 areas for improvement.",
      resources: ["CW1 Feedback Sample (in course files)","Recording tools: Teams, Zoom, or Loom","CW1 Assessment Criteria Rubric (Appendix I of Coursework Brief)"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Your video is worth 25% of the module — rehearse at least twice before recording. Address the camera, use slides to support your narrative, and stay within 7–8 minutes (no time penalty for under 7 min).",
      isMilestone: true,
      milestoneLabel: "CW1 Due",
    },
    {
      week: 6,
      date: "2026-07-06",
      title: "Technology Horizon",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "The Transformation Phase begins. Armed with your Discovery findings, your guild now scouts the technology landscape — identifying the digital technologies most relevant to transforming your chosen organisation.",
      missionObjective: "Produce a Technology Horizon scan identifying 3–4 enabling technologies with a structured evaluation matrix.",
      deliverables: [
        "Identify 3–4 digital technologies most relevant to your organisation (e.g. AI/ML, IoT, Cloud, Blockchain, RPA, AR/VR, 5G, Digital Twins)",
        "For each technology: explain relevance, current adoption rate in the sector, estimated implementation cost (low/medium/high), and expected business impact",
        "Create an evaluation matrix scoring each technology on 4 criteria (feasibility, impact, cost, timeline)",
        "Recommend a primary technology with a 2–3 sentence justification"
      ],
      cwAlignment: "CW2 — Digital Transformation Strategy: Technological Solutions",
      learningOutcomes: ["LO2: Apply digital technologies and frameworks","LO4: Critically reflect on DT theory"],
      peerReviewPrompt: "Are the 4 technologies plausible choices for this organisation and sector? Is the evaluation matrix criteria consistent across all technologies? Is the recommended technology the strongest choice given the scoring? Provide a 1–5 rating for rigour and 1 constructive suggestion.",
      resources: ["Week 6 Lecture: Emerging Technologies in DT","Week 6 Seminar: Technology Horizon Scan exercise"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Your technology choices should connect directly back to the gaps you identified in Week 4's Competitor Scan. Show the thread from problem → technology → solution.",
    },
    {
      week: 7,
      date: "2026-07-13",
      title: "Transformation Blueprint",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "This week your guild designs the high-level architecture of your proposed digital transformation — mapping technology solutions to business processes and strategic objectives.",
      missionObjective: "Produce a Transformation Blueprint: a visual architecture diagram with a supporting 400-word narrative.",
      deliverables: [
        "A layered architecture diagram showing: Business Objectives → Process Layer → Technology Layer → Data Layer",
        "Map your 3–4 chosen technologies (from Week 6) to specific business processes they will transform",
        "Identify new digital business models or revenue streams enabled by the transformation",
        "Include a 'before vs after' comparison for at least 2 key processes"
      ],
      cwAlignment: "CW2 — DT Strategy: New Business Models, Platform Models, Customer Networks",
      learningOutcomes: ["LO2: Apply technologies in a DT strategy","LO3: Justify capabilities for DT"],
      peerReviewPrompt: "Does the Blueprint logically connect technologies to business objectives? Is the architecture diagram clear and structured? Are the new business models credible for this organisation? Provide 1 specific improvement suggestion.",
      resources: ["Week 7 Lecture: Transformation Architecture & Business Models","Week 7 Seminar: Blueprint Workshop"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Keep the diagram clear and readable — use a tool like Lucidchart, Miro, or even PowerPoint. The narrative should explain WHY you've made the architectural choices, not just describe what's in the diagram.",
    },
    {
      week: 8,
      date: "2026-07-20",
      title: "Risk & Ethics",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "No transformation comes without risk. This week your guild conducts a rigorous risk assessment and examines the ethical implications of your proposed digital transformation.",
      missionObjective: "Produce a Risk Register (minimum 8 risks) and an Ethics Framework addressing 3+ key ethical dimensions.",
      deliverables: [
        "Risk Register: Identify minimum 8 risks across categories (technical, operational, financial, reputational, regulatory)",
        "For each risk: Likelihood (1–5), Impact (1–5), Risk Score, Mitigation Strategy, and Risk Owner",
        "Create a Risk Heat Map (2x2 or 5x5 matrix)",
        "Ethics Framework: Address data privacy (GDPR), cybersecurity, algorithmic bias/AI ethics, and employee displacement",
        "Identify the single highest-priority risk and explain your mitigation in detail"
      ],
      cwAlignment: "CW2 — Business Process Transformation & Reflection on Feedback",
      learningOutcomes: ["LO3: Justify people capabilities for DT","LO4: Critically reflect on DT practice"],
      peerReviewPrompt: "Is the risk register comprehensive — does it miss any obvious risks for this sector? Is the heat map calibrated sensibly? Is the ethics section substantive (not just generic GDPR statements)? Rate comprehensiveness (1–5).",
      resources: ["Week 8 Lecture: Risk, Ethics & Digital Governance","Week 8 Seminar: Practical Lab 08"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "The ethics section must be specific to your organisation and transformation — do not write generic statements about GDPR. Consider AI ethics, bias in automated decisions, and employee surveillance if your technologies include AI or automation.",
    },
    {
      week: 9,
      date: "2026-07-27",
      title: "Implementation Roadmap",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "Transformation only becomes real when there's a credible plan to execute it. This week your guild develops a phased, milestone-driven 3-year Implementation Roadmap.",
      missionObjective: "Produce a 3-Year Implementation Roadmap with milestones, resource requirements, and KPIs.",
      deliverables: [
        "Phase 1 (Months 1–6): Foundation — infrastructure, data governance, quick wins",
        "Phase 2 (Months 7–18): Scale — core technology rollout, process redesign, staff training",
        "Phase 3 (Months 19–36): Optimise — AI/advanced analytics, new business models, continuous improvement",
        "For each phase: 3+ milestones, budget range (high/medium/low), team/skills required",
        "Define 5+ Key Performance Indicators (KPIs) with measurable targets and review timelines"
      ],
      cwAlignment: "CW2 — DT Strategy: Implementation and Organisational Capability",
      learningOutcomes: ["LO2: Develop a DT strategy proposal","LO3: Justify organisational capabilities"],
      peerReviewPrompt: "Is the roadmap realistic in its timelines? Are the phases well-sequenced — does Phase 1 genuinely build the foundation for Phase 2? Are the KPIs specific and measurable (SMART)? Provide your most important improvement suggestion.",
      resources: ["Week 9 Lecture: DT Implementation & Change Agility","Week 9 Seminar: Practical Lab 09"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Use a Gantt-style visual for the roadmap even if it's simplified. Examiners will appreciate a structured, scannable plan over dense prose. Your KPIs must include both leading indicators (input) and lagging indicators (outcomes).",
    },
    {
      week: 10,
      date: "2026-08-03",
      title: "Change Management",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "Technology can be bought. Culture cannot. This week your guild designs the people and change management strategy that will make your digital transformation sustainable.",
      missionObjective: "Produce a Change Management Strategy covering communication, training, and resistance management (approx. 400 words + supporting tools).",
      deliverables: [
        "Apply a recognised change management model (e.g. Kotter's 8-Step, Lewin's Change Model, ADKAR)",
        "Communication Plan: who needs to know what, when, through what channel, and from whom",
        "Training Needs Analysis: identify 3 skill gaps and propose learning interventions (formal training, job shadowing, communities of practice)",
        "Resistance Management: identify 2 likely sources of resistance and define specific tactics to address each",
        "Propose 1 innovation to foster a digital culture (e.g. hackathons, digital champions programme, innovation lab)"
      ],
      cwAlignment: "CW2 — Knowledge Management, Collaborative Working, Innovation Strategies",
      learningOutcomes: ["LO3: Justify people and organisational capabilities for DT","LO4: Critically reflect on DT practice"],
      peerReviewPrompt: "Is the chosen change model correctly applied to this organisation's context? Is the communication plan specific (not generic)? Are the resistance tactics realistic and targeted? Does the culture innovation feel fresh or generic?",
      resources: ["Week 10 Lecture: Change Management & Digital Culture","Week 10 Seminar: CW2 Discussion Session"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Your CW2 report must include a 'Reflection on Feedback' section summarising your CW1 feedback and how you incorporated it. Use this week to draft that section while your CW1 feedback is fresh.",
    },
    {
      week: 11,
      date: "2026-08-10",
      title: "Pitch Deck",
      phase: "Transformation Phase",
      assessmentPhase: "CW2",
      questBrief: "You're presenting to the board. This week your guild synthesises the entire transformation strategy into a 10-slide executive pitch deck — the kind you would present to a C-suite audience to secure investment and sign-off.",
      missionObjective: "Produce a 10-slide executive pitch deck summarising your Digital Transformation Strategy.",
      deliverables: [
        "Slide 1 — Title & Organisation",
        "Slide 2 — Business Challenge: Why transform now?",
        "Slide 3 — Current State Snapshot (Digital Maturity + Key Gaps)",
        "Slide 4 — Our Transformation Vision (2029 target state)",
        "Slide 5 — Technology Recommendations (top 3 technologies + rationale)",
        "Slide 6 — Implementation Roadmap (3-phase summary visual)",
        "Slide 7 — Risk Overview (top 3 risks + mitigations)",
        "Slide 8 — Change Management & People Strategy",
        "Slide 9 — Expected Outcomes & KPIs",
        "Slide 10 — Investment Ask & ROI Summary"
      ],
      cwAlignment: "CW2 — Full strategy synthesis (preparation for final report)",
      learningOutcomes: ["LO2: DT strategy proposal","LO1: Industry disruption and competitive pressures"],
      peerReviewPrompt: "Does the pitch tell a compelling story from problem to solution? Is the investment case credible? Which slide is weakest — and what specific improvement would you recommend? Rate overall persuasiveness (1–10).",
      resources: ["Week 11 Lecture: Innovation, Knowledge Management & the Digital Pitch","Week 11 Seminar: Pitch Deck Workshop"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Executive decks live or die by their narrative flow. Slide 2 sets the burning platform; Slide 10 must make the ROI case compelling. Every slide should be understandable in 30 seconds. Use your tutor's CW1 feedback now to strengthen your CW2 report argument.",
    },
    {
      week: 12,
      date: "2026-08-17",
      title: "CW2 — Final Submission",
      phase: "Transformation Phase",
      assessmentPhase: "CW2 SUBMISSION",
      questBrief: "The studio season finale. Your guild submits the complete Strategic Digital Transformation Report — 3,000 words of analysis, strategy, and reflection that represents the full arc of your work across 12 weeks.",
      missionObjective: "Submit your complete 3,000-word Digital Transformation Strategy Report via Blackboard by the CW2 deadline.",
      deliverables: [
        "Introduction: Business Overview + Current State Analysis",
        "Interface: How digital technologies impact the organisation's structure and people",
        "Industry Analysis: Industry structure, case studies, industry convergence",
        "Digital Transformation Strategy: Technologies, customer networks, new business models, platform models, data as asset, social media impact",
        "Business Process Transformation: Innovation strategies, knowledge management, collaborative working, role of AI/ML/data analytics",
        "Reflection on Feedback: Summary of CW1 feedback + how you incorporated it into CW2",
        "References: IEEE format, minimum 12 academic sources",
        "Plagiarism Declaration: Must be included"
      ],
      cwAlignment: "CW2 — Full submission (75% of module mark)",
      learningOutcomes: ["LO1","LO2","LO3","LO4"],
      peerReviewPrompt: "This week's peer review is a final reflection: share one insight your guild gained from reviewing other guilds' work across the 12-week studio. What will you carry forward into your career from this experience?",
      resources: ["CW2 Assessment Criteria Rubric (Appendix II of Coursework Brief)","CW2 Feedback Sample (in course files)","Turnitin submission link (via Blackboard)"],
      xpBreakdown: "60 XP (submission) + 20 XP (peer review) + up to 20 XP (quality) + 10 XP (participation) = 110 XP max",
      tutorTip: "Word count is 3,000 words (±10% = 2,700–3,300). In-text citations and references do NOT count toward the word limit. Include your plagiarism declaration. Run your Turnitin check 24 hours before the deadline.",
      isMilestone: true,
      milestoneLabel: "CW2 Due",
    },
  ],

  // ── Guild Working Contract ───────────────────────────────────────────────
  guildContract: "As a member of this guild, I commit to: attending all studio sessions and contributing actively; sharing the workload equally across all 12 weekly deliverables; giving honest, constructive, and respectful peer feedback; maintaining full academic integrity in every submission; communicating openly with my guild if I am struggling; and supporting every guild member throughout our 12-week transformation journey. Our collective XP reflects our collective effort.",

  // ── Announcements (Module Leader posts here, students see at top) ─────────
  announcements: [],

  // ── Assessment Criteria ───────────────────────────────────────────────────
  assessmentCriteria: {
    cw1: [
      { criterion: "Content Understanding", marks: 25, desc: "Demonstrates clear understanding of the assignment task and outlines a coherent plan for the final report" },
      { criterion: "Clarity & Engagement", marks: 20, desc: "Logical flow, confident delivery, and ability to engage the audience throughout the presentation" },
      { criterion: "Structure & Organisation", marks: 20, desc: "Well-structured outline covering introduction, literature review, methodology, and planned artefacts" },
      { criterion: "Visual Aids", marks: 20, desc: "Professional, relevant slides or visuals that support and enhance the verbal narrative" },
      { criterion: "Delivery & Time Management", marks: 15, desc: "Delivered within the 7-8 minute limit with clear verbal communication and appropriate pace" },
    ],
    cw2: [
      { criterion: "Introduction & Content Understanding", marks: 15, desc: "Clear business overview, current digital state analysis, and accurate reflection of CW1 feedback" },
      { criterion: "Critical Analysis", marks: 20, desc: "Evidence-based, theoretically grounded analysis of digital disruption, industry dynamics, and organisational readiness" },
      { criterion: "Digital Transformation Strategy", marks: 20, desc: "Coherent, feasible, and well-justified transformation strategy with technologies, roadmap, and KPIs" },
      { criterion: "Documentation & Structure", marks: 15, desc: "Well-structured 3000-word report with logical flow, clear headings, and professional presentation" },
      { criterion: "Evidence & Literature", marks: 15, desc: "Minimum 12 academic sources in IEEE format; evidence appropriately integrated throughout" },
      { criterion: "Artefacts Presentation & Communication", marks: 15, desc: "Professional quality of all artefacts, visuals, and written communication across the report" },
    ],
  },

  aiEnabled: true,

  // ── Student roster (used by Students tab in ML panel) ─────────────────────
  students: [
  {
    "name": "ABDUL WADUDD",
    "campus": "London",
    "guild": "LDN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Abdulrazaq Badmos Mutalib",
    "campus": "London",
    "guild": "LDN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ali Nadeem",
    "campus": "London",
    "guild": "LDN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "ANANNO BARUA",
    "campus": "London",
    "guild": "LDN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "AROOJ KHANAM",
    "campus": "London",
    "guild": "LDN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "DEV MINESHKUMAR PATEL",
    "campus": "London",
    "guild": "LDN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Gyanu Shah",
    "campus": "London",
    "guild": "LDN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Krishna Poudel",
    "campus": "London",
    "guild": "LDN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Malaika Aslam",
    "campus": "London",
    "guild": "LDN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Masrafe Rahman",
    "campus": "London",
    "guild": "LDN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Matilda Frimpong",
    "campus": "London",
    "guild": "LDN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MD KAMRUL HASAN PRINCE",
    "campus": "London",
    "guild": "LDN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MD. SAZAL KHAN",
    "campus": "London",
    "guild": "LDN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Mrinmoy Kumar Chanda",
    "campus": "London",
    "guild": "LDN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Abdullah Zulfiqar",
    "campus": "London",
    "guild": "LDN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Qasim Safdar",
    "campus": "London",
    "guild": "LDN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Musaddek Ahmed",
    "campus": "London",
    "guild": "LDN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Rahat Nawaz Tushar",
    "campus": "London",
    "guild": "LDN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Saheed Olalekan Amusat",
    "campus": "London",
    "guild": "LDN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Zeeshan Tariq",
    "campus": "London",
    "guild": "LDN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Aiza Pervaiz",
    "campus": "London",
    "guild": "LDN-CD-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ashok Ale Magar",
    "campus": "London",
    "guild": "LDN-CD-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "CHARLES CHINEMEREM EZEH",
    "campus": "London",
    "guild": "LDN-CD-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "El Mehdi Bahri",
    "campus": "London",
    "guild": "LDN-CD-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Eman Munir",
    "campus": "London",
    "guild": "LDN-CD-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Eru Poudel",
    "campus": "London",
    "guild": "LDN-CD-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "ilyas hodaiby",
    "campus": "London",
    "guild": "LDN-CD-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Mamoon Bashir",
    "campus": "London",
    "guild": "LDN-CD-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MOHAMED EL ABDOULI",
    "campus": "London",
    "guild": "LDN-CD-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Waheed Saeed",
    "campus": "London",
    "guild": "LDN-CD-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Mujeeb Ur Rehman",
    "campus": "London",
    "guild": "LDN-CD-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Sadia Sadiq",
    "campus": "London",
    "guild": "LDN-CD-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "WAJIHA FATIMA",
    "campus": "London",
    "guild": "LDN-CD-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Aayush K C",
    "campus": "Birmingham",
    "guild": "BHM-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Aftab Ali",
    "campus": "Birmingham",
    "guild": "BHM-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chibuike Bethel Nwaogu",
    "campus": "Birmingham",
    "guild": "BHM-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chibuike Victor Agodi",
    "campus": "Birmingham",
    "guild": "BHM-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chinecherem Favour Ozoegwu",
    "campus": "Birmingham",
    "guild": "BHM-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Daniyal Hassan",
    "campus": "Birmingham",
    "guild": "BHM-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "FAITH ONOSEDEBA OKOGBO",
    "campus": "Birmingham",
    "guild": "BHM-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "GHAYUR BAIG",
    "campus": "Birmingham",
    "guild": "BHM-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ilyas Matloob",
    "campus": "Birmingham",
    "guild": "BHM-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "IQRA AMJAD",
    "campus": "Birmingham",
    "guild": "BHM-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Kelechi Arthur Ogualaji",
    "campus": "Birmingham",
    "guild": "BHM-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Kelechi Okoh",
    "campus": "Birmingham",
    "guild": "BHM-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Kinza Saddam",
    "campus": "Birmingham",
    "guild": "BHM-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MALIK UMAIR SAJJAD",
    "campus": "Birmingham",
    "guild": "BHM-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Melika Delafrouz Gavgani",
    "campus": "Birmingham",
    "guild": "BHM-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Mohamed ELKADDIRI",
    "campus": "Birmingham",
    "guild": "BHM-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Mohammed Abdul Noumaan",
    "campus": "Birmingham",
    "guild": "BHM-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Hassan Ali Khan",
    "campus": "Birmingham",
    "guild": "BHM-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Usman",
    "campus": "Birmingham",
    "guild": "BHM-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Sunil Khadka",
    "campus": "Birmingham",
    "guild": "BHM-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Syed Hamza Hussain",
    "campus": "Birmingham",
    "guild": "BHM-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Usama Naveed",
    "campus": "Birmingham",
    "guild": "BHM-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Zeeshan Azeem",
    "campus": "Birmingham",
    "guild": "BHM-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Abena Asiedua Buabeng",
    "campus": "Birmingham",
    "guild": "BHM-B-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ahmed Shaukat",
    "campus": "Birmingham",
    "guild": "BHM-B-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ahsan Shahbaz",
    "campus": "Birmingham",
    "guild": "BHM-B-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "BILAL ASGHAR",
    "campus": "Birmingham",
    "guild": "BHM-B-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Burhan Uddin Rana",
    "campus": "Birmingham",
    "guild": "BHM-B-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Hamza Jameel",
    "campus": "Birmingham",
    "guild": "BHM-B-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "KENNEDY CHIMAOBI JOSHUA NKWOCHA",
    "campus": "Birmingham",
    "guild": "BHM-B-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MUHAMMED ASKKAR",
    "campus": "Birmingham",
    "guild": "BHM-B-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Oluwapelumi Emmanuel Adebisi",
    "campus": "Birmingham",
    "guild": "BHM-B-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Suleman Muhammad",
    "campus": "Birmingham",
    "guild": "BHM-B-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "TAHREEM MALIK",
    "campus": "Birmingham",
    "guild": "BHM-B-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Touqeer Ahmed",
    "campus": "Birmingham",
    "guild": "BHM-B-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Aneela Ishtiaq",
    "campus": "Birmingham",
    "guild": "BHM-E-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Anthony Olawale Jigan",
    "campus": "Birmingham",
    "guild": "BHM-E-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chibuike Godswill Okafor",
    "campus": "Birmingham",
    "guild": "BHM-E-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chigozirim Maximillian Olebara",
    "campus": "Birmingham",
    "guild": "BHM-E-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Chukwuebuka Tony Emenike",
    "campus": "Birmingham",
    "guild": "BHM-E-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Hafiz Mudassar Ali",
    "campus": "Birmingham",
    "guild": "BHM-E-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "JOY BIOBELE BELLO",
    "campus": "Birmingham",
    "guild": "BHM-E-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Nisar Mehmood",
    "campus": "Birmingham",
    "guild": "BHM-E-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "OKECHUKWU ANDERSON ANDERSON UDOKORO",
    "campus": "Birmingham",
    "guild": "BHM-E-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Raja Muhammad Adil",
    "campus": "Birmingham",
    "guild": "BHM-E-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Shalom Irede Oworu",
    "campus": "Birmingham",
    "guild": "BHM-E-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Syed Moiz Haider",
    "campus": "Birmingham",
    "guild": "BHM-E-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Usman Ahmed",
    "campus": "Birmingham",
    "guild": "BHM-E-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Fakhr-e-alam",
    "campus": "Manchester",
    "guild": "MAN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "AHMAD ALI",
    "campus": "Manchester",
    "guild": "MAN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ali Akbar",
    "campus": "Manchester",
    "guild": "MAN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "ALISHAH ASHRAF",
    "campus": "Manchester",
    "guild": "MAN-A-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Aliza Rehman",
    "campus": "Manchester",
    "guild": "MAN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Atta Ul Mustafa Saeedi",
    "campus": "Manchester",
    "guild": "MAN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Bishnu Thapa",
    "campus": "Manchester",
    "guild": "MAN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Bruno Chukwuebuka Izunwanne",
    "campus": "Manchester",
    "guild": "MAN-A-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ehab Ibrahim",
    "campus": "Manchester",
    "guild": "MAN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "ELAGBAJE EMMANUEL IKWUOBE",
    "campus": "Manchester",
    "guild": "MAN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "FADLULLAH OLANREWAJU ABDUSSALAM",
    "campus": "Manchester",
    "guild": "MAN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "HABIBUR RAHMAN",
    "campus": "Manchester",
    "guild": "MAN-A-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Haider Ali",
    "campus": "Manchester",
    "guild": "MAN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Hassan Adil",
    "campus": "Manchester",
    "guild": "MAN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Ibrahim Ahmed",
    "campus": "Manchester",
    "guild": "MAN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Kennedy Onyeka Unamadu",
    "campus": "Manchester",
    "guild": "MAN-A-G4",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Khadija Shakeel",
    "campus": "Manchester",
    "guild": "MAN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "MD IMRAN",
    "campus": "Manchester",
    "guild": "MAN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Azeem",
    "campus": "Manchester",
    "guild": "MAN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Moeez Inaam",
    "campus": "Manchester",
    "guild": "MAN-A-G5",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "NADEEM MUZAFFAR",
    "campus": "Manchester",
    "guild": "MAN-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Opeyemi Ayobami Akinfenwa",
    "campus": "Manchester",
    "guild": "MAN-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Raja Shehryar Shahid",
    "campus": "Manchester",
    "guild": "MAN-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "SAMUEL KELECHI NNAJI",
    "campus": "Manchester",
    "guild": "MAN-A-G6",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Shazia Liaqat",
    "campus": "Manchester",
    "guild": "MAN-A-G7",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Sikandar Ali",
    "campus": "Manchester",
    "guild": "MAN-A-G7",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Talal Farooq",
    "campus": "Manchester",
    "guild": "MAN-A-G7",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "TOBI EVANS ADEWUNMI",
    "campus": "Manchester",
    "guild": "MAN-A-G8",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Vinit Hiteshbhai Patel",
    "campus": "Manchester",
    "guild": "MAN-A-G8",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Zohaib Zulifqar",
    "campus": "Manchester",
    "guild": "MAN-A-G8",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Adnan Anwar",
    "campus": "Manchester",
    "guild": "MAN-BC-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "BASIT ALI",
    "campus": "Manchester",
    "guild": "MAN-BC-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "BRIAN KARANJA KIBUI",
    "campus": "Manchester",
    "guild": "MAN-BC-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Daniel Efosa Ogedengbe",
    "campus": "Manchester",
    "guild": "MAN-BC-G1",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Hamza Shahid",
    "campus": "Manchester",
    "guild": "MAN-BC-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Muhammad Moneeb Khawar",
    "campus": "Manchester",
    "guild": "MAN-BC-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Nameera Sofin",
    "campus": "Manchester",
    "guild": "MAN-BC-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Noman Yousaf",
    "campus": "Manchester",
    "guild": "MAN-BC-G2",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "Rohan",
    "campus": "Manchester",
    "guild": "MAN-BC-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "SAMUEL UKACHUKWU AMADI",
    "campus": "Manchester",
    "guild": "MAN-BC-G3",
    "business": "",
    "weeksSubmitted": 0
  },
  {
    "name": "UCHENNA NZERIBE CHUKWU",
    "campus": "Manchester",
    "guild": "MAN-BC-G3",
    "business": "",
    "weeksSubmitted": 0
  }
],

  // ── Blackboard Links (update each week) ──────────────────────────────────
  // Paste the actual Blackboard assignment/discussion URLs each Monday morning.
  bbLinks: {
    gradebook: "",
    peerRotationOffset: {
      "LDN-A":  1,
      "LDN-CD": 1,
      "BHM-A":  1,
      "BHM-B":  1,
      "BHM-E":  1,
      "MAN-A":  1,
      "MAN-BC": 1,
    },
    "LDN-A": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "LDN-A-G1":"", "LDN-A-G2":"", "LDN-A-G3":"", "LDN-A-G4":"", "LDN-A-G5":"",
      },
    },
    "LDN-CD": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "LDN-CD-G1":"", "LDN-CD-G2":"", "LDN-CD-G3":"", "LDN-CD-G4":"",
      },
    },
    "BHM-A": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "BHM-A-G1":"", "BHM-A-G2":"", "BHM-A-G3":"", "BHM-A-G4":"", "BHM-A-G5":"", "BHM-A-G6":"",
      },
    },
    "BHM-B": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "BHM-B-G1":"", "BHM-B-G2":"", "BHM-B-G3":"",
      },
    },
    "BHM-E": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "BHM-E-G1":"", "BHM-E-G2":"", "BHM-E-G3":"", "BHM-E-G4":"",
      },
    },
    "MAN-A": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "MAN-A-G1":"", "MAN-A-G2":"", "MAN-A-G3":"", "MAN-A-G4":"",
        "MAN-A-G5":"", "MAN-A-G6":"", "MAN-A-G7":"", "MAN-A-G8":"",
      },
    },
    "MAN-BC": {
      currentAssignment: "",
      peerReviewForm:    "",
      guildWorkspaces: {
        "MAN-BC-G1":"", "MAN-BC-G2":"", "MAN-BC-G3":"",
      },
    },
  },

};
// End of config — do not edit below this line
if (typeof module !== 'undefined') module.exports = STUDIO_CONFIG;
