# Changelog

All notable changes to the weaver plugin (formerly skill-creator) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2025-11-07

### Directory Rename

This release renames the directory structure to fully avoid conflicts with Anthropic's default skills.

#### Changed

**Directory Structure**
- Renamed directory from "skill-creator/" to "weaver-create/"
- Updated plugin repository structure to match
- Updated all file paths in documentation

**Awareness Updates**
- Updated awareness notes to mention both "skill-builder" AND "skill-creator"
- Clarified that both Anthropic default skills may respond to requests
- Improved guidance on explicitly invoking Skill Weaver

**Documentation**
- Updated all references from "skill-creator/" to "weaver-create/"
- Updated installation paths and examples
- Updated INSTALLATION.md, SHARING.md, README.md, and all templates

## [0.2.0] - 2025-11-07

### Renamed to Weaver

This release renames the skill from "skill-creator" to "weaver" to avoid conflicts with Anthropic's default "skill-builder" skill.

#### Changed

**Skill Name and Branding**
- Renamed skill from "skill-creator" to "weaver" in frontmatter
- Updated description to use "weaves" terminology instead of "creates"
- Changed skill display name to "Skill Weaver"
- Updated plugin.json name field to "weaver"
- Updated all documentation references

**Added Awareness**
- Added prominent note about Anthropic's default "skill-builder" skill
- Provided guidance on how to explicitly invoke Skill Weaver when needed
- Updated description keywords to include "weaving" and "crafting"

**Breaking Changes**
- ⚠️ Plugin name changed from "skill-creator" to "weaver"
- ⚠️ Installation command changed to `/plugin install weaver@skill-weaver-marketplace`
- ⚠️ Users will need to uninstall old "skill-creator" and install new "weaver" plugin

## [0.1.1-beta.1] - 2025-11-07

### UX Improvements Beta

This beta release addresses user feedback about the adaptive workflow being too overwhelming.

#### Changed

**Phase 2: Concise Summary (Previously Comprehensive Review)**
- Changed from comprehensive review to digestible summary format
- Shows files created, key features (3-5 bullets), and prominent download link
- Offers to explain decisions instead of explaining everything upfront
- More inviting for specific questions vs overwhelming detail

**Artifact Creation**
- Added explicit guidance to create artifacts during Phase 1
- Uses Write tool for each file (SKILL.md, REFERENCE.md, templates, scripts)
- Opens artifact panes for real-time visibility during creation
- Restores user-preferred behavior from earlier version

**Download Link Management**
- Repeats download links after explanations to prevent loss in scrollback
- Repeats after making changes to maintain accessibility
- Consistent format: "**Download:** [Download skill-name.zip]"
- Reduces user frustration from having to scroll back

#### Added

**Documentation**
- Updated Initial Review Pattern in REFERENCE.md to concise format
- Added Artifact Creation Patterns section (134 lines)
- Added Download Link Management section (75 lines)
- Updated example interaction to show new concise format

**User Feedback Addressed:**
- ✓ Initial review was too comprehensive → now concise with offer to elaborate
- ✓ Download links lost in scrollback → now repeated after responses
- ✓ Missing artifact panes → now explicitly creates artifacts for visibility

## [0.1.0] - 2025-11-06

### First Production Release

This is the first stable, production-ready release of the skill-creator plugin.

#### Added

**Adaptive Workflow System**
- Quick Create Mode: Fast, autonomous skill creation with minimal interaction
- Guided Create Mode: Collaborative, educational skill creation with step-by-step guidance
- Default (Adaptive) Mode: Automatically adapts to user engagement level

**Engagement Detection**
- Comprehensive engagement pattern recognition (473 lines)
- Detects low, medium, and high engagement signals from user feedback
- Seamless transitions between engagement modes
- Response templates for each engagement level

**Progress Indicators & Decision Explanations**
- Real-time progress indicators during skill creation
- Clear explanations of key decisions made
- Decision rationale helps users understand choices

**Workflow Mode Deep Dive**
- Advanced implementation patterns (403 lines)
- Decision-making heuristics for each mode
- Educational patterns and question formats
- Common pitfalls and solutions

**Dual-Platform Support**
- Full compatibility with both Claude Code and claude.ai
- Metadata field format for frontmatter
- Platform-specific features clearly documented
- Defaults to "both platforms" approach

#### Documentation

- Comprehensive README with workflow mode examples
- Detailed REFERENCE.md with engagement detection patterns
- Updated templates with dual-platform compatibility notes
- Complete installation and usage guides

#### Changed

- Improved skill creation workflow from ask-then-build to create-review-adapt
- Enhanced user experience with engagement-based adaptation
- Clearer documentation structure

## [0.1.0-alpha.5] - 2025-11-06

### Added
- Adaptive skill creation workflow with engagement detection and progress indicators
- Three-phase interaction model (create → review → adapt)
- Engagement level detection from user feedback

## [0.1.0-alpha.4] - 2025-11-06

### Changed
- Enhanced dual-platform compatibility with version redundancy
- Improved documentation for claude.ai and Claude Code differences

## [0.1.0-alpha.3] - 2025-11-05

### Fixed
- Auto-release workflow to extract version from metadata field

## [0.1.0-alpha.2] - 2025-11-05

### Fixed
- Frontmatter structure for claude.ai compatibility
- Updated documentation for metadata field format

## [0.1.0-alpha.1] - 2025-11-05

### Added
- Initial alpha release of skill-creator plugin
- Basic skill creation functionality
- Templates for basic and advanced skills
- Script examples (Python and JavaScript)
- Validation and best practices

[0.1.0]: https://github.com/flashingcursor/skill-creator-plugin/compare/v0.1.0-alpha.5...v0.1.0
[0.1.0-alpha.5]: https://github.com/flashingcursor/skill-creator-plugin/compare/v0.1.0-alpha.4...v0.1.0-alpha.5
[0.1.0-alpha.4]: https://github.com/flashingcursor/skill-creator-plugin/compare/v0.1.0-alpha.3...v0.1.0-alpha.4
[0.1.0-alpha.3]: https://github.com/flashingcursor/skill-creator-plugin/compare/v0.1.0-alpha.2...v0.1.0-alpha.3
[0.1.0-alpha.2]: https://github.com/flashingcursor/skill-creator-plugin/compare/v0.1.0-alpha.1...v0.1.0-alpha.2
[0.1.0-alpha.1]: https://github.com/flashingcursor/skill-creator-plugin/releases/tag/v0.1.0-alpha.1
