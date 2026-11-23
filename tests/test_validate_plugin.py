"""Package failure cases; these tests do not evaluate the skills' prose or behavior."""

import json
import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_plugin import SKILLS, ValidationError, validate_plugin


class PluginValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        common = {
            "name": "ai-career-coach", "version": "1.0.0",
            "description": "Test career plugin", "author": {"name": "Test author"},
        }
        self.codex = {
            **common, "skills": "./skills/",
            "interface": {"displayName": "Career Coach", "shortDescription": "Career support",
                          "developerName": "Test author"},
        }
        self.write_json(".codex-plugin/plugin.json", self.codex)
        self.write_json(".claude-plugin/plugin.json", {**common, "skills": ["./"]})
        self.write_json(".claude-plugin/marketplace.json", {
            "name": "career-marketplace", "plugins": [{"name": common["name"], "source": "./"}],
        })
        self.write("SKILL.md", self.skill(common["name"]))
        self.write("scraper/linkedin_jd_scraper.py", "# Test scraper fixture\n")
        for name in SKILLS:
            self.write(f"skills/{name}/SKILL.md", self.skill(name))
            self.write(f"skills/{name}/agents/openai.yaml", yaml.safe_dump({
                "interface": {"display_name": name,
                              "short_description": "A description for the test skill",
                              "default_prompt": f"Use ${name} to help me."},
            }))

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_json(self, relative, value):
        self.write(relative, json.dumps(value))

    @staticmethod
    def skill(name):
        return f"---\nname: {name}\ndescription: A test skill.\n---\nDo the requested work.\n"

    def test_complete_package_passes(self):
        validate_plugin(self.root)

    def test_missing_skill_instructions_fail(self):
        (self.root / "skills/screen/SKILL.md").unlink()
        with self.assertRaisesRegex(ValidationError, "screen skill instructions.*missing file"):
            validate_plugin(self.root)

    def test_missing_codex_metadata_fails(self):
        (self.root / "skills/screen/agents/openai.yaml").unlink()
        with self.assertRaisesRegex(ValidationError, "screen Codex metadata.*missing file"):
            validate_plugin(self.root)

    def test_qualified_plugin_invocations_pass(self):
        for name in SKILLS:
            relative = f"skills/{name}/agents/openai.yaml"
            metadata = yaml.safe_load((self.root / relative).read_text(encoding="utf-8"))
            metadata["interface"]["default_prompt"] = f"Use $ai-career-coach:{name} to help me."
            self.write(relative, yaml.safe_dump(metadata))
        validate_plugin(self.root)

    def test_wrong_plugin_namespace_fails(self):
        relative = "skills/setup/agents/openai.yaml"
        metadata = yaml.safe_load((self.root / relative).read_text(encoding="utf-8"))
        metadata["interface"]["default_prompt"] = "Use $another-plugin:setup to help me."
        self.write(relative, yaml.safe_dump(metadata))
        with self.assertRaisesRegex(ValidationError, "default_prompt must invoke"):
            validate_plugin(self.root)

    def test_malformed_frontmatter_fails(self):
        self.write("skills/jd/SKILL.md", "---\nname: jd\ndescription: [unclosed\n---\nInstructions.\n")
        with self.assertRaisesRegex(ValidationError, "Invalid YAML"):
            validate_plugin(self.root)

    def test_missing_asset_fails(self):
        self.codex["interface"]["logo"] = "./assets/missing.png"
        self.write_json(".codex-plugin/plugin.json", self.codex)
        with self.assertRaisesRegex(ValidationError, "missing file"):
            validate_plugin(self.root)

    def test_paths_cannot_escape_package(self):
        for relative in ("./../outside", "/tmp", "C:\\outside"):
            with self.subTest(path=relative):
                self.codex["skills"] = relative
                self.write_json(".codex-plugin/plugin.json", self.codex)
                with self.assertRaisesRegex(ValidationError, "escapes|relative|parent traversal"):
                    validate_plugin(self.root)

    def test_parent_traversal_within_package_is_forbidden(self):
        self.codex["skills"] = "./skills/../skills"
        self.write_json(".codex-plugin/plugin.json", self.codex)
        with self.assertRaisesRegex(ValidationError, "parent traversal"):
            validate_plugin(self.root)

    def test_asset_symlink_cannot_escape_package(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "logo.png"
            target.write_bytes(b"fixture")
            (self.root / "logo.png").symlink_to(target)
            self.codex["interface"]["logo"] = "./logo.png"
            self.write_json(".codex-plugin/plugin.json", self.codex)
            with self.assertRaisesRegex(ValidationError, "escapes"):
                validate_plugin(self.root)

    def test_versions_must_match(self):
        self.codex["version"] = "2.0.0"
        self.write_json(".codex-plugin/plugin.json", self.codex)
        with self.assertRaisesRegex(ValidationError, "versions differ"):
            validate_plugin(self.root)

    def test_each_manifest_requires_semver(self):
        for client in ("codex", "claude"):
            relative = f".{client}-plugin/plugin.json"
            manifest = json.loads((self.root / relative).read_text(encoding="utf-8"))
            for version in ("1.0", "01.2.3", "v1.2.3", "1.2.3-01", "1.2.3+"):
                with self.subTest(client=client, version=version):
                    manifest["version"] = version
                    self.write_json(relative, manifest)
                    with self.assertRaisesRegex(ValidationError, f"{client.capitalize()} version must be valid SemVer"):
                        validate_plugin(self.root)
            manifest["version"] = "1.0.0"
            self.write_json(relative, manifest)

    def test_semver_prerelease_and_build_metadata_pass(self):
        for client in ("codex", "claude"):
            relative = f".{client}-plugin/plugin.json"
            manifest = json.loads((self.root / relative).read_text(encoding="utf-8"))
            manifest["version"] = "1.2.3-rc.1+build.04"
            self.write_json(relative, manifest)
        validate_plugin(self.root)

    def test_conflict_markers_fail(self):
        self.write("README.md", "<<<<<<< HEAD\nUnresolved change\n=======\nOther change\n>>>>>>> branch\n")
        with self.assertRaisesRegex(ValidationError, "Unresolved merge conflict"):
            validate_plugin(self.root)

    def test_marketplace_cannot_point_to_another_directory(self):
        self.write_json(".claude-plugin/marketplace.json", {
            "plugins": [{"name": "ai-career-coach", "source": "./skills"}],
        })
        with self.assertRaisesRegex(ValidationError, "source must refer to this plugin root"):
            validate_plugin(self.root)


if __name__ == "__main__":
    unittest.main()
