# Skill Weaver

A meta-skill repository for creating Custom Skills for Claude.

[![GitHub release](https://img.shields.io/github/v/release/flashingcursor/skill-weaver?include_prereleases)](https://github.com/flashingcursor/skill-weaver/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## What is This?

This repository contains **Skill Weaver**, a Custom Skill that helps you build other Custom Skills for Claude. It's a comprehensive guide and toolset that ensures your skills follow best practices, proper structure, and security guidelines.

**Works on both**:
- ✅ **claude.ai** (ZIP upload)
- ✅ **Claude Code** (Plugin, Git, or Manual install)

## Installation

### 📦 Quick Install

**For claude.ai**:
1. [Download latest release](https://github.com/flashingcursor/skill-weaver/releases/latest) (ZIP file)
2. Go to Settings → Capabilities → Skills → Upload
3. Enable and test: _"Create a skill for code reviews"_

**For Claude Code**:
```bash
# Via Plugin Marketplace (recommended)
/plugin marketplace add flashingcursor/skill-weaver-marketplace
/plugin install skill-creator

# Or via Git
git clone https://github.com/flashingcursor/skill-weaver.git
cp -r skill-weaver/skill-creator ~/.claude/skills/
# Restart Claude Code
```

📚 **Detailed Instructions**: See [INSTALLATION.md](INSTALLATION.md) for step-by-step guides, troubleshooting, and all installation methods.

## Sharing with Your Team

Want to distribute this skill to your team or organization?

👥 **See [SHARING.md](SHARING.md)** for:
- Distribution methods for teams
- Plugin marketplace setup
- Team rollout guides
- Announcement templates
- Best practices for adoption

## Quick Start

Once installed, try these prompts:

```
"Create a new skill for [your purpose]"
"Help me build a skill that does [task]"
"Create a skill for code reviews"
"Build a skill for analyzing CSV data"
```

### For Developers

```bash
# Clone the repository
git clone https://github.com/flashingcursor/skill-weaver.git
cd skill-weaver

# Validate the skill
python .github/scripts/validate-skill.py skill-creator

# Package the skill
./scripts/package-skill.sh
```

## Features

- **Comprehensive Skill Creation Guide**: Step-by-step instructions for building Custom Skills
- **Templates**: Ready-to-use templates for basic and advanced skills
- **Script Examples**: Python and JavaScript templates with best practices
- **Automated Validation**: CI/CD workflows to ensure quality
- **Automated Releases**: GitHub Actions for packaging and distribution
- **Security Scanning**: Built-in checks for common security issues
- **Progressive Disclosure**: Teaches Claude's efficient loading system

## Repository Structure

```
skill-weaver/
├── .github/
│   ├── workflows/
│   │   ├── validate.yml          # Validation workflow
│   │   └── release.yml            # Release automation
│   └── scripts/
│       ├── validate-skill.py      # Skill validation script
│       ├── update-version.py      # Version updater
│       └── generate-release-notes.py  # Release notes generator
├── scripts/
│   └── package-skill.sh           # Local packaging script
└── weaver-create/
    ├── Skill.md                   # Main skill file
    ├── README.md                  # Skill documentation
    ├── REFERENCE.md               # Technical reference
    └── templates/
        ├── basic-skill-template.md
        ├── advanced-skill-template.md
        ├── example-script.py
        └── example-script.js
```

## CI/CD Pipeline

### Automated Validation

Every push and pull request triggers validation checks:

- ✅ YAML frontmatter structure and field validation
- ✅ Semantic versioning compliance
- ✅ Security scanning for hardcoded secrets
- ✅ Python and JavaScript syntax validation
- ✅ Documentation completeness
- ✅ File reference integrity

**View workflow**: [`.github/workflows/validate.yml`](.github/workflows/validate.yml)

### Automated Releases

When you push a version tag, the pipeline automatically:

1. Validates the skill structure
2. Updates version in Skill.md
3. Packages into a ZIP file
4. Generates release notes
5. Creates a GitHub release
6. Uploads the package as an artifact

**Create a release**:
```bash
git tag v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

**View workflow**: [`.github/workflows/release.yml`](.github/workflows/release.yml)

## Development

### Testing Your Changes

```bash
# Validate skill structure
python .github/scripts/validate-skill.py skill-creator

# Check Python scripts
python -m py_compile weaver-create/templates/*.py

# Check JavaScript scripts
node --check weaver-create/templates/*.js

# Package locally
./scripts/package-skill.sh
```

### Creating a Release

1. Update the version in `weaver-create/Skill.md`
2. Update the version history in `weaver-create/README.md`
3. Commit your changes
4. Create and push a tag:
   ```bash
   git tag v1.1.0 -m "Release version 1.1.0"
   git push origin v1.1.0
   ```
5. GitHub Actions will automatically create the release

### Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes to skill structure or behavior
- **MINOR**: New features, templates, or capabilities
- **PATCH**: Bug fixes, documentation updates, typos

## What You'll Learn

Using the Skill Weaver teaches you:

- ✅ How to structure Custom Skills properly
- ✅ YAML frontmatter requirements and best practices
- ✅ Progressive disclosure for efficient loading
- ✅ Script integration with Python and JavaScript
- ✅ Security considerations for skills
- ✅ Testing and validation strategies
- ✅ Packaging and distribution methods

## Skills You Can Create

With Skill Weaver, you can build:

- **Knowledge Skills**: Embed company guidelines, style guides, or documentation
- **Workflow Skills**: Automate repetitive multi-step processes
- **Analysis Skills**: Create data processing and reporting workflows
- **Integration Skills**: Connect Claude to your tools and systems
- **Template Skills**: Provide reusable templates for common tasks

## Examples

### Creating a Brand Guidelines Skill
```
User: "Create a skill for our company brand guidelines"

Skill Weaver will help you:
1. Structure brand colors, fonts, and logo rules
2. Add example materials
3. Define when to apply the guidelines
4. Package for team distribution
```

### Creating a Data Analysis Skill
```
User: "Build a skill that analyzes CSV files and creates reports"

Skill Weaver will help you:
1. Set up Python script with pandas
2. Define input/output formats
3. Add error handling
4. Include example data
5. Test and validate
```

## Documentation

### This Repository
- **[INSTALLATION.md](INSTALLATION.md)** - Complete installation guide for all platforms
- **[SHARING.md](SHARING.md)** - Team distribution and rollout guide
- **[weaver-create/Skill.md](weaver-create/Skill.md)** - Main skill instructions
- **[weaver-create/REFERENCE.md](weaver-create/REFERENCE.md)** - Technical reference
- **[weaver-create/README.md](weaver-create/README.md)** - Skill overview

### External Resources
- **Skills Documentation**: [Claude Skills Docs](https://docs.claude.com/claude/docs/skills)
- **Example Skills**: [Anthropic Skills Repository](https://github.com/anthropics/skills)
- **Best Practices**: [Skill Authoring Guide](https://docs.claude.com/claude/docs/skill-authoring-best-practices)

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues**: Found a bug? [Open an issue](../../issues)
2. **Suggest Features**: Have ideas? [Start a discussion](../../discussions)
3. **Submit PRs**: Improvements welcome!
4. **Share Skills**: Create a skill using Skill Weaver and share your experience

### Contributing Guidelines

- Follow the existing code style
- Update documentation for changes
- Add tests where applicable
- Ensure CI passes
- Use semantic commit messages

## Security

If you discover a security issue, please email us directly rather than opening a public issue.

## License

This project is provided as an example and educational resource for creating Custom Skills for Claude.

## Acknowledgments

Created to help the Claude community build better Custom Skills.

---

**Made with** the Skill Weaver skill itself! 🎨
