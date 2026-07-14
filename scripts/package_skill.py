#!/usr/bin/env python3
"""Build clean Weekend Reads archives for skill upload surfaces."""

from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path


NAME_PATTERN = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)


def read_skill_name(skill_root: Path) -> str:
    skill_md = skill_root / "SKILL.md"
    if not skill_md.is_file():
        raise ValueError(f"Missing required file: {skill_md}")

    contents = skill_md.read_text(encoding="utf-8")
    frontmatter_parts = contents.split("---", 2)
    if len(frontmatter_parts) != 3 or frontmatter_parts[0].strip():
        raise ValueError("SKILL.md must begin with YAML frontmatter")

    match = NAME_PATTERN.search(frontmatter_parts[1])
    if not match:
        raise ValueError(
            "SKILL.md frontmatter must declare a lowercase, hyphenated name"
        )

    name = match.group(1)
    if skill_root.name != name:
        raise ValueError(
            f"Skill folder must be named {name!r}, not {skill_root.name!r}"
        )
    return name


def runtime_files(skill_root: Path) -> list[Path]:
    files = [skill_root / "SKILL.md", skill_root / "agents" / "openai.yaml"]
    files.extend(sorted((skill_root / "references").glob("*.md")))

    missing = [path for path in files if not path.is_file()]
    if missing:
        formatted = ", ".join(str(path) for path in missing)
        raise ValueError(f"Missing packaged file(s): {formatted}")
    return files


def package_skill(skill_root: Path, output_dir: Path) -> tuple[Path, Path]:
    skill_root = skill_root.resolve()
    output_dir = output_dir.resolve()
    name = read_skill_name(skill_root)
    files = runtime_files(skill_root)

    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{name}.zip"
    skill_path = output_dir / f"{name}.skill"

    with zipfile.ZipFile(
        zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in files:
            relative_path = path.relative_to(skill_root)
            archive.write(path, Path(name) / relative_path)

    shutil.copyfile(zip_path, skill_path)
    return skill_path, zip_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build ready-to-upload .skill and .zip archives."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("dist"),
        help="Output directory (default: dist)",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    skill_path, zip_path = package_skill(skill_root, args.output)
    print(f"Created {skill_path}")
    print(f"Created {zip_path}")


if __name__ == "__main__":
    main()
