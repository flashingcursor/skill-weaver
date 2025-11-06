# Changelog

All notable changes to the skill-creator plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
