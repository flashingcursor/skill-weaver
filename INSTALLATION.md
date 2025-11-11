# Installation Guide

This guide provides step-by-step instructions for installing the **skill-creator** skill on both claude.ai and Claude Code.

## Table of Contents

- [For claude.ai Users](#for-claudeai-users)
- [For Claude Code Users](#for-claude-code-users)
  - [Method 1: Plugin Marketplace (Recommended)](#method-1-plugin-marketplace-recommended)
  - [Method 2: Git Clone](#method-2-git-clone)
  - [Method 3: Manual Copy](#method-3-manual-copy)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## For claude.ai Users

### Prerequisites
- A claude.ai account (free or paid)
- Access to Settings > Capabilities

### Step-by-Step Installation

#### 1. Download the Skill Package

**Option A: From GitHub Releases (Recommended)**

1. Visit the [releases page](https://github.com/flashingcursor/skill-weaver/releases)
2. Find the latest release (e.g., `v0.1.0-alpha.4`)
3. Download the ZIP file: `skill-creator-{version}.zip`

**Option B: Build from Source**

```bash
git clone https://github.com/flashingcursor/skill-weaver.git
cd skill-weaver
zip -r weaver-create.zip weaver-create/
```

#### 2. Upload to claude.ai

1. Open [claude.ai](https://claude.ai) in your browser
2. Click the **Settings** icon (⚙️) in the bottom-left corner
3. Navigate to **Capabilities** tab
4. Scroll to the **Skills** section
5. Click **Upload skill** button
6. Select the downloaded ZIP file
7. Wait for upload to complete (usually takes a few seconds)

#### 3. Enable the Skill

1. Find **skill-creator** in your skills list
2. Toggle the switch to **ON** (it will turn blue/green)
3. The skill is now active!

#### 4. Test the Installation

Start a new conversation and try:

```
Create a new skill for code reviews
```

or

```
Help me build a skill that analyzes CSV files
```

Claude should invoke the skill-creator and guide you through the process.

---

## For Claude Code Users

Claude Code offers multiple installation methods. Choose the one that best fits your workflow.

### Method 1: Plugin Marketplace (Recommended)

**Best for**: Professional teams, automatic updates, easy management

**Prerequisites**:
- Claude Code installed
- Access to terminal

**Installation Steps**:

```bash
# Add the Skill Weaver marketplace
/plugin marketplace add flashingcursor/skill-weaver-marketplace

# Install the skill-creator plugin
/plugin install skill-creator@skill-weaver-marketplace

# Restart Claude Code
```

**For Team Auto-Installation**:

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

Team members will automatically get the marketplace when they trust the folder.

---

### Method 2: Git Clone

**Best for**: Development, contributing, staying up-to-date with git

**Prerequisites**:
- Claude Code installed
- Git installed
- Terminal access

**Installation Steps**:

#### For Project-Specific Use (Shared with Team)

```bash
# Navigate to your project
cd /path/to/your/project

# Clone the repository
git clone https://github.com/flashingcursor/skill-weaver.git

# Create skills directory if it doesn't exist
mkdir -p .claude/skills

# Copy the skill
cp -r skill-weaver/skill-creator .claude/skills/

# Commit for team sharing
git add .claude/skills/skill-creator
git commit -m "Add skill-creator v0.1.0-alpha.4"
git push

# Restart Claude Code
```

#### For Personal Use (All Projects)

```bash
# Clone the repository
git clone https://github.com/flashingcursor/skill-weaver.git

# Copy to personal skills directory
cp -r skill-weaver/skill-creator ~/.claude/skills/

# Restart Claude Code
```

**Updating**:

```bash
cd skill-weaver
git pull origin master
cp -r skill-creator ~/.claude/skills/  # or .claude/skills/
# Restart Claude Code
```

---

### Method 3: Manual Copy

**Best for**: Quick testing, no git workflow

**Prerequisites**:
- Claude Code installed
- Downloaded ZIP or cloned repository

**Installation Steps**:

#### 1. Get the Skill Files

**Option A: Download ZIP**
1. Download from [releases](https://github.com/flashingcursor/skill-weaver/releases)
2. Extract the ZIP file
3. Locate the `weaver-create/` folder

**Option B: Clone Repository**
```bash
git clone https://github.com/flashingcursor/skill-weaver.git
cd skill-weaver
```

#### 2. Copy to Skills Directory

**For Personal Use:**
```bash
# Create directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r skill-creator ~/.claude/skills/
```

**For Project Use:**
```bash
# Navigate to your project
cd /path/to/your/project

# Create directory if it doesn't exist
mkdir -p .claude/skills

# Copy the skill
cp -r /path/to/skill-weaver/skill-creator .claude/skills/
```

#### 3. Restart Claude Code

The skill will be loaded on next startup.

---

## Verification

### For claude.ai

1. **Check Skills List**:
   - Go to Settings > Capabilities > Skills
   - Verify "skill-creator" appears and is enabled

2. **Test Invocation**:
   - Start a new conversation
   - Say: "Create a skill for analyzing code quality"
   - Look for Claude to invoke the skill (check thinking/reasoning)

3. **Expected Behavior**:
   - Claude should recognize skill creation requests
   - It should guide you through structure, frontmatter, examples
   - It should reference official best practices

### For Claude Code

1. **Check Skill Loading**:
   ```bash
   # Start Claude Code with debug mode (if available)
   claude --debug

   # Look for skill loading messages in logs
   ```

2. **List Available Skills** (if command exists):
   ```bash
   /skills list
   ```

3. **Test Invocation**:
   - Start a conversation
   - Ask: "Help me create a new skill for data analysis"
   - Claude should invoke skill-creator

4. **Verify Files**:
   ```bash
   # For personal skills
   ls -la ~/.claude/skills/weaver-create/

   # For project skills
   ls -la .claude/skills/weaver-create/

   # Should see: Skill.md, README.md, REFERENCE.md, templates/
   ```

---

## Troubleshooting

### claude.ai Issues

#### Skill doesn't appear after upload

**Possible causes**:
- Upload failed silently
- Browser cache issue
- Invalid ZIP structure

**Solutions**:
1. Try uploading again
2. Clear browser cache and reload
3. Verify ZIP structure:
   ```
   weaver-create.zip
     └── weaver-create/
         ├── Skill.md
         ├── README.md
         └── ...
   ```
4. Ensure Skill.md has valid YAML frontmatter

#### Skill not invoked

**Possible causes**:
- Skill not enabled
- Query doesn't match description triggers

**Solutions**:
1. Verify skill is toggled ON in Settings > Capabilities
2. Use explicit keywords: "create skill", "build skill", "skill authoring"
3. Check conversation thinking to see which skills were considered
4. Try starting a new conversation

#### Upload fails with error

**Possible causes**:
- Invalid frontmatter format
- File too large
- Network issue

**Solutions**:
1. Verify frontmatter uses `metadata` field format:
   ```yaml
   ---
   name: skill-name
   description: ...
   metadata:
     version: 1.0.0
   ---
   ```
2. Check file size is under limit (typically a few MB)
3. Try from different network/browser

---

### Claude Code Issues

#### Skill not loading

**Possible causes**:
- Installed in wrong location
- Invalid YAML frontmatter
- Claude Code not restarted

**Solutions**:
1. Verify installation path:
   ```bash
   # Should exist
   ls ~/.claude/skills/weaver-create/Skill.md
   # OR
   ls .claude/skills/weaver-create/Skill.md
   ```

2. Check frontmatter syntax:
   ```bash
   head -20 ~/.claude/skills/weaver-create/Skill.md
   # Look for valid YAML between --- markers
   ```

3. **Restart Claude Code** (required for skills to load)

4. Check for errors:
   ```bash
   # If debug mode available
   claude --debug
   ```

#### Skill works differently than claude.ai

**Expected behavior**:
- Claude Code may use `version` top-level OR `metadata.version`
- Both formats are supported
- The `metadata` format ensures compatibility with both platforms

**Verification**:
```bash
# Check which format is used
grep -A 2 "^version:" ~/.claude/skills/weaver-create/Skill.md
grep -A 3 "^metadata:" ~/.claude/skills/weaver-create/Skill.md
```

#### Plugin marketplace not found

**Possible causes**:
- Marketplace repository doesn't exist yet
- Network/access issue
- Wrong command syntax

**Solutions**:
1. Verify marketplace exists: https://github.com/flashingcursor/skill-weaver-marketplace
2. Check command syntax:
   ```bash
   /plugin marketplace add flashingcursor/skill-weaver-marketplace
   ```
3. Try alternate installation methods (git clone, manual copy)

#### Permission errors

**Possible causes**:
- Insufficient file permissions
- Protected system directories

**Solutions**:
```bash
# Fix permissions for personal skills
chmod 755 ~/.claude/skills
chmod -R 644 ~/.claude/skills/weaver-create/*
chmod 755 ~/.claude/skills/skill-creator

# Fix permissions for project skills
chmod 755 .claude/skills
chmod -R 644 .claude/skills/weaver-create/*
chmod 755 .claude/skills/skill-creator
```

---

### Getting Help

If you continue to experience issues:

1. **Check Documentation**:
   - [README.md](README.md) - Overview and quick start
   - [REFERENCE.md](weaver-create/REFERENCE.md) - Detailed technical reference
   - [SHARING.md](SHARING.md) - Team distribution guide

2. **GitHub Issues**:
   - Search existing issues: https://github.com/flashingcursor/skill-weaver/issues
   - Create new issue with:
     - Platform (claude.ai or Claude Code)
     - Installation method used
     - Error messages or logs
     - Steps to reproduce

3. **Community**:
   - GitHub Discussions (if enabled)
   - Claude Code community forums

4. **Verify Installation**:
   ```bash
   # Check version
   grep -A 1 "metadata:" weaver-create/Skill.md

   # Verify file integrity
   find skill-creator -type f -name "*.md" | wc -l
   # Should show 5 files (Skill.md, README.md, REFERENCE.md, 2 templates)
   ```

---

## Next Steps

After successful installation:

1. **Read the Documentation**:
   - [weaver-create/Skill.md](weaver-create/Skill.md) - Main skill instructions
   - [weaver-create/REFERENCE.md](weaver-create/REFERENCE.md) - Advanced topics
   - [weaver-create/README.md](weaver-create/README.md) - Overview

2. **Try Creating a Skill**:
   - Ask Claude: "Create a new skill for [your use case]"
   - Follow the guided process
   - Reference the templates in `weaver-create/templates/`

3. **Share with Your Team**:
   - See [SHARING.md](SHARING.md) for distribution methods
   - Share this installation guide
   - Set up plugin marketplace for team distribution

4. **Stay Updated**:
   - Watch the repository for new releases
   - Subscribe to release notifications
   - Check [releases page](https://github.com/flashingcursor/skill-weaver/releases) periodically

---

## Platform Comparison

| Feature | claude.ai | Claude Code |
|---------|-----------|-------------|
| Installation Method | ZIP upload | Plugin, Git, or Manual copy |
| Skill Location | Cloud (Settings > Capabilities) | Filesystem (~/.claude/skills/) |
| Team Sharing | Manual (each person uploads) | Automatic (git or plugin) |
| Updates | Manual re-upload | git pull or plugin update |
| Access Scope | Per-account | Personal or project-specific |
| Offline Use | No (requires internet) | Yes (local files) |

---

**Version**: This guide applies to skill-creator v0.1.0-alpha.4 and later.

**Last Updated**: 2025-11-06
