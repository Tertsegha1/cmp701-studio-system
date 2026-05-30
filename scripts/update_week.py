#!/usr/bin/env python3
"""
CMP701 Digital Transformation Studio — Weekly Config Updater
Run each Monday morning before students arrive:
    python scripts/update_week.py
"""
import json, re, sys, os, datetime
from pathlib import Path

CONFIG_PATH  = Path(__file__).parent.parent / "config.js"
STUDIO_DIR   = Path(__file__).parent.parent
HTML_FILES   = ["index.html", "moduleleader.html", "tutor.html"]
PLACEHOLDER  = "<!-- CONFIG_PLACEHOLDER -->"

def extract_config(js_text):
    """Pull the JSON object out of the JS file, stripping JS-only syntax."""
    m = re.search(r'const STUDIO_CONFIG\s*=\s*(\{.*\})\s*;', js_text, re.DOTALL)
    if not m:
        raise ValueError("Could not find STUDIO_CONFIG in config.js")
    raw = m.group(1)
    # Strip single-line // comments (but not URLs like https://)
    raw = re.sub(r'(?<!:)//[^\n]*', '', raw)
    # Strip trailing commas before } or ] (JS allows, JSON doesn't)
    raw = re.sub(r',\s*([}\]])', r'\1', raw)
    return json.loads(raw)

def write_config(cfg, js_text):
    """Replace the STUDIO_CONFIG object in the JS file."""
    new_json = json.dumps(cfg, indent=2, ensure_ascii=False)
    updated = re.sub(
        r'const STUDIO_CONFIG\s*=\s*\{.*?\}\s*;',
        f'const STUDIO_CONFIG = {new_json};',
        js_text, flags=re.DOTALL
    )
    # Update header comment
    now = datetime.datetime.now().isoformat(timespec='seconds')
    updated = re.sub(
        r'//  Generated:.*',
        f'//  Generated: {now}',
        updated
    )
    return updated

def prompt(msg, default=None, cast=str):
    suffix = f" [{default}]" if default is not None else ""
    val = input(f"{msg}{suffix}: ").strip()
    if not val and default is not None:
        return default
    return cast(val) if val else default

def xp_entry(cfg, week):
    print(f"\n── XP Entry for Week {week} ────────────────────────────────")
    print("Enter XP earned this week for each guild (0–110). Press Enter to skip.")
    print("XP rules: 60 (submit) + 20 (peer review) + 20 (quality) + 10 (participation)")
    print()
    group = None
    for guild in cfg['guilds']:
        if guild['group'] != group:
            group = guild['group']
            sg = cfg['seminarGroups'][group]
            print(f"\n  {sg['label']} ({sg['campus']}):")
        old = guild['weeklyXP'][week - 1]
        val = input(f"    {guild['id']:14} current total {guild['xp']:4} XP | week {week} XP [{old}]: ").strip()
        if val:
            new_val = min(110, max(0, int(val)))
            guild['weeklyXP'][week - 1] = new_val
            guild['xp'] = sum(w or 0 for w in guild['weeklyXP'])
    print()

def bb_links_entry(cfg, week):
    print(f"\n── Blackboard Links for Week {week} ────────────────────────")
    print("Paste the Blackboard URLs (press Enter to keep existing).")
    grad = input(f"  Gradebook URL [{cfg['bbLinks']['gradebook'][:60] if cfg['bbLinks']['gradebook'] else 'not set'}]: ").strip()
    if grad:
        cfg['bbLinks']['gradebook'] = grad
    for key, sg in cfg['seminarGroups'].items():
        print(f"\n  {sg['label']}:")
        links = cfg['bbLinks'].get(key, {})
        cur_assign = links.get('currentAssignment', '')
        cur_peer   = links.get('peerReviewForm', '')
        assign = input(f"    Assignment URL [{cur_assign[:50] if cur_assign else 'not set'}]: ").strip()
        peer   = input(f"    Peer Review URL [{cur_peer[:50] if cur_peer else 'not set'}]: ").strip()
        if assign: cfg['bbLinks'][key]['currentAssignment'] = assign
        if peer:   cfg['bbLinks'][key]['peerReviewForm'] = peer
        ws_choice = input(f"    Update guild workspace URLs? (y/N): ").strip().lower()
        if ws_choice == 'y':
            for gid in cfg['bbLinks'][key].get('guildWorkspaces', {}):
                old = cfg['bbLinks'][key]['guildWorkspaces'].get(gid, '')
                url = input(f"      {gid} [{old[:40] if old else 'not set'}]: ").strip()
                if url:
                    cfg['bbLinks'][key]['guildWorkspaces'][gid] = url

def award_badges(cfg):
    print("\n── Badge Awards ─────────────────────────────────────────────")
    print("Award badges to guilds (press Enter to skip).")
    print("Available badges:")
    for b in cfg['badges']:
        print(f"  {b['id']:20} {b['icon']} {b['label']}")
    while True:
        guild_id = input("\nGuild ID (or Enter to finish): ").strip()
        if not guild_id:
            break
        guild = next((g for g in cfg['guilds'] if g['id'] == guild_id), None)
        if not guild:
            print(f"  Guild '{guild_id}' not found.")
            continue
        badge_id = input(f"Badge ID to award to {guild_id}: ").strip()
        badge = next((b for b in cfg['badges'] if b['id'] == badge_id), None)
        if not badge:
            print(f"  Badge '{badge_id}' not found.")
            continue
        if badge_id not in guild['badges']:
            guild['badges'].append(badge_id)
            print(f"  ✓ Awarded '{badge['label']}' to {guild_id}")
        else:
            print(f"  Guild already has this badge.")

def main():
    if not CONFIG_PATH.exists():
        print(f"ERROR: config.js not found at {CONFIG_PATH}")
        sys.exit(1)

    js_text = CONFIG_PATH.read_text(encoding='utf-8')
    cfg = extract_config(js_text)

    current_week = cfg['meta']['currentWeek']
    print("=" * 60)
    print("  CMP701 Digital Transformation Studio — Weekly Updater")
    print("=" * 60)
    print(f"\n  Current week in config: {current_week}")
    print(f"  Cohort: {cfg['meta']['cohort']}")
    print(f"  Last updated: {cfg['meta'].get('lastUpdated', 'unknown')}")
    print()

    print("What would you like to do?")
    print("  1. Advance to next week (full update)")
    print("  2. Enter XP scores only")
    print("  3. Update Blackboard links only")
    print("  4. Award badges")
    print("  5. Update business names for guilds")
    print("  6. Exit without saving")
    choice = input("\nChoice [1]: ").strip() or "1"

    if choice == "6":
        print("No changes made.")
        return

    if choice == "1":
        new_week = prompt("New week number", default=min(current_week + 1, 12), cast=int)
        cfg['meta']['currentWeek'] = new_week
        cfg['meta']['lastUpdated'] = datetime.date.today().isoformat()

        cw1 = prompt("CW1 deadline date (YYYY-MM-DD)", default=cfg['meta']['cw1Deadline'])
        cw2 = prompt("CW2 deadline date (YYYY-MM-DD)", default=cfg['meta']['cw2Deadline'])
        cfg['meta']['cw1Deadline'] = cw1
        cfg['meta']['cw2Deadline'] = cw2

        week_xp = prompt(f"Enter XP scores from Week {current_week}? (y/N)", default="n")
        if week_xp.lower() == 'y':
            xp_entry(cfg, current_week)

        do_links = prompt("Update Blackboard links for new week? (y/N)", default="n")
        if do_links.lower() == 'y':
            bb_links_entry(cfg, new_week)

        wData = cfg['weeks'][new_week - 1]
        print(f"\n  ✓ Advanced to Week {new_week}: {wData['title']}")
        print(f"  Phase: {wData['phase']} | Assessment: {wData['assessmentPhase']}")

    elif choice == "2":
        week = prompt(f"Which week to enter XP for", default=current_week, cast=int)
        xp_entry(cfg, week)

    elif choice == "3":
        bb_links_entry(cfg, current_week)

    elif choice == "4":
        award_badges(cfg)

    elif choice == "5":
        print("\n── Update Business Names ────────────────────────────────")
        for g in cfg['guilds']:
            val = input(f"  {g['id']:14} [{g['business'] or 'not set'}]: ").strip()
            if val:
                g['business'] = val

    # Leaderboard summary
    print("\n── Leaderboard Snapshot ─────────────────────────────────")
    prev_group = None
    for guild in sorted(cfg['guilds'], key=lambda g: (g['group'], -g['xp'])):
        if guild['group'] != prev_group:
            sg = cfg['seminarGroups'][guild['group']]
            print(f"\n  {sg['label']}:")
            prev_group = guild['group']
        badges = ' '.join(b['icon'] for b in cfg['badges'] if b['id'] in guild['badges'])
        print(f"    {guild['id']:14} {guild['xp']:4} XP  {badges}")

    print()
    save = prompt("Save changes? (Y/n)", default="y")
    if save.lower() != 'n':
        # 1. Write config.js (source of truth / GitHub backup)
        updated_js = write_config(cfg, js_text)
        CONFIG_PATH.write_text(updated_js, encoding='utf-8')
        print(f"\n  ✓ config.js updated")

        # 2. Embed config inline in all three HTML files (Blackboard-ready)
        config_block = (
            "<script>\n"
            f"const STUDIO_CONFIG = {json.dumps(cfg, indent=2, ensure_ascii=False)};\n"
            "if (typeof module !== 'undefined') module.exports = STUDIO_CONFIG;\n"
            "</script>"
        )
        bundled = []
        for fname in HTML_FILES:
            fpath = STUDIO_DIR / fname
            if not fpath.exists():
                print(f"  ⚠ {fname} not found — skipping")
                continue
            html = fpath.read_text(encoding='utf-8')
            if PLACEHOLDER in html:
                html = html.replace(PLACEHOLDER, config_block)
            elif '<script src="config.js"></script>' in html:
                html = html.replace('<script src="config.js"></script>', config_block)
            else:
                # Config already inlined — replace the existing STUDIO_CONFIG block
                html = re.sub(
                    r'<script>\s*const STUDIO_CONFIG\s*=\s*\{.*?\};\s*(?:if \(typeof module[^<]*)?\s*</script>',
                    config_block, html, flags=re.DOTALL
                )
            fpath.write_text(html, encoding='utf-8')
            bundled.append(fname)

        if bundled:
            print(f"  ✓ Config embedded into: {', '.join(bundled)}")
            print("    → These files are self-contained and ready to upload to Blackboard")

        print("\n  Next steps:")
        print("  1. Upload index.html (and admin/tutor if changed) to Blackboard Course Files")
        print("  2. git add . && git commit -m 'Week update' && git push")
        print("  3. Verify the student dashboard shows the correct week\n")
    else:
        print("Changes discarded.")

if __name__ == '__main__':
    main()
