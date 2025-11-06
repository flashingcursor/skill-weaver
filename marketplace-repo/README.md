# Skill Weaver Marketplace

Claude Code marketplace for Skill Weaver plugins - tools for creating and managing custom Claude Skills.

## Installation

Add this marketplace to your Claude Code:

```bash
/plugin marketplace add flashingcursor/skill-weaver-marketplace
```

## Available Plugins

### skill-creator v0.1.0-alpha.5

Creates custom Skills for Claude following official best practices.

**Install**:
```bash
/plugin install skill-creator@skill-weaver-marketplace
```

**Features**:
- Comprehensive skill creation guide
- Ready-to-use templates (basic and advanced)
- Script examples (Python and JavaScript)
- Automated validation and best practices
- Security guidelines
- Progressive disclosure patterns

**Usage**:
```
"Create a new skill for code reviews"
"Help me build a skill for data analysis"
```

**Documentation**:
- [Installation Guide](https://github.com/flashingcursor/skill-weaver/blob/master/INSTALLATION.md)
- [Sharing Guide](https://github.com/flashingcursor/skill-weaver/blob/master/SHARING.md)
- [Main Repository](https://github.com/flashingcursor/skill-weaver)

## What You Can Build

With the skill-creator plugin, create:

- **Knowledge Skills**: Embed guidelines, documentation, or best practices
- **Workflow Skills**: Automate multi-step processes
- **Analysis Skills**: Data processing and reporting workflows
- **Integration Skills**: Connect Claude to your tools
- **Template Skills**: Reusable templates for common tasks

## Quick Start

```bash
# Add marketplace
/plugin marketplace add flashingcursor/skill-weaver-marketplace

# Install skill-creator
/plugin install skill-creator@skill-weaver-marketplace

# Try it out
```

Then ask Claude:
```
"Create a skill for reviewing pull requests"
```

## Marketplace Structure

This marketplace provides plugins for:
- Creating custom Skills
- Managing Skill workflows
- Sharing Skills with teams
- Validating Skill structure

## For Teams

Want your team to automatically have access to these plugins?

Add to your project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "skill-weaver": {
      "source": {
        "source": "github",
        "repo": "flashingcursor/skill-weaver-marketplace"
      }
    }
  }
}
```

Team members will get the marketplace when they trust the folder.

## Plugin Repositories

- **skill-creator**: https://github.com/flashingcursor/skill-creator-plugin

## Support

- **Issues**: [GitHub Issues](https://github.com/flashingcursor/skill-weaver/issues)
- **Discussions**: [GitHub Discussions](https://github.com/flashingcursor/skill-weaver/discussions)
- **Documentation**: [Main Repository](https://github.com/flashingcursor/skill-weaver)

## Contributing

Want to add your plugin to this marketplace?

1. Create a Claude Code plugin following the [plugin structure](https://docs.claude.com/claude-code/plugins)
2. Open an issue or PR in the [main repository](https://github.com/flashingcursor/skill-weaver)
3. We'll review and add it to the marketplace

**Criteria for inclusion**:
- Helps with skill creation or management
- Follows Claude Code plugin best practices
- Well-documented with examples
- Active maintenance

## About Skill Weaver

Skill Weaver is a project dedicated to helping developers create high-quality custom Skills for Claude.

- **Main Repository**: https://github.com/flashingcursor/skill-weaver
- **Plugin**: https://github.com/flashingcursor/skill-creator-plugin
- **Marketplace**: https://github.com/flashingcursor/skill-weaver-marketplace

## License

MIT License - see individual plugin repositories for details.

---

**Made with** the skill-creator skill itself! 🎨
