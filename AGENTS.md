# Repository Guidelines

This repository is the published RCF-wiki: a MkDocs (Material theme) static
site built from plain Markdown. It is the human- and AI-readable home for
Ride Club Finland's permanent institutional knowledge — content that is too
heavy to keep buried in Discord scrollback.

## Project Structure & Module Organization

- `docs/` is the only source of truth for site content. Everything under it
  is published as-is; there is no separate "raw" vs "rendered" content.
  - `docs/YLLAPITO/` — admin/maintenance: Discord operating model, resource
    inventory, roles & responsibilities.
  - `docs/TAPAHTUMAT/` — event and competition playbooks/process docs.
  - `docs/JASENPOLKU/` — member-facing FAQ/onboarding.
  - `docs/ORGANIZER_CHECKLISTS/` — step-by-step organizer checklists and
    announcement templates (`templates/`).
  - `docs/meta/` — process/background docs about the wiki itself (e.g.
    `wiki_decision.md`), not RCF operational content.
  - `docs/index.md` is the site homepage and the canonical table of contents.
- `mkdocs.yml` defines the theme, navigation (`nav:`) and Markdown
  extensions. **The `nav:` list is hand-maintained** — MkDocs does not
  auto-discover pages, so a new file is invisible in the sidebar until it is
  added there.
- `requirements.txt` pins `mkdocs` + `mkdocs-material`. `.venv/` is the local
  virtualenv (gitignored, not portable — recreate it, don't copy it).
- `site/` is generated build output (gitignored). Never hand-edit it.
- Upstream source: the original Discord-mining pipeline that produced this
  content lives in the sibling `RCF_DISCORD_EXPORT` project
  (`content/wiki/` + `content/wiki_decision.md`). This repo is the
  destination, not the pipeline — don't recreate mining/synthesis logic here.

## Build, Test, and Development Commands

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\mkdocs serve            # local preview at http://127.0.0.1:8000
.venv\Scripts\mkdocs build --strict   # fails on broken internal links / nav errors — run before every deploy
.venv\Scripts\mkdocs gh-deploy --force  # builds and publishes to the gh-pages branch
```

There is no CI/CD pipeline wired up yet — publishing is a manual
`gh-deploy` run by whoever edits content. If you add or change pages, you
are responsible for running `build --strict` (verification) and, if asked,
`gh-deploy` (publishing) yourself.

## Content Guidelines (what belongs in this wiki)

Apply the same test used to build the initial set (full reasoning in
`docs/meta/wiki_decision.md`):

**Belongs in the wiki** if the information is permanent (doesn't change
week to week), useful to someone who wasn't there when it was decided, and
doesn't require constant upkeep to stay true.

**Stays in Discord instead** if it's live/in-progress discussion, a TODO
list, this-project's-own process bookkeeping, or anything containing
personal data, credentials, or access-control specifics.

When adding a page:
1. Put it in the right category folder (or propose a new one if none fits).
2. Give it YAML frontmatter matching the existing schema:
   ```yaml
   ---
   gold_id: short_snake_case_id       # unique, stable identifier
   wiki_category: TAPAHTUMAT          # matches the folder
   related_gold_docs: [other_gold_id] # cross-links by gold_id, not by path
   publishability: internal_only      # or public_candidate — see below
   status: koostettu_wikiin
   last_verified: YYYY-MM-DD          # bump this whenever you confirm/edit the content
   ---
   ```
3. Add the page to `mkdocs.yml`'s `nav:` and to `docs/index.md`'s table of
   contents — both, or it's unreachable/undiscoverable.
4. Use relative Markdown links (`../OTHER_CATEGORY/file.md`) between pages,
   not absolute URLs — `mkdocs build --strict` verifies these resolve.

`publishability: internal_only` is the default — it means club-internal
admin/organizer content. Only mark `public_candidate` when the content is
genuinely safe for an outside member to read verbatim (check for stale
links, membership fees, or other facts that drift over time before
promoting it). Note the whole repo is a **public** GitHub repo already —
`internal_only` is an editorial label for who the content is *written for*,
not an access-control boundary. Never rely on it to gate anything actually
sensitive.

## Coding Style & Naming Conventions

Markdown files: `snake_case.md`, UTF-8, Finnish prose (matches existing
content — don't switch languages mid-wiki). Preserve existing domain
terminology (Kruunajaiset, ZRS, WTRL TTT, etc.) rather than inventing new
names for the same concepts. Keep frontmatter keys and folder names exactly
as documented above — a new key ad hoc breaks the schema every other doc
follows.

## Testing Guidelines

No automated test suite. The load-bearing check is
`mkdocs build --strict`, which fails the build on broken internal links,
missing nav entries pointing at nonexistent files, or theme/config errors.
Run it after every content change, before every `gh-deploy`.

## Commit & Pull Request Guidelines

Use concise imperative commit messages (e.g. `Add TalviCup 2026-27 section
to competition process doc`). Mention which category/page changed. No
established PR template yet — describe what changed and why, and note if
`gh-deploy` still needs to be run after merge (it is not automatic).

## Security & Configuration Tips

This repo (`ride-club-finland/rcf-wiki`) and its published site
(`https://ride-club-finland.github.io/rcf-wiki/`) are **public**. Never
commit secrets, tokens, real member personal data, or anything redacted out
of the original Discord export for privacy reasons. When in doubt about
whether something is safe to publish, treat `docs/meta/wiki_decision.md`'s
criteria as the bar, not your own judgment call — and ask the repo owner if
a new case doesn't clearly fit either bucket.
