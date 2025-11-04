---
name: skill-creator
description: Creates custom Skills for Claude following official best practices including proper structure, metadata, progressive disclosure, and security guidelines. Use when creating new skills, building custom workflows, or when user mentions skill creation, skill development, or custom skill authoring.
version: 1.0.0
dependencies: none
---

# Skill Creator

## Overview
This Skill helps users create new custom Skills for Claude following official best practices. It guides through creating Skill.md files, structuring directories, adding resources, and ensuring quality.

## When to Use This Skill
Use when:
- User asks to create a new Skill
- User wants to build a custom workflow for Claude
- User needs help structuring a Skill directory
- User asks about Skill authoring best practices
- User wants to package or test a Skill

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

### Step 1: Gather Requirements
Ask about:
1. **Purpose**: What specific task should this Skill solve?
2. **Name**: What should it be called? (lowercase-with-hyphens, max 64 chars, use gerund form like "processing-pdfs")
3. **Description**: When should Claude use it? (max 1024 chars, be specific, include triggers)
4. **Scope**: What inputs/outputs are expected?
5. **Resources**: Will it need reference files, scripts, or external data?
6. **Dependencies**: Does it require specific packages?

### Step 2: Create Directory Structure
Create a directory with the Skill name containing:
```
skill-name/
├── Skill.md           # Required: Main Skill file
├── REFERENCE.md       # Optional: Supplemental information
├── resources/         # Optional: Reference files
│   ├── examples/
│   └── templates/
└── scripts/          # Optional: Executable code
    ├── script.py
    └── script.js
```

### Step 3: Write the Skill.md File
The Skill.md file must include:

#### Required YAML Frontmatter
```yaml
---
name: skill-name
description: What the Skill does and when to use it. Include specific triggers and contexts. Use third person. Max 1024 characters.
version: 1.0.0
dependencies: package>=version, another-package>=version
---
```

**Name requirements:**
- Lowercase letters, numbers, and hyphens only
- Max 64 characters
- Use gerund form: "processing-pdfs", "analyzing-data"
- Cannot contain "anthropic" or "claude"

**Description requirements:**
- Max 1024 characters
- Third person: "Processes files..." not "I can help..."
- Include what it does AND when to use it
- Mention specific triggers/keywords

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

### Step 6: Package the Skill
To share or upload the Skill:
1. Ensure the folder name matches the Skill name
2. Create a ZIP file of the folder
3. The ZIP should contain the Skill folder as its root

**Correct structure:**
```
my-skill.zip
  └── my-skill/
      ├── Skill.md
      └── resources/
```

**Incorrect structure:**
```
my-skill.zip
  └── Skill.md (files directly in ZIP root - WRONG)
```

### Step 7: Testing
Before finalizing:
1. Review Skill.md for clarity and completeness
2. Verify the description accurately reflects when Claude should use the Skill
3. Check all referenced files exist in correct locations
4. Test with example prompts to ensure proper invocation

After uploading to Claude:
1. Enable the Skill in Settings > Capabilities
2. Try various prompts that should trigger it
3. Review Claude's thinking to confirm it loads correctly
4. Iterate on the description if Claude doesn't use it as expected

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

## Security Considerations
When adding scripts to Skills:
- ⚠️ **Never hardcode sensitive information** (API keys, passwords)
- Use appropriate MCP connections for external service access
- Validate inputs in scripts
- Follow principle of least privilege
- Document security requirements

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
