import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "package_skill.py"


def load_packager():
    spec = importlib.util.spec_from_file_location("package_skill", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PackageSkillTest(unittest.TestCase):
    def test_builds_matching_clean_archives(self):
        packager = load_packager()

        with tempfile.TemporaryDirectory() as temp_dir:
            skill_file, zip_file = packager.package_skill(
                REPO_ROOT, Path(temp_dir)
            )

            self.assertEqual(skill_file.read_bytes(), zip_file.read_bytes())

            with zipfile.ZipFile(skill_file) as archive:
                members = set(archive.namelist())

            self.assertEqual(
                members,
                {
                    "weekend-reads/SKILL.md",
                    "weekend-reads/agents/openai.yaml",
                    "weekend-reads/references/outline-methodology.md",
                    "weekend-reads/references/quality-checklist.md",
                    "weekend-reads/references/research-method.md",
                    "weekend-reads/references/voice-and-style.md",
                },
            )

    def test_rejects_name_outside_yaml_frontmatter(self):
        packager = load_packager()

        with tempfile.TemporaryDirectory() as temp_dir:
            skill_root = Path(temp_dir) / "weekend-reads"
            skill_root.mkdir()
            (skill_root / "SKILL.md").write_text(
                "# Weekend Reads\n\nname: weekend-reads\n", encoding="utf-8"
            )

            with self.assertRaisesRegex(ValueError, "YAML frontmatter"):
                packager.read_skill_name(skill_root)


if __name__ == "__main__":
    unittest.main()
