"""
CMP701 Studio — Blackboard Bundler
Embeds config.js inline into all three HTML files so they are fully
self-contained (no external file references) and safe to host on Blackboard.

Usage:
    python scripts/bundle.py

Output: index.html, moduleleader.html, tutor.html  (overwritten in place)
        → upload these directly to Blackboard Course Files each week
"""
import json, re, subprocess, sys
from pathlib import Path

STUDIO_DIR  = Path(__file__).parent.parent
CONFIG_PATH = STUDIO_DIR / "config.js"
HTML_FILES  = ["index.html", "moduleleader.html", "tutor.html"]
PLACEHOLDER = "<!-- CONFIG_PLACEHOLDER -->"

# ── Parse config.js using Node.js (handles unquoted keys, comments, etc.) ───
node_cmd = (
    "const c = require(require('path').resolve(process.argv[1])); "
    "process.stdout.write(JSON.stringify(c));"
)
result = subprocess.run(
    ["node", "-e", node_cmd, str(CONFIG_PATH)],
    capture_output=True, encoding="utf-8", errors="replace"
)
if result.returncode != 0:
    print("ERROR: Node.js could not parse config.js:")
    print(result.stderr)
    sys.exit(1)

cfg = json.loads(result.stdout)
print(f"Config parsed: Week {cfg['meta']['currentWeek']} | {len(cfg['guilds'])} guilds | cohort {cfg['meta']['cohort']}")

config_block = (
    "<script>\n"
    "const STUDIO_CONFIG = " + json.dumps(cfg, indent=2, ensure_ascii=False) + ";\n"
    "if (typeof module !== 'undefined') module.exports = STUDIO_CONFIG;\n"
    "</script>"
)

# ── Embed into each HTML file ─────────────────────────────────────────────────
bundled = []
for fname in HTML_FILES:
    fpath = STUDIO_DIR / fname
    if not fpath.exists():
        print(f"  skip {fname} (not found)")
        continue
    html = fpath.read_text(encoding="utf-8")
    if PLACEHOLDER in html:
        html = html.replace(PLACEHOLDER, config_block)
    else:
        # Replace previously embedded inline config
        html = re.sub(
            r"<script>\s*const STUDIO_CONFIG\s*=\s*\{.*?\};\s*(?:if \(typeof module[^<]*)?\s*</script>",
            config_block, html, flags=re.DOTALL
        )
    fpath.write_text(html, encoding="utf-8")
    bundled.append(fname)
    print(f"  OK {fname}")

print(f"\nAll {len(bundled)} files bundled. They are self-contained — no external dependencies.")
print("Upload to Blackboard Course Files and replace the old versions.")
print("\nAlso commit to GitHub:")
print("  git add . && git commit -m 'Week bundle update' && git push")
