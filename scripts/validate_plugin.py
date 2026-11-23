#!/usr/bin/env python3
"""Check the shared Claude/Codex package, without exercising model behavior."""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml


SKILLS = {
    "setup", "dimensions", "screen", "jd", "cv", "cover-letter",
    "add-to-encyclopedia",
}
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SEMVER = re.compile(
    r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
CONFLICT = re.compile(r"^(?:<{7}|>{7})(?:\s|$)", re.MULTILINE)


class ValidationError(ValueError):
    """A package invariant failed."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def text(path):
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValidationError(f"Cannot read {path}: {error}") from error
    require(not CONFLICT.search(content), f"Unresolved merge conflict in {path}")
    return content


def mapping(value, label):
    require(isinstance(value, dict), f"{label} must be an object")
    return value


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()),
            f"{label} must be a non-empty string")
    return value


def json_object(path):
    try:
        return mapping(json.loads(text(path)), str(path))
    except json.JSONDecodeError as error:
        raise ValidationError(f"Invalid JSON in {path}: {error}") from error


def yaml_object(content, label):
    try:
        return mapping(yaml.safe_load(content), label)
    except yaml.YAMLError as error:
        raise ValidationError(f"Invalid YAML in {label}: {error}") from error


def package_path(root, value, label, directory=False):
    value = string(value, label)
    require(value.startswith("./") and "\\" not in value,
            f"{label} must be a ./ path relative to its package")
    require(".." not in value.split("/"), f"{label} must not contain parent traversal (..)")
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), f"{label} escapes its package")
    exists = path.is_dir() if directory else path.is_file()
    require(exists, f"{label} references a missing {'directory' if directory else 'file'}: {value}")
    return path


def validate_skill(path, expected_name):
    lines = text(path).splitlines()
    require(lines and lines[0] == "---", f"{path} must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValidationError(f"Unclosed YAML frontmatter in {path}") from error
    frontmatter = yaml_object("\n".join(lines[1:end]), str(path))
    require(frontmatter.get("name") == expected_name,
            f"{path} name must match {expected_name!r}")
    require(NAME.fullmatch(expected_name) and len(expected_name) <= 64,
            f"Invalid skill name: {expected_name}")
    description = string(frontmatter.get("description"), f"{path} description")
    require(len(description) <= 1024, f"{path} description exceeds 1024 characters")
    require(bool("\n".join(lines[end + 1:]).strip()), f"{path} has no instructions")


def validate_metadata(skill_dir, plugin_name):
    path = package_path(skill_dir, "./agents/openai.yaml", f"{skill_dir.name} Codex metadata")
    metadata = yaml_object(text(path), str(path))
    interface = mapping(metadata.get("interface"), f"{path} interface")
    string(interface.get("display_name"), f"{path} display_name")
    description = string(interface.get("short_description"), f"{path} short_description")
    require(25 <= len(description) <= 64,
            f"{path} short_description must contain 25–64 characters")
    prompt = string(interface.get("default_prompt"), f"{path} default_prompt")
    invocation = r"\$(?:" + re.escape(plugin_name) + r":)?" + re.escape(skill_dir.name)
    require(re.search(invocation + r"(?![a-z0-9-])", prompt),
            f"{path} default_prompt must invoke ${skill_dir.name} or ${plugin_name}:{skill_dir.name}")
    for key in ("icon_small", "icon_large"):
        if key in interface:
            package_path(skill_dir, interface[key], f"{path} {key}")
    if "policy" in metadata:
        policy = mapping(metadata["policy"], f"{path} policy")
        if "allow_implicit_invocation" in policy:
            require(isinstance(policy["allow_implicit_invocation"], bool),
                    f"{path} allow_implicit_invocation must be a boolean")


def validate_plugin(root):
    root = Path(root).resolve()
    codex = json_object(root / ".codex-plugin/plugin.json")
    claude = json_object(root / ".claude-plugin/plugin.json")
    for label, manifest in (("Codex", codex), ("Claude", claude)):
        name = string(manifest.get("name"), f"{label} name")
        require(NAME.fullmatch(name) and len(name) <= 64, f"Invalid {label} name: {name}")
        version = string(manifest.get("version"), f"{label} version")
        require(SEMVER.fullmatch(version), f"{label} version must be valid SemVer: {version}")
        string(manifest.get("description"), f"{label} description")
        author = mapping(manifest.get("author"), f"{label} author")
        string(author.get("name"), f"{label} author.name")
    require(codex["name"] == claude["name"], "Claude and Codex plugin names differ")
    require(codex["version"] == claude["version"], "Claude and Codex plugin versions differ")

    skills_dir = package_path(root, codex.get("skills"), "Codex skills", directory=True)
    require(skills_dir == root / "skills", "Codex must expose the shared skills directory")
    discovered = {path.name for path in skills_dir.iterdir() if path.is_dir()}
    require(discovered == SKILLS,
            f"Skill inventory differs: missing={sorted(SKILLS - discovered)}, "
            f"unexpected={sorted(discovered - SKILLS)}")
    validate_skill(package_path(root, "./SKILL.md", "Root overview skill"), codex["name"])
    for name in sorted(SKILLS):
        skill_dir = package_path(root, f"./skills/{name}", f"{name} skill", directory=True)
        skill_file = package_path(skill_dir, "./SKILL.md", f"{name} skill instructions")
        validate_skill(skill_file, name)
        validate_metadata(skill_dir, codex["name"])

    claude_skills = claude.get("skills")
    require(isinstance(claude_skills, list) and bool(claude_skills),
            "Claude skills must be a non-empty list")
    for entry in claude_skills:
        package_path(root, entry, "Claude skills", directory=True)
    require("./" in claude_skills, "Claude must retain its root overview skill")

    interface = mapping(codex.get("interface"), "Codex interface")
    for key in ("displayName", "shortDescription", "developerName"):
        string(interface.get(key), f"Codex interface.{key}")
    for key in ("composerIcon", "logo", "logoDark"):
        if key in interface:
            package_path(root, interface[key], f"Codex interface.{key}")
    screenshots = interface.get("screenshots", [])
    require(isinstance(screenshots, list), "Codex screenshots must be a list")
    for entry in screenshots:
        package_path(root, entry, "Codex screenshot")
    for key in ("apps", "mcpServers"):
        if key in codex:
            if key == "mcpServers" and isinstance(codex[key], dict):
                continue
            component = package_path(root, codex[key], f"Codex {key}")
            json_object(component)

    marketplace = json_object(root / ".claude-plugin/marketplace.json")
    plugins = marketplace.get("plugins")
    require(isinstance(plugins, list), "Claude marketplace plugins must be a list")
    require(all(isinstance(entry, dict) for entry in plugins),
            "Claude marketplace plugin entries must be objects")
    entries = [entry for entry in plugins if entry.get("name") == claude["name"]]
    require(len(entries) == 1, "Claude marketplace must contain one matching plugin entry")
    source = package_path(root, entries[0].get("source"), "Claude marketplace source", directory=True)
    require(source == root, "Claude marketplace source must refer to this plugin root")
    package_path(root, "./scraper/linkedin_jd_scraper.py", "Screen scraper")

    # Check shipped text, without traversing personal workspaces or virtual environments.
    for pattern in ("*.md", "skills/**/*.md", "skills/**/*.yaml", "scraper/*.py",
                    "scripts/*.py", ".github/workflows/*.yml"):
        for path in root.glob(pattern):
            text(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1], help="Plugin directory")
    args = parser.parse_args()
    try:
        validate_plugin(args.root)
    except ValidationError as error:
        print(f"Plugin validation failed: {error}", file=sys.stderr)
        return 1
    print(f"Plugin validation passed: Claude and Codex manifests, {len(SKILLS)} shared skills, and Codex metadata")
    return 0


if __name__ == "__main__":
    sys.exit(main())
