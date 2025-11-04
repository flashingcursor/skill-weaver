#!/usr/bin/env python3
"""
Update version in Skill.md frontmatter.

Usage: update-version.py <skill-directory> <version>
Example: update-version.py skill-creator 1.2.0
"""

import sys
import re
from pathlib import Path


def update_version(skill_path, new_version):
    """Update version in Skill.md frontmatter."""
    skill_md = Path(skill_path) / "Skill.md"

    if not skill_md.exists():
        print(f"Error: Skill.md not found at {skill_md}", file=sys.stderr)
        return False

    content = skill_md.read_text()

    # Update version in frontmatter
    # Match: version: <anything>
    pattern = r'^version:\s*.*$'
    replacement = f'version: {new_version}'

    updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    if updated_content == content:
        print(f"Warning: No version field found to update", file=sys.stderr)
        return False

    skill_md.write_text(updated_content)
    print(f"✓ Updated version to {new_version} in {skill_md}")
    return True


def main():
    if len(sys.argv) != 3:
        print("Usage: update-version.py <skill-directory> <version>", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print("  python update-version.py skill-creator 1.2.0", file=sys.stderr)
        sys.exit(1)

    skill_path = sys.argv[1]
    version = sys.argv[2]

    # Validate version format (basic check)
    if not re.match(r'^\d+\.\d+\.\d+', version):
        print(f"Warning: Version '{version}' doesn't follow semantic versioning (X.Y.Z)", file=sys.stderr)

    if update_version(skill_path, version):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
