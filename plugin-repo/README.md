# Skill Weaver Plugin

Claude Code plugin containing the "weaver" skill for creating custom Skills.

> **Important**: Directory renamed from "skill-creator" to "weaver-create" in v0.2.1 to fully avoid conflicts with Anthropic's default skills ("skill-builder" and "skill-creator").

## Latest Release

**Version 0.2.1** - Directory Rename (2025-11-07)

This release renames the directory structure to fully avoid conflicts with Anthropic's default skills. See [CHANGELOG.md](CHANGELOG.md) for full release notes.

**Key Changes:**
- ✅ Renamed directory from "skill-creator/" to "weaver-create/"
- ✅ Updated all documentation references
- ✅ Added awareness note about both Anthropic "skill-builder" and "skill-creator"
- ✅ Updated all installation paths

## What's Included

This plugin provides the **weaver** skill, which helps you create custom Skills for Claude following official best practices.

**Version**: 0.2.1

## Installation

### Via Marketplace (Recommended)

```bash
# Add the Skill Weaver marketplace
/plugin marketplace add flashingcursor/skill-weaver-marketplace

# Install the skill-creator plugin
/plugin install weaver@skill-weaver-marketplace
```

### Manual Installation

```bash
# Clone this repository
git clone https://github.com/flashingcursor/skill-creator-plugin.git

# Install as local plugin
/plugin install ./skill-creator-plugin
```

## Usage

Once installed, the skill-creator skill is automatically available. Try:

```
"Create a new skill for code reviews"
"Help me build a skill for data analysis"
"Create a skill for [your purpose]"
```

### Adaptive Workflow Modes

The skill-creator adapts to your preferred interaction style:

**Quick Create** - Fast and autonomous:
```
"Just quickly create a skill for API testing"
```

**Guided Create** - Collaborative and educational:
```
"Walk me through creating a data analysis skill"
```

**Default (Adaptive)** - Automatically adapts based on your feedback:
```
"Create a skill for processing documents"
```

The skill will create complete, functional skills autonomously, show you what it built with decision explanations, detect your engagement level, and adapt accordingly.

## What You Can Build

With skill-creator, create:
- **Knowledge Skills**: Embed guidelines, documentation, or best practices
- **Workflow Skills**: Automate multi-step processes
- **Analysis Skills**: Data processing and reporting workflows
- **Integration Skills**: Connect Claude to your tools
- **Template Skills**: Reusable templates for common tasks

## Documentation

- **Installation Guide**: [INSTALLATION.md](https://github.com/flashingcursor/skill-weaver/blob/master/INSTALLATION.md)
- **Sharing Guide**: [SHARING.md](https://github.com/flashingcursor/skill-weaver/blob/master/SHARING.md)
- **Main Repository**: [flashingcursor/skill-weaver](https://github.com/flashingcursor/skill-weaver)

## What's Inside

```
skill-creator-plugin/
├── .claude-plugin/
│   └── plugin.json        # Plugin metadata
├── skills/
│   └── skill-creator/
│       ├── Skill.md       # Main skill instructions
│       ├── README.md      # Skill documentation
│       ├── REFERENCE.md   # Technical reference
│       └── templates/     # Skill templates and examples
└── README.md              # This file
```

## Updates

To update to the latest version:

```bash
# If installed via marketplace
/plugin update skill-creator

# If installed manually
cd skill-creator-plugin
git pull origin master
/plugin reload skill-creator
```

## Support

- **Issues**: [GitHub Issues](https://github.com/flashingcursor/skill-weaver/issues)
- **Discussions**: [GitHub Discussions](https://github.com/flashingcursor/skill-weaver/discussions)
- **Main Repository**: [flashingcursor/skill-weaver](https://github.com/flashingcursor/skill-weaver)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## About

This plugin is part of the Skill Weaver project, providing tools and templates for creating custom Claude Skills.

- **Main Repository**: https://github.com/flashingcursor/skill-weaver
- **Plugin Repository**: https://github.com/flashingcursor/skill-creator-plugin
- **Marketplace**: https://github.com/flashingcursor/skill-weaver-marketplace
