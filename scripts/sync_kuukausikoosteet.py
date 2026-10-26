"""Synkronoi kuukausikoosteet automaattisesti rcf_aineistovarasto-repositoriosta RCF_WIKI:iin.

Käyttö:
    python scripts/sync_kuukausikoosteet.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AINEISTOVARASTO_DIR = PROJECT_ROOT.parent / "rcf_aineistovarasto" / "koosteet" / "kuukausi"
WIKI_HISTORIA_DIR = PROJECT_ROOT / "docs" / "HISTORIA" / "kuukausikoosteet"
MKDOCS_FILE = PROJECT_ROOT / "mkdocs.yml"


def sync():
    if not AINEISTOVARASTO_DIR.exists():
        print(f"Aineistovarastoa ei löytynyt polusta: {AINEISTOVARASTO_DIR}")
        return

    WIKI_HISTORIA_DIR.mkdir(parents=True, exist_ok=True)
    monthly_files = sorted(AINEISTOVARASTO_DIR.glob("*.md"))

    if not monthly_files:
        print("Ei kuukausikoosteita aineistovarastossa.")
        return

    synced_periods = []
    for file in monthly_files:
        period = file.stem  # esim. 2026-09
        if not re.match(r"^\d{4}-\d{2}$", period):
            continue

        target_file = WIKI_HISTORIA_DIR / f"{period}.md"
        content = file.read_text(encoding="utf-8")

        # Päivitetään tai injektoidaan wikille sopiva frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = parts[1]
                body = parts[2].strip()
                new_fm = (
                    f"\nwiki_category: HISTORIA\n"
                    f"publishability: public_candidate\n"
                    f"status: arkistoitu_wikiin\n"
                    f"{fm.strip()}\n"
                )
                final_content = f"---{new_fm}---\n\n{body}\n"
            else:
                final_content = content
        else:
            final_content = (
                f"---\nwiki_category: HISTORIA\npublishability: public_candidate\nstatus: arkistoitu_wikiin\n---\n\n{content}"
            )

        if not target_file.exists() or target_file.read_text(encoding="utf-8") != final_content:
            target_file.write_text(final_content, encoding="utf-8")
            print(f"Päivitetty kuukausikooste: {target_file.name}")
        synced_periods.append(period)

    print(f"Synkronoitu {len(synced_periods)} kuukausikoostetta.")


if __name__ == "__main__":
    sync()
