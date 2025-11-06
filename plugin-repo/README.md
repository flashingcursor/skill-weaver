# Skill Creator Plugin

Claude Code plugin containing the skill-creator skill.

## Latest Release

**Version 0.1.0** - First Production Release (2025-11-06)

This is the first stable, production-ready release with the complete adaptive workflow system. See [CHANGELOG.md](CHANGELOG.md) for full release notes.

**Key Features:**
- ✅ Adaptive workflow modes (Quick Create, Guided Create, Default)
- ✅ Engagement detection and response adaptation
- ✅ Progress indicators and decision explanations
- ✅ Full dual-platform support (Claude Code and claude.ai)

## What's Included

This plugin provides the **skill-creator** skill, which helps you create custom Skills for Claude following official best practices.

**Version**: 0.1.0

## Installation

### Via Marketplace (Recommended)

```bash
# Add the Skill Weaver marketplace
/plugin marketplace add flashingcursor/skill-weaver-marketplace

# Install the skill-creator plugin
/plugin install skill-creator@skill-weaver-marketplace
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
