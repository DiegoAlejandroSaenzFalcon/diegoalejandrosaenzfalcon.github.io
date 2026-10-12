#!/usr/bin/env python3
"""Validate the portfolio's structural, navigation, and evidence-first invariants.

Uses only the Python standard library so CI remains lightweight and reproducible.
This is not a replacement for a full HTML conformance or browser accessibility audit.
"""
from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_SECTIONS = {
    "sobre-mi",
    "experiencia",
    "conocimientos",
    "formacion",
    "proyectos",
    "evidencia",
    "cv",
    "contacto",
}


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.json_ld: list[str] = []
        self._in_json_ld = False
        self._json_ld_parts: list[str] = []
        self._current_script_type = ""
        self.external_links_without_rel: list[str] = []
        self.phone_links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.append(element_id)

        href = values.get("href") or ""
        parsed = urlparse(href)
        if href.startswith("#") and len(href) > 1:
            self.fragments.append(href[1:])
        if parsed.scheme.lower() == "tel":
            self.phone_links.append(href)
        if parsed.scheme.lower() in {"http", "https"} and values.get("target") == "_blank":
            rel = set((values.get("rel") or "").lower().split())
            if "noopener" not in rel:
                self.external_links_without_rel.append(href)

        if tag.lower() == "script":
            self._current_script_type = (values.get("type") or "").lower()
            self._in_json_ld = self._current_script_type == "application/ld+json"
            self._json_ld_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._json_ld_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._in_json_ld:
            self.json_ld.append("".join(self._json_ld_parts))
            self._in_json_ld = False
            self._current_script_type = ""
            self._json_ld_parts = []


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)


def main() -> int:
    path = Path("index.html")
    if not path.is_file() or path.stat().st_size == 0:
        fail("index.html is missing or empty")
        return 1

    source = path.read_text(encoding="utf-8")
    lower = source.lower()
    if not lower.lstrip().startswith("<!doctype html>"):
        fail("HTML5 doctype must be the first markup")
        return 1
    if '<html lang="es"' not in lower and "<html lang='es'" not in lower:
        fail("root HTML element must declare lang=es")
        return 1

    parser = PortfolioParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:  # HTMLParser should be permissive, but fail closed.
        fail(f"HTML parser error: {exc}")
        return 1

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        fail("duplicate id attributes: " + ", ".join(duplicates))
    missing_sections = sorted(REQUIRED_SECTIONS - set(parser.ids))
    if missing_sections:
        fail("required sections missing: " + ", ".join(missing_sections))
    missing_fragments = sorted(set(parser.fragments) - set(parser.ids))
    if missing_fragments:
        fail("internal fragment targets missing: " + ", ".join(missing_fragments))
    if parser.external_links_without_rel:
        fail("external target=_blank links missing rel=noopener: " + ", ".join(parser.external_links_without_rel))
    if parser.phone_links:
        fail("public phone links are not allowed by the current privacy baseline")
    if "3 años consecutivos con medalla de cero incidentes viales" in source.lower():
        fail("unverified traffic-award claim must not be published")
    if "bachiller académico" not in source.lower():
        fail("completed bachiller education must be represented")

    if not parser.json_ld:
        fail("JSON-LD Person structured data is missing")
    else:
        for index, block in enumerate(parser.json_ld, start=1):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                fail(f"JSON-LD block {index} is invalid: {exc}")

    if parser.external_links_without_rel or parser.phone_links or duplicates or missing_sections or missing_fragments:
        return 1
    if not parser.json_ld or any("JSON-LD block" in line for line in []):
        return 1
    if "bachiller académico" not in source.lower() or "3 años consecutivos con medalla de cero incidentes viales" in source.lower():
        return 1

    print(
        "Portfolio validation OK: "
        f"{len(parser.ids)} ids, {len(set(parser.fragments))} internal fragments, "
        f"{len(parser.json_ld)} JSON-LD block(s), privacy and evidence invariants passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
