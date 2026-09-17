#!/usr/bin/env python3
"""Validate the public Agent Skills PT-BR package with the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,63}$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PRIVATE_PATTERNS = {
    "nome interno de agência A": re.compile(r"contentdoc", re.IGNORECASE),
    "nome interno de agência B": re.compile(r"\bethos\b", re.IGNORECASE),
    "perfil local do autor": re.compile(r"maaur", re.IGNORECASE),
    "caminho local do Windows": re.compile(r"[A-Z]:\\", re.IGNORECASE),
    "referência a cofre local": re.compile(r"cofre\.env|\[\[cofre:", re.IGNORECASE),
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("frontmatter ausente")
    marker = text.find("\n---\n", 4)
    if marker == -1:
        raise ValueError("frontmatter não terminado")
    raw = text[4:marker]
    body = text[marker + 5 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, body


def local_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for target in LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        relative = target.split("#", 1)[0]
        if relative and not (path.parent / relative).resolve().exists():
            errors.append(f"link local quebrado: {target}")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append("name inválido")
    if name != path.parent.name:
        errors.append(f"name '{name}' difere da pasta '{path.parent.name}'")
    if not description:
        errors.append("description ausente")
    if len(description) > 500:
        errors.append("description excede 500 caracteres")
    if len(body.strip()) < 200:
        errors.append("corpo curto demais para orientar o agente")

    placeholder_patterns = {
        "TODO": re.compile(r"\bTODO\b"),
        "FIXME": re.compile(r"\bFIXME\b"),
        "<skill-name>": re.compile(r"<skill-name>", re.IGNORECASE),
        "placeholder": re.compile(r"\bplaceholder\b", re.IGNORECASE),
    }
    for label, pattern in placeholder_patterns.items():
        if pattern.search(text):
            errors.append(f"placeholder encontrado: {label}")

    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"referência privada encontrada: {label}")

    errors.extend(local_links(path, text))
    return errors


def validate_public_docs() -> list[tuple[Path, str]]:
    errors: list[tuple[Path, str]] = []
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for label, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(text):
                errors.append((path, f"referência privada encontrada: {label}"))
        if "\N{EM DASH}" in text:
            errors.append((path, "travessão encontrado"))
        for error in local_links(path, text):
            errors.append((path, error))
    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERRO: pasta skills não encontrada")
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("ERRO: nenhuma skill encontrada")
        return 1

    failed = False
    documentation_errors = validate_public_docs()
    for path, error in documentation_errors:
        failed = True
        print(f"FALHOU {path.relative_to(ROOT)}")
        print(f"  - {error}")

    for skill_file in skill_files:
        errors = validate_skill(skill_file)
        if errors:
            failed = True
            print(f"FALHOU {skill_file.parent.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {skill_file.parent.name}")

    if failed:
        return 1
    print(f"Pacote válido: {len(skill_files)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
