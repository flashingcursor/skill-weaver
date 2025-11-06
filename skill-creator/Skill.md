---
name: skill-creator
description: Creates custom Skills for Claude following official best practices including proper structure, metadata, progressive disclosure, and security guidelines. Use when creating new skills, building custom workflows, or when user mentions skill creation, skill development, or custom skill authoring.
metadata:
  version: 0.1.0-alpha.4
  dependencies: none
---

# Skill Creator

## Overview
This Skill helps users create Skills for both Claude Code and claude.ai following official best practices. It guides through creating SKILL.md files, structuring directories, adding resources, and ensuring quality.

**What are Skills?**
Skills package expertise into discoverable capabilities. Each Skill consists of a SKILL.md file with instructions that Claude reads when relevant, plus optional supporting files like scripts and templates.

**Model-invoked**: Skills are autonomously triggered by Claude based on your request and the Skill's description. This is different from slash commands (which you explicitly type to trigger).

## Version

**Current Version**: 0.1.0-alpha.4

This is an alpha release. For version history and changelog, see [README.md](README.md#version-history).

## Platform Support

This Skill Creator supports two platforms:

### Claude Code (Agent Skills)
- Filesystem-based storage (`~/.claude/skills/`, `.claude/skills/`)
- Plugin distribution for team sharing
- Tool restrictions via `allowed-tools` field
- Auto-installs dependencies from PyPI/npm
- Debug mode: `claude --debug`

### claude.ai (Custom Skills)
- Upload via Settings > Capabilities (ZIP file)
- Manual distribution (share ZIP files)
- No `allowed-tools` field support
- Can install packages from PyPI/npm when needed
- Review Skill usage in conversation thinking

**Common Features** (both platforms):
- SKILL.md with YAML frontmatter
- Progressive disclosure (metadata → SKILL.md → additional files)
- Same naming conventions and best practices
- Scripts, templates, and resources support

## When to Use This Skill
Use when:
- User asks to create a new Skill
- User wants to build a custom workflow for Claude
- User needs help structuring a Skill directory
- User asks about Skill authoring best practices
- User wants to package, test, or share a Skill

## Core Principles

### Conciseness is Key
The context window is a public good. Your Skill shares it with system prompts, conversation history, other Skills' metadata, and the user's request. Be concise:
- Only include information Claude doesn't already have
- Assume Claude is intelligent and knowledgeable
- Challenge each piece: "Does Claude really need this?"
- Keep Skill.md body under 500 lines
- Move detailed content to REFERENCE.md

**Good (concise):** "Use pdfplumber for PDF text extraction"
**Bad (verbose):** "PDF (Portable Document Format) files are common... you'll need a library... there are many options..."

### Set Appropriate Freedom
Match specificity to task fragility:
- **High freedom** (text instructions): Multiple valid approaches, context-dependent decisions
- **Medium freedom** (pseudocode/parameterized scripts): Preferred pattern with acceptable variation
- **Low freedom** (exact scripts): Fragile operations requiring specific sequences

### Test with All Target Models
Skills affect models differently. Test with Haiku, Sonnet, and Opus. What works for Opus may need more detail for Haiku.

## Skill Creation Process

### Step 1: Determine Platform and Gather Requirements

First, ask which platform(s) the user is targeting:
- **Claude Code only**: Filesystem-based, can use allowed-tools
- **claude.ai only**: ZIP upload, no allowed-tools
- **Both**: Maximum compatibility, skip Claude Code-only features

Then gather requirements:
1. **Platform**: Claude Code, claude.ai, or both?
2. **Purpose**: What specific task should this Skill solve?
3. **Name**: What should it be called? (lowercase-with-hyphens, max 64 chars, use gerund form like "processing-pdfs")
4. **Description**: When should Claude use it? (max 1024 chars, be specific, include triggers)
5. **Scope**: What inputs/outputs are expected?
6. **Tool restrictions** (Claude Code only): Should it limit which tools Claude can use? (allowed-tools field)
7. **Storage location** (Claude Code only): Personal (~/.claude/skills/), Project (.claude/skills/), or Plugin?
8. **Resources**: Will it need reference files, scripts, or external data?
9. **Dependencies**: Does it require specific packages?

### Step 2: Create Directory Structure

**For Claude Code:**

Personal Skills:
```bash
mkdir -p ~/.claude/skills/skill-name
```

Project Skills:
```bash
mkdir -p .claude/skills/skill-name
```

**For claude.ai:**

Create a local directory (will be ZIPped later):
```bash
mkdir -p skill-name
```

**Directory contents (both platforms):**
```
skill-name/
├── SKILL.md           # Required: Main Skill file
├── reference.md       # Optional: Supplemental information
├── examples.md        # Optional: Extended examples
├── templates/         # Optional: Template files
│   └── template.txt
└── scripts/          # Optional: Executable code
    ├── helper.py
    └── validate.py
```

### Step 3: Write the SKILL.md File
The SKILL.md file must include:

#### Required YAML Frontmatter

**For both platforms:**
```yaml
---
name: skill-name
description: What the Skill does and when to use it. Include specific triggers and contexts. Use third person. Max 1024 characters.
metadata:
  version: 1.0.0
  dependencies: package>=version, another-package>=version
---
```

**For Claude Code only (add this field if needed):**
```yaml
allowed-tools: Read, Grep, Glob  # Restrict which tools Claude can use
```

**Platform Compatibility Notes:**

claude.ai has strict frontmatter validation and only accepts these top-level keys: `name`, `description`, `license`, `allowed-tools`, `metadata`. This is why `version` and `dependencies` must be nested under the `metadata` field.

Claude Code is more permissive and will accept the `metadata` field without issues. While Claude Code's documentation shows `version` as a top-level field, using the `metadata` structure ensures your Skill works on both platforms.

**Best Practice for Dual-Platform Support:**
1. Use the `metadata` field format shown above for maximum compatibility
2. Include version information in the markdown body as well (see the Version section)
3. This provides redundancy - version info appears in both frontmatter and documentation
4. Omit the `allowed-tools` field if targeting both platforms (Claude Code only)

**Name requirements (both platforms):**
- Lowercase letters, numbers, and hyphens only
- Max 64 characters
- Use gerund form: "processing-pdfs", "analyzing-data"
- Cannot contain "anthropic" or "claude"

**Description requirements (both platforms):**
- Max 1024 characters
- Third person: "Processes files..." not "I can help..."
- Include what it does AND when to use it
- Mention specific triggers/keywords

**Dependencies handling:**
- **Claude Code**: Auto-installs packages (or asks for permission)
- **claude.ai**: Can install from PyPI/npm when needed
- **Anthropic API**: No network access, pre-installed only
- List packages: `python>=3.8, pandas>=1.5.0, requests>=2.28.0`

**Tool restrictions (allowed-tools) - Claude Code ONLY:**
- Optional field to limit which tools Claude can use when Skill is active
- **Not supported on claude.ai**
- Useful for read-only Skills or security-sensitive workflows
- When specified, Claude can only use listed tools without asking permission
- Example tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch
- Example: `allowed-tools: Read, Grep, Glob` for read-only Skill

#### Markdown Body Structure
```markdown
# Skill Name

## Overview
Brief explanation of what the Skill does and its purpose.

## When to Use This Skill
- Specific scenario 1
- Specific scenario 2
- Specific scenario 3

## Instructions
Clear, step-by-step instructions for Claude to follow.

## Examples
Include example inputs and expected outputs.

## Resources
Reference any additional files in the Skill directory.
```

### Step 4: Add Resources (Optional)
If the Skill requires additional information:
- Create `REFERENCE.md` for supplemental content
- Add example files to `resources/examples/`
- Include templates in `resources/templates/`
- Store data files, logos, or other assets as needed

### Step 5: Add Scripts (Optional)
For advanced Skills that need executable code:
- Add Python scripts (`.py`) for data processing, analysis, or automation
- Add JavaScript scripts (`.js`) for web-related tasks
- Document all required dependencies in the frontmatter
- Include usage examples in the Skill.md file

**Supported languages:**
- Python (with pandas, numpy, matplotlib, etc.)
- JavaScript/Node.js (with standard npm packages)

**Note:** Claude and Claude Code can install packages from standard repositories when loading Skills.

### Step 6: Package and Share the Skill

#### For claude.ai (ZIP Upload)

**Create ZIP file:**
```bash
# From parent directory
zip -r skill-name.zip skill-name/

# Verify structure
unzip -l skill-name.zip
```

**Expected structure:**
```
skill-name.zip
  └── skill-name/
      ├── SKILL.md
      ├── reference.md
      └── scripts/
```

**Share with users:**
1. Users navigate to Settings > Capabilities
2. Upload the ZIP file
3. Enable the Skill
4. Start using it

**Team distribution:**
- Share ZIP file via email, file sharing, or git repository
- Users manually upload to their claude.ai account

#### For Claude Code

**Recommended: Share via Plugin**
Best for team distribution:
1. Create a plugin with Skills in the `skills/` directory
2. Publish to a marketplace
3. Team members install the plugin
4. Skills automatically available

**Alternative: Share via Git (Project Skills)**
For project-specific Skills:
1. Place Skill in `.claude/skills/skill-name/`
2. Commit to git: `git add .claude/skills/ && git commit -m "Add skill"`
3. Team members get Skills automatically: `git pull`

**Personal Skills:**
- Stay local: `~/.claude/skills/`
- Not shared automatically
- Use for individual workflows

#### For Both Platforms

If targeting both, provide:
1. ZIP file for claude.ai users
2. Plugin or git instructions for Claude Code users
3. Omit Claude Code-only features (like `allowed-tools`)

### Step 7: Test the Skill

#### Testing on Both Platforms

**Test with matching requests:**
Skills are autonomously invoked—Claude decides when to use them based on the description.

Ask questions that match your description:
```
# If description mentions "PDF files"
"Can you help me extract text from this PDF?"

# Claude automatically uses your Skill if it matches
```

**Verify Skill is loaded:**
Ask Claude: `"What Skills are available?"`

#### Platform-Specific Testing

**For claude.ai:**
1. **Upload Skill**: Settings > Capabilities > Upload ZIP
2. **Enable Skill**: Toggle it on in Capabilities
3. **Test invocation**: Ask relevant questions
4. **Review thinking**: Check if Skill was considered and why/why not
5. **Iterate description**: Update if Skill not triggering correctly

**For Claude Code:**
1. **Verify file location**:
   ```bash
   ls ~/.claude/skills/skill-name/SKILL.md  # Personal
   ls .claude/skills/skill-name/SKILL.md   # Project
   ```
2. **Restart Claude Code**: Required for changes to take effect
3. **Test invocation**: Ask relevant questions
4. **Debug if needed**: Run `claude --debug` to see loading errors
5. **Check YAML syntax**: Validate frontmatter format

**Common Debugging Steps:**
1. **Check description specificity**: Too vague? Add specific triggers
2. **Verify YAML syntax**: Must start/end with `---`, no tabs
3. **Test with exact keywords**: Use terms from your description
4. **Review Skill name**: Must be lowercase-with-hyphens
5. **Check dependencies**: Listed correctly in frontmatter?

## Best Practices

For comprehensive details, see [REFERENCE.md](REFERENCE.md).

### Naming Conventions
Use consistent patterns:
- **Gerund form** (recommended): "processing-pdfs", "analyzing-data"
- Must be lowercase-with-hyphens
- Max 64 characters
- No "anthropic" or "claude"

### Description Effectiveness
- **Always third person**: "Processes files..." not "I help..."
- **Be specific**: Include both what it does AND when to use it
- **Add triggers**: Mention keywords that should activate it
- **Example**: "Extracts text from PDF files using pdfplumber. Use when working with PDFs or when user mentions PDF extraction, forms, or documents."

### Progressive Disclosure
Claude loads information in stages:
1. **Metadata** (always loaded): name, description
2. **Skill.md body** (when Skill used): core instructions
3. **REFERENCE.md** (on-demand): detailed specs, edge cases
4. **Other files** (as needed): templates, data, scripts

Keep Skill.md under 500 lines. Move details to separate files.

### Workflow Patterns
For multi-step tasks, provide checklists:

```markdown
## Task workflow

Copy this checklist:
```
Progress:
- [ ] Step 1: Analyze input
- [ ] Step 2: Process data
- [ ] Step 3: Validate output
- [ ] Step 4: Generate report
```

**Step 1: Analyze input**
[Detailed instructions...]
```

### Feedback Loops
Add validation cycles for quality:

```markdown
1. Make changes
2. Run validation: `python validate.py`
3. If validation fails:
   - Review errors
   - Fix issues
   - Run validation again
4. Only proceed when validation passes
```

### Common Patterns

**Template pattern** - Provide output format:
```markdown
ALWAYS use this exact structure:
[template here]
```

**Examples pattern** - Show input/output pairs:
```markdown
Example 1:
Input: [specific input]
Output: [expected output]
```

**Conditional workflow** - Guide decisions:
```markdown
1. Determine type:
   **Creating new?** → Follow creation workflow
   **Editing existing?** → Follow editing workflow
```

### Avoid Anti-Patterns
- ❌ Windows paths (`\`): Use forward slashes (`/`) always
- ❌ Too many options: Provide default with escape hatch
- ❌ Vague terms: Be specific and concrete
- ❌ Time-sensitive info: Use "old patterns" section instead
- ❌ Inconsistent terminology: Pick one term and stick to it
- ❌ Deeply nested references: Keep references one level deep from Skill.md

## Example Skill Patterns

### Simple Skill (commit message helper)
```yaml
---
name: generating-commit-messages
description: Generates clear commit messages from git diffs. Use when writing commit messages or reviewing staged changes.
---

# Generating Commit Messages

## Instructions
1. Run `git diff --staged` to see changes
2. Suggest a commit message with:
   - Summary under 50 characters
   - Detailed description
   - Affected components
```

### Read-Only Skill (code reviewer)
```yaml
---
name: code-reviewer
description: Review code for best practices and potential issues. Use when reviewing code, checking PRs, or analyzing code quality.
allowed-tools: Read, Grep, Glob  # Restrict to read-only operations
---

# Code Reviewer

## Instructions
1. Read target files using Read tool
2. Search for patterns using Grep
3. Find related files using Glob
4. Provide detailed feedback on code quality
```

### Multi-File Skill (PDF processing)
```
pdf-processing/
├── SKILL.md
├── forms.md          # Form-filling guide (loaded on-demand)
├── reference.md      # API reference (loaded as needed)
└── scripts/
    ├── fill_form.py
    └── validate.py
```

```yaml
---
name: pdf-processing
description: Extract text, fill forms, merge PDFs. Use when working with PDF files, forms, or document extraction.
metadata:
  dependencies: pypdf>=3.0.0, pdfplumber>=0.9.0
---

# PDF Processing

## Quick start
For form filling, see [forms.md](forms.md).
For API reference, see [reference.md](reference.md).
```

## Security Considerations
When adding scripts to Skills:
- ⚠️ **Never hardcode sensitive information** (API keys, passwords)
- Use appropriate MCP connections for external service access
- Validate inputs in scripts
- Follow principle of least privilege
- Document security requirements
- Use **allowed-tools** to restrict capabilities when appropriate

## Templates

### Basic Skill Template
See `templates/basic-skill-template.md` for a minimal Skill structure suitable for simple instruction-based Skills.

### Advanced Skill Template
See `templates/advanced-skill-template.md` for a complete Skill structure with resources and scripts.

## Example Skills
For reference implementations, see:
- GitHub repository: https://github.com/anthropics/skills
- Claude Docs: Skill authoring best practices

## Troubleshooting

### Claude isn't invoking the Skill
- Check the description is specific and clear
- Verify the Skill is enabled in Settings
- Review Claude's thinking to see why it wasn't selected
- Make the description more specific about triggering scenarios

### Skill loads but doesn't work as expected
- Review instructions for clarity
- Add more examples
- Check that referenced files exist
- Verify script dependencies are correctly specified

### Scripts aren't running
- Confirm dependencies are listed in frontmatter
- Check script syntax and permissions
- Verify file paths are correct
- Test scripts independently first

## Output Format
When creating a Skill, provide:
1. The complete directory structure
2. Full Skill.md file with frontmatter
3. Any template or resource files
4. Instructions for testing
5. Suggested prompts to trigger the Skill
