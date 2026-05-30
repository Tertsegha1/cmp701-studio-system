"""Fix admin.html: replace crypto.subtle auth with simple direct comparison."""
import re
from pathlib import Path

TARGET = Path(__file__).parent.parent / "admin.html"
html = TARGET.read_text(encoding="utf-8")

# ── 1. Replace sha256 + doLogin ───────────────────────────────────────────────
old_login = r"""async function sha256\(message\) \{[^}]+\}

async function doLogin\(\) \{.*?^\}"""
new_login = """function doLogin() {
  const pw = document.getElementById('pw-input').value.trim();
  if (!pw) return;
  const stored = (adminConfig && adminConfig.meta && adminConfig.meta.adminPassword)
    || (C && C.meta && C.meta.adminPassword)
    || 'CMP701@Studio2026';
  if (pw === stored) {
    sessionStorage.setItem('cmp701_admin', '1');
    document.getElementById('login-screen').style.display = 'none';
    initAdmin();
  } else {
    const errEl = document.getElementById('login-error');
    errEl.style.cssText = 'display:block;background:#fee2e2;border:1px solid #fca5a5;color:#7f1d1d;padding:10px 14px;border-radius:8px;font-size:13px;margin-bottom:12px;text-align:left';
    errEl.textContent = 'Incorrect password. Contact the Module Leader if locked out.';
  }
}"""

result = re.sub(old_login, new_login, html, flags=re.DOTALL | re.MULTILINE)
if result == html:
    print("WARNING: sha256+doLogin pattern not matched - trying simpler approach")
    # Simpler targeted replacement
    result = html.replace(
        "async function sha256(message) {",
        "// sha256 removed - using direct comparison\nfunction _unused_sha256(message) {"
    )
    result = result.replace(
        "async function doLogin() {",
        "function doLogin() {"
    )
    # Replace the body of doLogin
    result = re.sub(
        r"function doLogin\(\) \{.*?^\}",
        new_login,
        result,
        flags=re.DOTALL | re.MULTILINE
    )

# ── 2. Replace generatePasswordHash ───────────────────────────────────────────
old_gen = re.search(r"async function generatePasswordHash\(\) \{.*?^\}", result, re.DOTALL | re.MULTILINE)
if old_gen:
    new_gen = """function generatePasswordHash() {
  const pw = document.getElementById('new-pw').value;
  const cpw = document.getElementById('confirm-pw').value;
  if (!pw) { alert('Enter a password.'); return; }
  if (pw !== cpw) { alert('Passwords do not match.'); return; }
  if (pw.length < 8) { alert('Password must be at least 8 characters.'); return; }
  document.getElementById('pw-hash-output').value = pw;
  if (adminConfig && adminConfig.meta) adminConfig.meta.adminPassword = pw;
  showToast('Password set. Export Blackboard Bundle to deploy.');
}"""
    result = result[:old_gen.start()] + new_gen + result[old_gen.end():]
    print("  generatePasswordHash replaced")
else:
    print("WARNING: generatePasswordHash not found")

# ── 3. Update Setup tab UI text ───────────────────────────────────────────────
result = result.replace(
    "After generating a new password hash, copy it into config.js (adminPasswordHash field) and re-upload.",
    "Set a new admin password below. Then click Export &rarr; Generate Blackboard Bundle and re-upload admin.html."
)
result = result.replace("Generate Hash", "Set Password")
result = result.replace(
    'placeholder="Hash will appear here…"',
    'placeholder="Your new password will appear here…"'
)
result = result.replace(
    '<label>Generated SHA-256 Hash (copy into config.js)</label>',
    '<label>New password (saved into config on export)</label>'
)

TARGET.write_text(result, encoding="utf-8")
print(f"  admin.html updated at {TARGET}")
print("Done. Run bundle.py next.")
