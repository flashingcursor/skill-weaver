# Skill Creator - Custom Skill for Creating Skills

A meta-skill that helps you create new Custom Skills for Claude following best practices and proper structure.

## Overview

The Skill Creator guides you through the entire process of building a Custom Skill, from initial planning to final packaging. It ensures your skills follow the correct structure, include proper metadata, and adhere to best practices.

## What This Skill Does

When activated, Skill Creator will:

1. **Gather Requirements**: Ask about your skill's purpose, scope, and needs
2. **Create Structure**: Set up the proper directory and file organization
3. **Generate Files**: Create Skill.md with correct YAML frontmatter and content
4. **Add Templates**: Provide starter templates for resources and scripts
5. **Guide Testing**: Help you test and validate your new skill
6. **Provide Best Practices**: Ensure your skill follows recommended patterns

## When to Use

Use this skill when you want to:
- Create a new Custom Skill from scratch
- Build a specialized workflow for Claude
- Package organizational knowledge or guidelines
- Automate repetitive tasks with scripts
- Structure complex instructions for Claude

## Quick Start

Simply ask Claude to create a skill:
```
"Create a new skill for [your purpose]"
"Help me build a skill that does [task]"
"I need a custom skill for [workflow]"
```

## Templates Included

This skill includes several templates to help you get started:

### 1. Basic Skill Template (`templates/basic-skill-template.md`)
Use for simple, instruction-based skills that don't need resources or scripts.

**Best for:**
- Style guides and guidelines
- Simple workflows
- Question-answering skills
- Documentation helpers

### 2. Advanced Skill Template (`templates/advanced-skill-template.md`)
Use for complex skills with resources, scripts, and multiple components.

**Best for:**
- Data processing workflows
- Multi-step automation
- Skills requiring external resources
- Complex integrations

### 3. Example Python Script (`templates/example-script.py`)
Template for Python scripts with proper error handling and argument parsing.

**Best for:**
- Data analysis
- File processing
- API interactions
- Mathematical computations

### 4. Example JavaScript Script (`templates/example-script.js`)
Template for Node.js scripts with async/await patterns.

**Best for:**
- JSON processing
- Web scraping
- File transformations
- Modern async workflows

## Directory Structure

```
skill-creator/
├── Skill.md                    # Main skill file
├── README.md                   # This file
└── templates/
    ├── basic-skill-template.md      # Simple skill template
    ├── advanced-skill-template.md   # Complex skill template
    ├── example-script.py            # Python script template
    └── example-script.js            # JavaScript script template
```

## Key Features

### Progressive Disclosure
The skill teaches Claude's progressive disclosure system:
- Metadata (always loaded)
- Skill.md core content (loaded when skill is used)
- REFERENCE.md (loaded only if needed)
- Additional resources (loaded on-demand)

### Best Practices Enforcement
Ensures your skills follow:
- Focused, single-purpose design
- Clear, specific descriptions
- Proper version control
- Security considerations
- Composability with other skills

### Complete Guidance
Covers all aspects:
- YAML frontmatter requirements
- Markdown structure
- Resource organization
- Script integration
- Testing procedures
- Packaging for distribution

## Example Usage

### Creating a Simple Skill
```
User: "Create a skill for applying our company's coding standards"

Skill Creator will:
1. Ask about your coding standards
2. Create a focused skill directory
3. Generate Skill.md with your guidelines
4. Provide testing instructions
```

### Creating an Advanced Skill
```
User: "Build a skill that processes CSV data and generates reports"

Skill Creator will:
1. Gather requirements about data format and report types
2. Set up directory with scripts folder
3. Create Skill.md with proper dependencies
4. Add Python script template for processing
5. Include example inputs/outputs
6. Guide testing and validation
```

## Testing Your New Skill

After creating a skill:

1. **Review Structure**: Verify all files are in place
2. **Check Metadata**: Ensure description is clear and specific
3. **Validate References**: Confirm all file paths are correct
4. **Test Prompts**: Try various prompts that should trigger it
5. **Iterate**: Refine based on how Claude responds

## Tips for Success

### Write Clear Descriptions
The description field is crucial - Claude uses it to decide when to invoke your skill.

**Good:** "Apply Acme Corp brand guidelines to presentations and documents"
**Bad:** "Helps with branding stuff"

### Keep Skills Focused
One skill = one workflow. Create multiple skills instead of one mega-skill.

**Good:** Separate skills for "Generate Reports" and "Validate Data"
**Bad:** One "Data Management" skill that does everything

### Start Simple, Iterate
Begin with basic Markdown instructions. Add complexity only when needed.

1. Start: Basic Skill.md with instructions
2. Add: Example files in resources folder
3. Expand: Scripts for automation
4. Refine: Based on testing and use

### Use Examples Liberally
Examples help Claude understand what success looks like.

Include:
- Example inputs
- Expected outputs
- Edge cases
- Common variations

## Security Reminders

When creating skills with scripts:

⚠️ **Never** hardcode API keys or passwords
⚠️ **Always** use MCP connections for external services
⚠️ **Validate** all inputs in scripts
⚠️ **Document** security requirements

## Version History

- **1.0.0**: Initial release of Skill Creator

## Resources

- [Official Skills Documentation](https://docs.claude.com/claude/docs/skills)
- [Example Skills Repository](https://github.com/anthropics/skills)
- [Skill Authoring Best Practices](https://docs.claude.com/claude/docs/skill-authoring-best-practices)

## Contributing

To improve this skill:
1. Test with various skill creation scenarios
2. Add more template examples
3. Enhance error handling guidance
4. Expand troubleshooting section

## License

This skill is provided as an example and template for creating Custom Skills for Claude.
