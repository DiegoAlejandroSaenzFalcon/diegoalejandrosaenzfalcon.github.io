#!/usr/bin/env python3
"""Lightweight structural, navigation, metadata and privacy checks for GitHub Pages."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_SECTIONS = {
    "sobre-mi", "experiencia", "conocimientos", "formacion",
    "proyectos", "evidencia", "cv", "contacto",
}


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.json_ld: list[str] = []
        self.in_json_ld = False
        self.json_ld_parts: list[str] = []
        self.unsafe_external_links: list[str] = []
        self.phone_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        href = values.get("href") or ""
        parsed = urlparse(href)
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(href[1:])
        if parsed.scheme.lower() == "tel":
            self.phone_links.append(href)
        if parsed.scheme.lower() in {"http", "https"} and values.get("target") == "_blank":
            rel = set((values.get("rel") or "").lower().split())
            if "noopener" not in rel:
                self.unsafe_external_links.append(href)
        if tag.lower() == "script":
            self.in_json_ld = (values.get("type") or "").lower() == "application/ld+json"
            self.json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if self.in_json_ld:
            self.json_ld_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self.in_json_ld:
            self.json_ld.append("".join(self.json_ld_parts))
            self.in_json_ld = False
            self.json_ld_parts = []


def main() -> int:
    errors = 0

    def report(message: str) -> None:
        nonlocal errors
        print(f"FAIL: {message}", file=sys.stderr)
        errors += 1

    path = Path("index.html")
    if not path.is_file() or path.stat().st_size == 0:
        report("index.html is missing or empty")
        return 1

    source = path.read_text(encoding="utf-8")
    lower = source.lower()
    if not lower.lstrip().startswith("<!doctype html>"):
        report("HTML5 doctype must be the first markup")
    if '<html lang="es"' not in lower and "<html lang='es'" not in lower:
        report("root HTML element must declare lang=es")

    if '<meta name="viewport"' not in lower:
        report("responsive viewport metadata is missing")
    if '<meta name="description"' not in lower:
        report("search description metadata is missing")
    if '<link rel="canonical" href="https://diegoalejandrosaenzfalcon.github.io/">' not in lower:
        report("canonical URL must point to the official Pages domain")
    if len(re.findall(r"<h1\b", lower)) != 1:
        report("page must have exactly one primary h1 heading")
    if "prefers-reduced-motion" not in lower:
        report("reduced-motion accessibility preference is missing")

    parser = PortfolioParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:
        report(f"HTML parser error: {exc}")
        return 1

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        report("duplicate id attributes: " + ", ".join(duplicates))
    missing_sections = sorted(REQUIRED_SECTIONS - set(parser.ids))
    if missing_sections:
        report("required sections missing: " + ", ".join(missing_sections))
    missing_fragments = sorted(set(parser.fragments) - set(parser.ids))
    if missing_fragments:
        report("internal fragment targets missing: " + ", ".join(missing_fragments))
    if parser.unsafe_external_links:
        report("external target=_blank links missing rel=noopener: " + ", ".join(parser.unsafe_external_links))
    if parser.phone_links:
        report("public phone links are not allowed by the current privacy baseline")
    if "3 años consecutivos con medalla de cero incidentes viales" in lower:
        report("unverified traffic-award claim must not be published")
    if "bachiller académico" not in lower:
        report("completed bachiller education must be represented")

    if not parser.json_ld:
        report("JSON-LD structured data is missing")
    for index, block in enumerate(parser.json_ld, start=1):
        try:
            data = json.loads(block)
            if not isinstance(data, dict) or data.get("@type") != "Person":
                report(f"JSON-LD block {index} must describe a Person")
        except json.JSONDecodeError as exc:
            report(f"JSON-LD block {index} is invalid: {exc}")

    if errors:
        return 1

    print(
        "Portfolio validation OK: "
        f"{len(parser.ids)} ids, {len(set(parser.fragments))} internal fragments, "
        f"{len(parser.json_ld)} JSON-LD block(s); privacy and evidence checks passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
