# DevOps & SRE Interview Questions

Real interview questions collected from people who actually sat through DevOps, SRE, and Cloud engineering interviews in 2025 and 2026. No paraphrasing, no "top 50 questions" filler — these are the exact questions candidates were asked, organized so you can look up a specific company or just browse broadly to prep.

> **Browse it as a website:** <https://litu54.github.io/DevOps-Interview-Guide/>
> — full-text search, a company directory, browse-by-topic, and dark mode. Built with MkDocs
> Material and published automatically from `main`.

## What's here

- **153 interview write-ups**
- **85 companies**, plus an `Others/` folder for interviews where the company wasn't named
- Topics span Kubernetes, Docker, Terraform, AWS/Azure/GCP, CI/CD (Jenkins, GitHub Actions, Azure DevOps), Ansible, Linux, scripting, and SRE fundamentals (SLI/SLO/SLA, observability, incident response)

Some companies show up more than once — different candidates, different rounds, sometimes years apart. Each of those is kept as a separate file rather than merged, since the questions and interviewer style often differ.

## How it's organized

```text
docs/
  <Company Name>/
    DevOps_Engineer.md      (default when no specific role was mentioned)
    DevOps_Engineer_2.md    (second interview for the same company)
    SRE_principal.md        (used when a role was explicitly called out)
    ...
  index.md                  (site landing page)
  tags.md                   (browse-by-tag index)
  stylesheets/extra.css     (site styling)
hooks/interview_pages.py    (build hook: company pages, nav, page summaries, live stats)
mkdocs.yml                  (site configuration)
```

Company overview pages, the A–Z company directory, and every count on the home page are generated
at build time from each file's frontmatter, so there's nothing to update by hand when you add an
interview.

Each file is one interview experience. If a company was interviewed at more than once, you'll find multiple files in its folder instead of one giant merged list. Roles are reflected in the filename when the original submission mentioned one; otherwise it defaults to `DevOps_Engineer`.

Submissions that never named a company live under `Others/`.

## Using this as an Obsidian vault

Every interview file carries YAML frontmatter, so the repo can be opened directly as an Obsidian vault (`Open folder as vault` → point it at the `docs/` directory). Tags are nested, which means Obsidian's tag pane groups them into a browsable tree:

```yaml
---
company: "Accion Labs"
role: "SRE"
interview: 2 # only present when it's the Nth interview for that role
experience: "5 years" # candidate's experience, if stated: "3.5 years", "3–5 years", "6+ years"
tags:
  - interview
  - company/accion-labs
  - role/sre
  - topic/kubernetes
  - topic/terraform
---
```

`topic/` tags are derived from what each file actually mentions. The vocabulary is fixed at 17 topics:

`kubernetes`, `docker`, `terraform`, `aws`, `azure`, `gcp`, `ci-cd`, `jenkins`, `ansible`, `linux`, `git`, `monitoring`, `sre`, `networking`, `security`, `scripting`, `databases`

Useful searches once the vault is open:

```text
tag:#topic/kubernetes tag:#topic/terraform    both topics in one interview
tag:#company/amazon                           everything from one company
tag:#role/sre -tag:#topic/aws                 SRE interviews that skip AWS
```

Files under `Others/` have `company: "Unknown"` and carry no `company/` tag, since those submissions never named the employer.

## Using this

Search the repo for a company name, or open its folder directly. If you're prepping broadly rather than for one company, skim a handful of folders across different company sizes (product companies, service companies like TCS/Infosys/Wipro, fintech, etc.) — the range of questions tells you more than any single list.

## Previewing the site locally

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>. `mkdocs build --strict` is what CI runs — it turns broken
internal links into build failures, so run it before opening a PR that moves or renames pages.

## Contributing

Have an interview experience worth sharing? Add it as a new file under the matching company folder in `docs/` (create the folder if it doesn't exist yet). Keep the one-file-per-interview format, and include the role and years of experience at the top if you can — it helps other candidates gauge relevance. If the company can't be named, put it under `docs/Others/`.

### Page format

Every page follows the same shape, so the site can render a consistent summary and table of contents:

```markdown
---
company: "Acme"
role: "DevOps Engineer"
experience: "5 years"
tags:
  - interview
  - company/acme
  - role/devops-engineer
  - topic/kubernetes
---

# Acme — DevOps Engineer

Optional one-line context: number of rounds, format, location.

## Round 1: Technical

1. Question exactly as it was asked
2. Next question
```

- **Frontmatter** — `company`, `role`, and `tags` are required; `experience` is optional. Follow the
  schema in [Using this as an Obsidian vault](#using-this-as-an-obsidian-vault), and pick `topic/`
  tags only from the fixed 17-topic vocabulary, for topics the interview actually covered.
- **Title** — `# <Company> — <Role>`, with `(Interview N)` appended when `interview: N` is set. Use
  `Undisclosed company` for files under `Others/`.
- **Sections** — `##` for rounds (or topics, if there were no distinct rounds), `###` for topics
  inside a round. Don't use bold text as a heading.
- **Questions** — one list item per question, worded exactly as asked. Typos and casual phrasing
  stay; that's the point of the repo.
- **Code** — fenced with a language tag, indented under the question it belongs to.

### Naming your file

Use `<Role>.md`, with underscores instead of spaces — `DevOps_Engineer.md`, `SRE_principal.md`, `Cloud_Administrator_senior.md`. If a file for that role already exists in the folder, append the next number rather than merging into the existing one: `DevOps_Engineer_2.md`. Separate files preserve who was asked what, which is the point of the repo.

### Formatting

Markdown formatting is checked automatically on every pull request. The check only looks at files your PR touches, so you are never blocked by pre-existing issues elsewhere in the repo.

Before pushing, run the auto-fixer from the repository root:

```bash
npx --yes markdownlint-cli2@0.23.2 --fix "**/*.md"
```

That resolves nearly everything — blank lines around lists, stray double blank lines, trailing whitespace, bare URLs. Rules that would rewrite list numbering are deliberately turned off in `.markdownlint-cli2.jsonc`, so the fixer will **not** renumber your questions.

One rule can't auto-fix: `MD040` wants a language tag on every code fence. Use ```` ```bash ```` for commands, ```` ```yaml ```` for manifests, or ```` ```text ```` for plain output and diagrams.

### Opening the PR

A [pull request template](.github/PULL_REQUEST_TEMPLATE.md) is filled in for you when you open a PR. It asks for the company, role, and interview date, and has a short checklist covering the things that actually matter here: questions recorded as asked, no personal details about the interviewer, and the file in the right place.

## Support this

This is maintained on personal time, and it only stays useful because people keep contributing their interview experiences. If it helped your prep, starring the repo is the simplest way to say thanks — it also makes the repo easier for the next person to find.
