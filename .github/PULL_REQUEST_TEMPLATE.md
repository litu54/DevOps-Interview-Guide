<!--
Thanks for contributing an interview experience.

Fill in the details below and tick the checklist. Delete any section that
doesn't apply (for example, if you're fixing a typo rather than adding a new
interview, just say so and skip the rest).
-->

## What's in this PR

<!-- One line: "Adds a DevOps Engineer interview at Acme from March 2026" -->

**Type of change:**

- [ ] New interview write-up
- [ ] Addition to an existing write-up (more questions from the same interview)
- [ ] Correction / typo fix
- [ ] Repo maintenance (tooling, docs, structure)

## Interview details

<!-- Skip this section for corrections and maintenance PRs. -->

| Field | Value |
| --- | --- |
| Company | |
| Role as advertised | |
| Round(s) covered | <!-- e.g. screening, L2 technical, hiring manager --> |
| Approximate date | <!-- e.g. March 2026 --> |
| Years of experience | <!-- the candidate's, if you're comfortable sharing --> |
| File added | <!-- e.g. docs/Acme/DevOps_Engineer.md --> |

## Checklist

### Content

- [ ] Questions are recorded **as they were actually asked**, not rephrased into polished textbook wording
- [ ] This is a real interview, not a compiled "top questions" list from elsewhere
- [ ] No confidential material — no take-home problem statements under NDA, no internal system names, no proprietary architecture details
- [ ] No personal information about the interviewer (name, contact details, LinkedIn)
- [ ] Nothing identifying about the candidate beyond role and years of experience

### Frontmatter

- [ ] File starts with YAML frontmatter containing `company`, `role`, and `tags` (plus `experience` if known, e.g. `"5 years"`)
- [ ] Title is `# <Company> — <Role>`, with `(Interview N)` appended when `interview: N` is set
- [ ] Rounds and topics are `##` / `###` headings, not bold text
- [ ] `company` matches the folder name, or is `"Unknown"` for entries under `Others/`
- [ ] `topic/` tags come from the fixed 17-topic vocabulary in the README — no invented topics
- [ ] Tags reflect what the interview actually covered, not every tool you know

### Placement

- [ ] File is in the correct company folder under `docs/`, or under `docs/Others/` if the company can't be named
- [ ] Folder name matches the existing convention (underscores for spaces, e.g. `Morgan_Stanley`)
- [ ] Filename follows `<Role>.md`, numbered if a file for that role already exists (`DevOps_Engineer_2.md`)
- [ ] An existing file was **not** overwritten or merged into — separate interviews stay in separate files

### Formatting

- [ ] Ran `npx --yes markdownlint-cli2@0.23.2 --fix "**/*.md"` from the repo root
- [ ] Every code fence has a language tag (```` ```bash ````, ```` ```yaml ````, ```` ```text ````)
- [ ] Question numbering is intact and sequential — check this by eye after running the fixer
- [ ] The `Markdown Lint & Format` check passes on this PR

## Anything else

<!--
Optional. Useful things to mention:
  - the interview format (live coding, whiteboard, scenario-based, panel)
  - roughly how long each round ran
  - whether the questions leaned practical or theoretical
  - anything that surprised you
-->
