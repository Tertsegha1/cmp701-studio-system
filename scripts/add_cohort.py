#!/usr/bin/env python3
"""
CMP701 Digital Transformation Studio — Add New Cohort / Campus Group
Run this to generate the guild JSON for a new intake:
    python scripts/add_cohort.py

Paste the output into admin.html > Cohort tab > "New Guild Block" field,
or directly append to the guilds array in config.js.
"""
import json, math, re, csv, sys
from pathlib import Path

def clean_name(s):
    if not s:
        return None
    s = str(s).strip()
    s = re.sub(r'\s*\.\s*$', '', s).strip()
    return s or None

def read_csv_students(csv_path, name_col='Name', group_col='Group'):
    """Read students from a CSV file with Name and Group columns."""
    students = []
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = clean_name(row.get(name_col, ''))
            group = clean_name(row.get(group_col, ''))
            if name and group:
                students.append({'name': name, 'group': group})
    return students

def build_guilds(students, prefix, campus):
    """Allocate students into guilds of 3–4, return guild list."""
    n = len(students)
    n_guilds = math.ceil(n / 4)
    big_guilds = n - 3 * n_guilds  # guilds with 4 members

    guilds = []
    idx = 0
    for i in range(n_guilds):
        size = 4 if i < big_guilds else 3
        guild_id = f"{prefix}-G{i+1}"
        members = [s['name'] for s in students[idx:idx+size]]
        guilds.append({
            "id": guild_id,
            "group": prefix,
            "campus": campus,
            "xp": 0,
            "weeklyXP": [0]*12,
            "badges": [],
            "business": "",
            "_members": members,  # for reference — remove before pasting into config
        })
        idx += size
    return guilds

def main():
    print("=" * 60)
    print("  CMP701 Studio — Add New Cohort / Campus Group")
    print("=" * 60)
    print()
    print("Choose input method:")
    print("  1. Enter students manually")
    print("  2. Read from CSV file")
    method = input("Choice [1]: ").strip() or "1"

    campus = input("Campus (e.g. London, Birmingham, Manchester, Online): ").strip()
    group_label = input("Group label (e.g. Group A, Group B&C): ").strip()
    prefix_suggestion = f"{campus[:3].upper()}-{group_label.replace(' ','').replace('&','')[:4].upper()}"
    prefix = input(f"Guild prefix (e.g. {prefix_suggestion}) [{prefix_suggestion}]: ").strip() or prefix_suggestion
    tutors = input("Tutor name(s) (comma-separated): ").strip()

    students = []

    if method == "2":
        csv_path = input("Path to CSV file: ").strip().strip('"')
        if not Path(csv_path).exists():
            print(f"ERROR: File not found: {csv_path}")
            sys.exit(1)
        name_col = input("Column name for student names [Name]: ").strip() or "Name"
        students_raw = read_csv_students(csv_path, name_col=name_col)
        students = [s for s in students_raw]
        print(f"  Loaded {len(students)} students from CSV.")
    else:
        print(f"\nEnter student names one per line (empty line when done):")
        while True:
            name = input("  Student name: ").strip()
            if not name:
                break
            students.append({'name': name, 'group': group_label})

    if not students:
        print("No students entered. Exiting.")
        sys.exit(0)

    guilds = build_guilds(students, prefix, campus)
    n_guilds = len(guilds)
    print(f"\n  Created {n_guilds} guilds for {len(students)} students:")
    for g in guilds:
        print(f"    {g['id']} ({len(g['_members'])} members): {', '.join(g['_members'])}")

    # Seminar group entry for config
    sg_entry = {
        prefix: {
            "label": f"{campus} {group_label}",
            "campus": campus,
            "tutors": [t.strip() for t in tutors.split(',')],
            "color": "#1b3a6b",
            "guildCount": n_guilds,
        }
    }

    # BB links template
    bb_entry = {
        prefix: {
            "currentAssignment": "",
            "peerReviewForm": "",
            "guildWorkspaces": {g['id']: "" for g in guilds},
        }
    }

    # Tutor entry
    tutor_pin = f"{prefix[:2].upper()}{str(len(students))}"
    tutor_entries = []
    for t in tutors.split(','):
        t = t.strip()
        if t:
            tutor_entries.append({
                "name": t,
                "pin": tutor_pin,
                "role": "tutor",
                "groups": [prefix],
            })

    # Clean output (remove _members for the final paste)
    guilds_clean = [{k: v for k, v in g.items() if k != '_members'} for g in guilds]

    print("\n" + "=" * 60)
    print("  OUTPUT — paste into admin.html > Cohort > New Guild Block")
    print("=" * 60)
    print(json.dumps(guilds_clean, indent=2))

    print("\n" + "=" * 60)
    print("  ADD TO seminarGroups in config.js:")
    print("=" * 60)
    print(json.dumps(sg_entry, indent=2))

    print("\n" + "=" * 60)
    print("  ADD TO bbLinks in config.js:")
    print("=" * 60)
    print(json.dumps(bb_entry, indent=2))

    print("\n" + "=" * 60)
    print("  ADD TO tutors array in config.js (update PIN):")
    print("=" * 60)
    print(json.dumps(tutor_entries, indent=2))

    # Optionally write to a file
    out = input("\nSave output to a file? (y/N): ").strip().lower()
    if out == 'y':
        out_path = Path(__file__).parent.parent / f"new_cohort_{prefix}.json"
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump({
                "guilds": guilds_clean,
                "seminarGroups": sg_entry,
                "bbLinks": bb_entry,
                "tutors": tutor_entries,
            }, f, indent=2)
        print(f"  ✓ Saved to {out_path}")

    print("\n  Next steps:")
    print(f"  1. Add guild block to config.js > guilds array")
    print(f"  2. Add seminarGroup entry to config.js > seminarGroups")
    print(f"  3. Add bbLinks entry to config.js > bbLinks")
    print(f"  4. Add tutor entries to config.js > tutors")
    print(f"  5. Share PIN '{tutor_pin}' with tutors (change in config.js)")
    print(f"  6. Export and redeploy config.js\n")

if __name__ == '__main__':
    main()
