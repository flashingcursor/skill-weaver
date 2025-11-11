#!/usr/bin/env python3
"""
Validate Custom Skill structure and content.

This script validates that a Custom Skill follows the required structure
and best practices for Claude Custom Skills.
"""

import sys
import yaml
import re
from pathlib import Path


class SkillValidator:
    """Validates Custom Skill structure and content."""

    def __init__(self, skill_path):
        self.skill_path = Path(skill_path)
        self.errors = []
        self.warnings = []
        self.skill_md_path = self.skill_path / "Skill.md"

    def validate(self):
        """Run all validation checks."""
        print(f"Validating skill at: {self.skill_path}")
        print("=" * 60)

        self.check_directory_exists()
        self.check_skill_md_exists()
        self.validate_frontmatter()
        self.check_recommended_files()
        self.validate_file_references()

        self.print_results()
        return len(self.errors) == 0

    def check_directory_exists(self):
        """Check that the skill directory exists."""
        if not self.skill_path.exists():
            self.errors.append(f"Skill directory not found: {self.skill_path}")
            return False
        if not self.skill_path.is_dir():
            self.errors.append(f"Path is not a directory: {self.skill_path}")
            return False
        print("✓ Skill directory exists")
        return True

    def check_skill_md_exists(self):
        """Check that Skill.md exists."""
        if not self.skill_md_path.exists():
            self.errors.append("Required file 'Skill.md' not found")
            return False
        print("✓ Skill.md exists")
        return True

    def validate_frontmatter(self):
        """Validate YAML frontmatter in Skill.md."""
        if not self.skill_md_path.exists():
            return False

        try:
            content = self.skill_md_path.read_text()

            # Check for frontmatter delimiters
            if not content.startswith('---'):
                self.errors.append("Skill.md must start with YAML frontmatter (---)")
                return False

            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.errors.append("Invalid YAML frontmatter format")
                return False

            frontmatter_text = parts[1].strip()
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
            except yaml.YAMLError as e:
                self.errors.append(f"Invalid YAML in frontmatter: {e}")
                return False

            # Validate required fields
            if 'name' not in frontmatter:
                self.errors.append("Missing required field 'name' in frontmatter")
            else:
                name = frontmatter['name']
                if not isinstance(name, str) or not name.strip():
                    self.errors.append("Field 'name' must be a non-empty string")
                elif len(name) > 64:
                    self.errors.append(f"Field 'name' exceeds 64 characters (found {len(name)})")
                elif not re.match(r'^[a-z0-9-]+$', name):
                    self.errors.append(f"Field 'name' must use lowercase letters, numbers, and hyphens only (found: '{name}')")
                elif 'anthropic' in name.lower() or 'claude' in name.lower():
                    self.errors.append(f"Field 'name' cannot contain reserved words 'anthropic' or 'claude' (found: '{name}')")
                else:
                    print(f"✓ Skill name: '{name}'")

            if 'description' not in frontmatter:
                self.errors.append("Missing required field 'description' in frontmatter")
            else:
                description = frontmatter['description']
                if not isinstance(description, str) or not description.strip():
                    self.errors.append("Field 'description' must be a non-empty string")
                elif len(description) > 1024:
                    self.errors.append(f"Field 'description' exceeds 1024 characters (found {len(description)})")
                else:
                    print(f"✓ Description: '{description[:60]}...'")

            # Validate optional fields
            # Support both formats: top-level and nested under metadata
            version = None
            dependencies = None

            if 'metadata' in frontmatter and isinstance(frontmatter['metadata'], dict):
                # New format: nested under metadata (required for claude.ai)
                version = frontmatter['metadata'].get('version')
                dependencies = frontmatter['metadata'].get('dependencies')
            else:
                # Old format: top-level (still supported for Claude Code)
                version = frontmatter.get('version')
                dependencies = frontmatter.get('dependencies')

            if version:
                # Check for semantic versioning format
                if not re.match(r'^\d+\.\d+\.\d+', str(version)):
                    self.warnings.append(f"Version '{version}' doesn't follow semantic versioning (X.Y.Z)")
                else:
                    print(f"✓ Version: {version}")

            if dependencies:
                if dependencies != 'none':
                    print(f"✓ Dependencies: {dependencies}")

            print("✓ Frontmatter validation passed")
            return True

        except Exception as e:
            self.errors.append(f"Error reading Skill.md: {e}")
            return False

    def check_recommended_files(self):
        """Check for recommended files."""
        recommended = {
            'README.md': 'User documentation',
            'REFERENCE.md': 'Technical reference'
        }

        for filename, description in recommended.items():
            filepath = self.skill_path / filename
            if filepath.exists():
                print(f"✓ Found {filename} ({description})")
            else:
                self.warnings.append(f"Recommended file '{filename}' not found ({description})")

    def validate_file_references(self):
        """Validate that referenced files exist."""
        if not self.skill_md_path.exists():
            return

        content = self.skill_md_path.read_text()

        # Look for file references in markdown
        # Common patterns: `path/to/file`, "path/to/file", resources/file
        file_patterns = [
            r'`([^`]+\.(md|py|js|json|csv|txt))`',
            r'["\']([^"\']+\.(md|py|js|json|csv|txt))["\']',
            r'resources/([^\s\)]+)',
            r'scripts/([^\s\)]+)',
            r'templates/([^\s\)]+)'
        ]

        referenced_files = set()
        for pattern in file_patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                referenced_files.add(match.group(1))

        # Check if referenced files exist
        for ref_file in referenced_files:
            file_path = self.skill_path / ref_file
            if not file_path.exists():
                self.warnings.append(f"Referenced file not found: {ref_file}")

    def print_results(self):
        """Print validation results."""
        print("\n" + "=" * 60)
        print("VALIDATION RESULTS")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ All checks passed! Skill is valid.")
        elif not self.errors:
            print(f"\n✅ Validation passed with {len(self.warnings)} warning(s).")
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s).")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: validate-skill.py <skill-directory>")
        print("\nExample:")
        print("  python validate-skill.py weaver-create")
        sys.exit(1)

    skill_path = sys.argv[1]
    validator = SkillValidator(skill_path)

    if validator.validate():
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
