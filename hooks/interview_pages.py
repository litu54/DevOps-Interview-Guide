"""MkDocs build hook for the interview site.

Everything here is derived from the frontmatter of docs/<Company>/<Role>.md at
build time, so counts and listings can never drift from the content:

- a generated overview page for every company folder, plus a Companies index
- a summary strip under each interview's title (company, role, experience,
  question count)
- live stats, topic cards and a company directory on the home page
- one "Companies" section in the nav instead of 86 top-level folders
"""

from __future__ import annotations

import html
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from types import SimpleNamespace

import yaml
from mkdocs.structure.files import File
from mkdocs.structure.nav import Section

# Folders whose name doesn't title-case into the company's real name.
DISPLAY_NAMES = {
    "L_and_T": "L&T",
    "Others": "Undisclosed companies",
}
OTHERS = "Others"

TOPIC_ICONS = {
    "kubernetes": "material-kubernetes",
    "docker": "material-docker",
    "terraform": "material-terraform",
    "aws": "material-aws",
    "azure": "material-microsoft-azure",
    "gcp": "material-google-cloud",
    "ci-cd": "material-pipe",
    "jenkins": "material-cog-sync-outline",
    "ansible": "material-ansible",
    "linux": "material-linux",
    "git": "material-git",
    "monitoring": "material-chart-line",
    "sre": "material-lifebuoy",
    "networking": "material-lan",
    "security": "material-shield-lock-outline",
    "scripting": "material-console",
    "databases": "material-database-outline",
}
TOPIC_LABELS = {"aws": "AWS", "gcp": "GCP", "ci-cd": "CI/CD", "sre": "SRE"}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE = re.compile(r"^\s*(```|~~~)")
LIST_ITEM = re.compile(r"^\s{0,3}(?:\d+\.|[-*+])\s+\S")
H1 = re.compile(r"^# .*$", re.M)


@dataclass
class Interview:
    src: str
    folder: str
    title: str
    role: str
    experience: str | None
    topics: list[str]
    questions: int


@dataclass
class Company:
    folder: str
    interviews: list[Interview] = field(default_factory=list)

    @property
    def name(self) -> str:
        return company_name(self.folder)


_companies: dict[str, Company] = {}


def natural_key(src: str) -> list:
    # DevOps_Engineer_2 before DevOps_Engineer_10.
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", src)]


def company_name(folder: str) -> str:
    return DISPLAY_NAMES.get(folder, folder.replace("_", " "))


def topic_label(topic: str) -> str:
    return TOPIC_LABELS.get(topic, topic.capitalize())


def count_questions(body: str) -> int:
    count, in_fence = 0, False
    for line in body.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and LIST_ITEM.match(line):
            count += 1
    return count


def parse(path: str, src: str) -> Interview | None:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    match = FRONTMATTER.match(text)
    if not match:
        return None
    meta = yaml.safe_load(match.group(1)) or {}
    if "company" not in meta:
        return None
    body = text[match.end():]
    h1 = H1.search(body)
    return Interview(
        src=src,
        folder=src.split("/")[0],
        title=h1.group(0)[2:].strip() if h1 else src,
        role=meta.get("role", ""),
        experience=meta.get("experience"),
        topics=[t.split("/", 1)[1] for t in meta.get("tags", []) if t.startswith("topic/")],
        questions=count_questions(body),
    )


def sorted_companies() -> list[Company]:
    # Named companies A–Z, the undisclosed bucket last.
    return sorted(_companies.values(), key=lambda c: (c.folder == OTHERS, c.name.lower()))


def interview_card(iv: Interview, link: str) -> str:
    # The card title already names the role.
    details = []
    if iv.experience:
        details.append(f":material-briefcase-clock-outline: {iv.experience}")
    details.append(f":material-format-list-numbered: {iv.questions} questions")
    topics = " ".join(f"`{topic_label(t)}`" for t in iv.topics)
    return (
        f"-   **[{iv.title.split(' — ', 1)[-1]}]({link})**\n\n"
        f"    ---\n\n"
        f"    {' · '.join(details)}\n\n"
        + (f"    {topics}\n" if topics else "")
    )


def company_page(company: Company) -> str:
    total = sum(iv.questions for iv in company.interviews)
    plural = "s" if len(company.interviews) != 1 else ""
    lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        f"# {company.name}",
        "",
        f"{len(company.interviews)} interview{plural} · {total} questions",
        "",
    ]
    if company.folder == OTHERS:
        lines += [
            "Submissions where the candidate didn't name the employer. Each page is still a single,",
            "real interview — they're just not attributable to a company.",
            "",
        ]
    lines.append('<div class="grid cards" markdown>\n')
    for iv in company.interviews:
        lines.append(interview_card(iv, os.path.basename(iv.src)))
    lines.append("</div>\n")
    return "\n".join(lines)


def companies_index() -> str:
    groups: dict[str, list[Company]] = defaultdict(list)
    for company in sorted_companies():
        key = "#" if company.folder == OTHERS else company.name[0].upper()
        groups[key].append(company)

    lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        "# Companies",
        "",
        f"{len(_companies) - (OTHERS in _companies)} named companies, plus undisclosed submissions.",
        "Pick a company to see every interview recorded for it.",
        "",
        '<div class="company-index" markdown>',
        "",
    ]
    for letter, companies in groups.items():
        heading = "Undisclosed" if letter == "#" else letter
        lines += [f"## {heading}", ""]
        for company in companies:
            n = len(company.interviews)
            lines.append(
                f"- [{company.name}](../{company.folder}/index.md) "
                f'<span class="count">{n}</span>'
            )
        lines.append("")
    lines.append("</div>")
    return "\n".join(lines)


def home_stats() -> dict[str, str]:
    interviews = [iv for c in _companies.values() for iv in c.interviews]
    topics = Counter(t for iv in interviews for t in iv.topics)
    roles = {iv.role for iv in interviews}

    stats = (
        '<div class="grid cards stats" markdown>\n\n'
        f"-   :material-file-document-multiple-outline:{{ .lg }} **{len(interviews)}** interviews\n"
        f"-   :material-comment-question-outline:{{ .lg }} **{sum(iv.questions for iv in interviews):,}** questions\n"
        f"-   :material-office-building-outline:{{ .lg }} **{len(_companies) - (OTHERS in _companies)}** companies\n"
        f"-   :material-account-tie-outline:{{ .lg }} **{len(roles)}** roles\n\n"
        "</div>"
    )
    cards = ['<div class="grid cards topics" markdown>\n']
    for topic, n in topics.most_common():
        icon = TOPIC_ICONS.get(topic, "material-tag-outline")
        cards.append(
            f"-   [:{icon}: **{topic_label(topic)}** <span class=\"count\">{n}</span>]"
            f"(tags.md#tag:topic/{topic})"
        )
    cards.append("\n</div>")
    return {"<!-- stats -->": stats, "<!-- topics -->": "\n".join(cards)}


# ---------------------------------------------------------------------------
# MkDocs events
# ---------------------------------------------------------------------------


def on_files(files, config):
    _companies.clear()
    for file in list(files.documentation_pages()):
        src = file.src_uri
        if src.count("/") != 1 or src.endswith("/index.md"):
            continue
        iv = parse(file.abs_src_path, src)
        if iv:
            _companies.setdefault(iv.folder, Company(iv.folder)).interviews.append(iv)

    for company in _companies.values():
        company.interviews.sort(key=lambda iv: natural_key(iv.src))
        files.append(File.generated(config, f"{company.folder}/index.md", content=company_page(company)))
    files.append(File.generated(config, "companies/index.md", content=companies_index()))
    return files


def short_nav_titles(section: Section, company: Company) -> None:
    """Drop the company prefix from sidebar entries; the section already names it.

    Material's nav renders ``nav_item.typeset.title`` in preference to the page
    title when it's set, so this changes only the sidebar, not the page heading,
    browser title, search results or tag listings.
    """
    titles = {iv.src: iv.title.split(" — ", 1)[-1] for iv in company.interviews}
    # Overview page first (navigation.indexes needs it there), then interviews in natural order.
    section.children.sort(key=lambda p: (not p.file.src_uri.endswith("/index.md"), natural_key(p.file.src_uri)))
    for page in section.children:
        title = titles.get(page.file.src_uri)
        if title:
            page.typeset = SimpleNamespace(title=html.escape(title))


def on_nav(nav, config, files):
    def folder_of(section: Section) -> str:
        return section.children[0].file.src_uri.split("/")[0]

    pages = [item for item in nav.items if not isinstance(item, Section)]
    sections = {folder_of(s): s for s in nav.items if isinstance(s, Section)}

    # Reuse the auto-generated "companies/" section and hang every company under it.
    # Its index.md stays first, which is what navigation.indexes keys off.
    companies = sections.pop("companies")
    companies.title = "Companies"
    for company in sorted_companies():
        section = sections.get(company.folder)
        if section:
            section.title = company.name
            section.parent = companies
            companies.children.append(section)
            short_nav_titles(section, company)

    home = [p for p in pages if p.file.src_uri == "index.md"]
    rest = [p for p in pages if p.file.src_uri != "index.md"]
    nav.items = home + [companies] + rest
    return nav


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if src == "index.md":
        for marker, html in home_stats().items():
            markdown = markdown.replace(marker, html)
        return markdown

    folder = src.split("/")[0]
    company = _companies.get(folder)
    iv = next((i for i in company.interviews if i.src == src), None) if company else None
    if iv is None:
        return markdown

    chips = [f"- :material-office-building-outline: [{company.name}](index.md)"]
    chips.append(f"- :material-account-tie-outline: {iv.role}")
    if iv.experience:
        chips.append(f"- :material-briefcase-clock-outline: {iv.experience} experience")
    chips.append(f"- :material-format-list-numbered: {iv.questions} questions")
    strip = '\n\n<div class="iv-meta" markdown>\n\n' + "\n".join(chips) + "\n\n</div>\n"
    return H1.sub(lambda m: m.group(0) + strip, markdown, count=1)
