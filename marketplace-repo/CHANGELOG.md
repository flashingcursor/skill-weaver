# Changelog

All notable changes to the skill-weaver-marketplace will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2025-11-07

### Directory Rename

The skill-weaver-marketplace now includes weaver v0.2.1 with directory renamed to fully avoid conflicts with Anthropic's default skills.

#### Updated

**weaver v0.2.1**
- Renamed directory from "skill-creator/" to "weaver-create/"
- Updated all documentation references
- Added awareness notes about both Anthropic "skill-builder" AND "skill-creator"
- Updated all installation paths and examples

**Changes:**
- Directory structure renamed to avoid any conflicts
- Documentation updated throughout
- Improved clarity on potential conflicts with Anthropic's default skills

**Installation:**
```bash
/plugin marketplace add flashingcursor/skill-weaver-marketplace
/plugin install weaver
```

## [0.2.0] - 2025-11-07

### Renamed to Weaver

The skill-weaver-marketplace now includes weaver v0.2.0 (renamed from skill-creator) to avoid conflicts with Anthropic's default skill-builder.

#### Updated

**weaver v0.2.0 (formerly skill-creator)**
- Renamed skill from "skill-creator" to "weaver"
- Updated to avoid naming conflicts with Anthropic's default "skill-builder" skill
- Added awareness notes about potential conflicts
- Updated all documentation and installation commands

**Breaking Changes:**
- ⚠️ Plugin name changed from "skill-creator" to "weaver"
- ⚠️ Installation command changed to `/plugin install weaver@skill-weaver-marketplace`
- ⚠️ Users will need to uninstall old "skill-creator" and install new "weaver"

**Installation:**
```bash
/plugin marketplace add flashingcursor/skill-weaver-marketplace
/plugin install weaver
```

## [0.1.1-beta.1] - 2025-11-07

### UX Improvements Beta

The skill-weaver-marketplace now includes the beta release of skill-creator (v0.1.1-beta.1) with UX improvements based on user feedback.

#### Updated

**skill-creator v0.1.1-beta.1**
- UX improvements beta release
- Concise summary format instead of overwhelming comprehensive reviews
- Artifact creation for real-time file visibility
- Download link repetition pattern to prevent loss in scrollback

**Key Changes:**
- Phase 2 changed from comprehensive review to digestible summary
- Shows files created, key features (3-5 bullets), and prominent download link
- Offers to explain decisions instead of explaining everything upfront
- Artifact panes now open during creation for better visibility
- Download links repeated after explanations and changes

**User Feedback Addressed:**
- ✓ Initial review was too comprehensive → now concise with offer to elaborate
- ✓ Download links lost in scrollback → now repeated after responses
- ✓ Missing artifact panes → now explicitly creates artifacts for visibility

**Installation:**
```bash
/plugin marketplace add flashingcursor/skill-weaver-marketplace
/plugin install skill-creator
```

## [0.1.0] - 2025-11-06

### First Production Release

The skill-weaver-marketplace now includes the first production release of skill-creator (v0.1.0).

#### Updated

**skill-creator v0.1.0**
- First stable, production-ready release
- Complete adaptive workflow system
- Full dual-platform support (Claude Code and claude.ai)

**Key Features Available:**
- Adaptive workflow modes (Quick Create, Guided Create, Default)
- Autonomous skill creation with progress indicators
- Engagement detection and response adaptation
- Comprehensive skill creation guide
- Ready-to-use templates (basic and advanced)
- Script examples (Python and JavaScript)
- Automated validation and best practices
- Security guidelines
- Progressive disclosure patterns

**Installation:**
```bash
/plugin marketplace add flashingcursor/skill-weaver-marketplace
/plugin install skill-creator
```

**Usage Examples:**
```
"Create a new skill for code reviews"
"Just quickly create a skill for API testing"
"Walk me through creating a data analysis skill"
```

#### Documentation

- Updated README with new features list
- Added adaptive workflow mode examples
- Enhanced usage documentation

## [0.1.0-alpha.5] - 2025-11-06

### Updated
- skill-creator v0.1.0-alpha.5 with adaptive workflow system

## [0.1.0-alpha.4] - 2025-11-06

### Updated
- skill-creator v0.1.0-alpha.4 with enhanced dual-platform compatibility

## [0.1.0-alpha.3] - 2025-11-05

### Updated
- skill-creator v0.1.0-alpha.3 with fixed auto-release workflow

## [0.1.0-alpha.2] - 2025-11-05

### Updated
- skill-creator v0.1.0-alpha.2 with claude.ai frontmatter compatibility

## [0.1.0-alpha.1] - 2025-11-05

### Added
- Initial marketplace release
- skill-creator v0.1.0-alpha.1 plugin

[0.1.0]: https://github.com/flashingcursor/skill-weaver-marketplace/compare/v0.1.0-alpha.5...v0.1.0
[0.1.0-alpha.5]: https://github.com/flashingcursor/skill-weaver-marketplace/compare/v0.1.0-alpha.4...v0.1.0-alpha.5
[0.1.0-alpha.4]: https://github.com/flashingcursor/skill-weaver-marketplace/compare/v0.1.0-alpha.3...v0.1.0-alpha.4
[0.1.0-alpha.3]: https://github.com/flashingcursor/skill-weaver-marketplace/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[0.1.0-alpha.2]: https://github.com/flashingcursor/skill-weaver-marketplace/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[0.1.0-alpha.1]: https://github.com/flashingcursor/skill-weaver-marketplace/releases/tag/v0.1.0-alpha.1
