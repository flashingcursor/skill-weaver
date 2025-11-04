#!/usr/bin/env python3
"""
Generate release notes for a skill release.

Usage: generate-release-notes.py <skill-directory> <version>
Example: generate-release-notes.py skill-creator 1.2.0
"""

import sys
import yaml
import re
from pathlib import Path
from datetime import datetime


def extract_frontmatter(skill_md_path):
    """Extract YAML frontmatter from Skill.md."""
    content = skill_md_path.read_text()

    if not content.startswith('---'):
        return None

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None

    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def get_file_stats(skill_path):
    """Get statistics about the skill files."""
    stats = {
        'total_files': 0,
        'templates': 0,
        'scripts': 0,
        'docs': 0
    }

    for file in skill_path.rglob('*'):
        if file.is_file():
            stats['total_files'] += 1

            if 'template' in file.name.lower():
                stats['templates'] += 1
            elif file.suffix in ['.py', '.js', '.sh']:
                stats['scripts'] += 1
            elif file.suffix in ['.md', '.txt', '.rst']:
                stats['docs'] += 1

    return stats


def extract_features_from_readme(skill_path):
    """Extract features from README.md if available."""
    readme = skill_path / "README.md"
    if not readme.exists():
        return []

    content = readme.read_text()

    # Look for features section
    features = []
    in_features = False

    for line in content.split('\n'):
        if re.match(r'^##\s+(Features|What.*Does|Key Features)', line, re.IGNORECASE):
            in_features = True
            continue
        elif in_features and re.match(r'^##\s+', line):
            break
        elif in_features and line.strip().startswith('-'):
            feature = line.strip().lstrip('- ').strip()
            if feature:
                features.append(feature)

    return features[:5]  # Limit to first 5 features


def generate_release_notes(skill_path, version):
    """Generate release notes for the skill."""
    skill_path = Path(skill_path)
    skill_md = skill_path / "Skill.md"

    if not skill_md.exists():
        print(f"Error: Skill.md not found", file=sys.stderr)
        return None

    # Extract frontmatter
    frontmatter = extract_frontmatter(skill_md)
    if not frontmatter:
        print("Error: Could not parse frontmatter", file=sys.stderr)
        return None

    # Get file statistics
    stats = get_file_stats(skill_path)

    # Extract features
    features = extract_features_from_readme(skill_path)

    # Generate release notes
    notes = []

    # Header
    notes.append(f"# {frontmatter.get('name', 'Custom Skill')} v{version}")
    notes.append("")
    notes.append(f"Released on {datetime.now().strftime('%Y-%m-%d')}")
    notes.append("")

    # Description
    if 'description' in frontmatter:
        notes.append("## Overview")
        notes.append("")
        notes.append(frontmatter['description'])
        notes.append("")

    # Features
    if features:
        notes.append("## Key Features")
        notes.append("")
        for feature in features:
            notes.append(f"- {feature}")
        notes.append("")

    # Contents
    notes.append("## Package Contents")
    notes.append("")
    notes.append(f"This package includes:")
    notes.append(f"- **{stats['docs']}** documentation files")
    notes.append(f"- **{stats['templates']}** templates")
    notes.append(f"- **{stats['scripts']}** scripts")
    notes.append(f"- **{stats['total_files']}** total files")
    notes.append("")

    # Installation
    notes.append("## Installation")
    notes.append("")
    notes.append("1. Download `skill-creator-" + version + ".zip` from the assets below")
    notes.append("2. Open Claude and navigate to **Settings > Capabilities**")
    notes.append("3. Click **Upload Skill** and select the downloaded ZIP file")
    notes.append("4. Enable the skill in your capabilities list")
    notes.append("")

    # Usage
    notes.append("## Usage")
    notes.append("")
    notes.append("Once installed, you can use this skill by asking Claude:")
    notes.append('```')
    notes.append('"Create a new skill for [your purpose]"')
    notes.append('"Help me build a skill that does [task]"')
    notes.append('"I need a custom skill for [workflow]"')
    notes.append('```')
    notes.append("")

    # Dependencies
    if 'dependencies' in frontmatter and frontmatter['dependencies'] != 'none':
        notes.append("## Dependencies")
        notes.append("")
        notes.append(f"```")
        notes.append(frontmatter['dependencies'])
        notes.append(f"```")
        notes.append("")

    # Resources
    notes.append("## Resources")
    notes.append("")
    notes.append("- [Skills Documentation](https://docs.claude.com/claude/docs/skills)")
    notes.append("- [Example Skills](https://github.com/anthropics/skills)")
    notes.append("- [Skill Authoring Best Practices](https://docs.claude.com/claude/docs/skill-authoring-best-practices)")
    notes.append("")

    # Changelog
    notes.append("## What's Changed")
    notes.append("")
    notes.append(f"See the commit history for detailed changes in this release.")
    notes.append("")

    # Footer
    notes.append("---")
    notes.append("")
    notes.append("**Full Changelog**: https://github.com/$GITHUB_REPOSITORY/commits/v" + version)

    return '\n'.join(notes)


def main():
    if len(sys.argv) != 3:
        print("Usage: generate-release-notes.py <skill-directory> <version>", file=sys.stderr)
        print("\nExample:", file=sys.stderr)
        print("  python generate-release-notes.py skill-creator 1.2.0", file=sys.stderr)
        sys.exit(1)

    skill_path = sys.argv[1]
    version = sys.argv[2]

    notes = generate_release_notes(skill_path, version)
    if notes:
        print(notes)
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
