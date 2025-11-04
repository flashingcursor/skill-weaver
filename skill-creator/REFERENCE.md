# Skill Creator - Technical Reference

This document provides detailed technical information for creating Custom Skills. It's referenced from Skill.md but contains supplemental details that aren't needed for every skill creation task.

## YAML Frontmatter Specification

### Required Fields

#### name
- **Type**: String
- **Max length**: 64 characters
- **Format**: Human-readable display name
- **Examples**:
  - ✅ "Brand Guidelines"
  - ✅ "Data Analysis Pipeline"
  - ❌ "BrandGuidelinesForMarketingTeamAndSalesTeamAndEveryoneElse" (too long)

#### description
- **Type**: String
- **Max length**: 200 characters
- **Purpose**: Claude uses this to determine when to invoke the skill
- **Format**: Clear, specific statement of when to use the skill
- **Best practices**:
  - Use action verbs
  - Be specific about scenarios
  - Mention key domains or contexts
  - Avoid vague terms
- **Examples**:
  - ✅ "Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage"
  - ✅ "Process CSV data files to generate statistical reports with visualizations and export to multiple formats"
  - ❌ "Helps with stuff" (too vague)
  - ❌ "Use this skill when you need to do things related to our company brand and maybe some other related tasks" (too long, unfocused)

### Optional Fields

#### version
- **Type**: String
- **Format**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Example**: "1.0.0", "2.1.3"
- **Recommendation**: Always include for tracking changes

#### dependencies
- **Type**: String (comma-separated list)
- **Format**: `package>=version, another-package>=version`
- **Examples**:
  - Python: `python>=3.8, pandas>=1.5.0, numpy>=1.21.0`
  - JavaScript: `node>=16.0.0, axios>=1.0.0`
- **Notes**:
  - Claude/Claude Code can install from PyPI and npm
  - API Skills require pre-installed dependencies

## File Naming Conventions

### Skill Directory
- **Format**: lowercase-with-hyphens
- **Match**: Should match the skill name (normalized)
- **Examples**:
  - Skill name: "Brand Guidelines" → Directory: `brand-guidelines`
  - Skill name: "Data Analysis" → Directory: `data-analysis`

### Required Files
- `Skill.md` - Exact capitalization, always required

### Optional Files
- `REFERENCE.md` - Uppercase, for supplemental information
- `README.md` - Uppercase, for documentation
- `resources/` - Lowercase directory for assets
- `scripts/` - Lowercase directory for executable code

## Progressive Disclosure System

Claude loads skill information in stages:

### Stage 1: Metadata (Always Loaded)
```yaml
name: Brand Guidelines
description: Apply brand guidelines to documents
```
- Loaded for all skills
- Used to decide if skill is relevant
- Keep minimal and focused

### Stage 2: Skill.md Body (Loaded When Skill Used)
- Core instructions and workflows
- Essential examples
- Key guidelines
- When to use this skill

### Stage 3: REFERENCE.md (Loaded On-Demand)
- Detailed technical specifications
- Edge cases and advanced scenarios
- Comprehensive API documentation
- Historical context

### Stage 4: Resources (Loaded As Needed)
- Example files
- Templates
- Data files
- Images and assets

**Why This Matters:**
- Faster skill loading
- Lower token usage
- Better performance
- More maintainable

## Script Integration Patterns

### Python Scripts

#### Basic Pattern
```python
#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    # Your logic here

    return 0

if __name__ == '__main__':
    sys.exit(main())
```

#### With Dependencies
```yaml
# In Skill.md frontmatter
dependencies: python>=3.8, pandas>=1.5.0, requests>=2.28.0
```

```python
# In script
import pandas as pd
import requests
```

#### Error Handling
```python
try:
    # Operations
    result = process_data(input_data)
except FileNotFoundError as e:
    print(f"Error: {e}", file=sys.stderr)
    return 1
except ValueError as e:
    print(f"Invalid data: {e}", file=sys.stderr)
    return 2
```

### JavaScript Scripts

#### Basic Pattern
```javascript
#!/usr/bin/env node
const fs = require('fs').promises;

async function main() {
    const args = process.argv.slice(2);
    // Parse args and process

    try {
        // Your logic here
        process.exit(0);
    } catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
}

main().catch(error => {
    console.error(error);
    process.exit(1);
});
```

#### With Dependencies
```yaml
# In Skill.md frontmatter
dependencies: node>=16.0.0, axios>=1.0.0, cheerio>=1.0.0
```

```javascript
// In script
const axios = require('axios');
const cheerio = require('cheerio');
```

## Resource Organization Patterns

### Small Skills (< 5 files)
```
skill-name/
├── Skill.md
└── resources/
    └── examples/
        ├── example-1.txt
        └── example-2.txt
```

### Medium Skills (5-15 files)
```
skill-name/
├── Skill.md
├── REFERENCE.md
├── resources/
│   ├── examples/
│   ├── templates/
│   └── data/
└── scripts/
    └── process.py
```

### Large Skills (15+ files)
```
skill-name/
├── Skill.md
├── REFERENCE.md
├── README.md
├── resources/
│   ├── examples/
│   │   ├── basic/
│   │   └── advanced/
│   ├── templates/
│   │   ├── minimal.md
│   │   └── complete.md
│   └── data/
│       ├── reference.json
│       └── lookup.csv
└── scripts/
    ├── __init__.py
    ├── process.py
    ├── validate.py
    └── utils.py
```

## Testing Strategies

### Unit Testing (Before Upload)
1. **Syntax Validation**
   - YAML frontmatter is valid
   - All referenced files exist
   - Scripts have correct shebang
   - Scripts are executable

2. **Content Validation**
   - Description is specific and clear
   - Instructions are actionable
   - Examples are complete
   - No hardcoded secrets

3. **Script Testing**
   ```bash
   # Test Python script
   python scripts/process.py --help
   python scripts/process.py --input test.json --output result.json

   # Test JavaScript script
   node scripts/process.js --help
   node scripts/process.js --input test.json --output result.json
   ```

### Integration Testing (After Upload)
1. **Invocation Testing**
   - Try prompts that should trigger the skill
   - Try prompts that shouldn't trigger it
   - Verify Claude loads the skill when expected

2. **Execution Testing**
   - Test with typical inputs
   - Test with edge cases
   - Test with invalid inputs
   - Verify error handling

3. **Thinking Analysis**
   - Review Claude's reasoning
   - Check if skill was considered
   - Verify why it was/wasn't used
   - Refine description if needed

## Common Patterns and Anti-Patterns

### ✅ Good Patterns

#### Focused Skills
```yaml
# Good: One clear purpose
name: CSV Data Validator
description: Validate CSV files against schema and data quality rules
```

#### Clear Instructions
```markdown
## Instructions
1. Load the CSV file using pandas
2. Check column names match schema
3. Validate data types for each column
4. Report any validation errors
```

#### Helpful Examples
```markdown
## Examples
### Example 1: Valid File
Input: users.csv with columns: id, name, email
Output: "✓ All validations passed. 150 rows processed."

### Example 2: Invalid File
Input: users.csv missing 'email' column
Output: "✗ Validation failed: Missing required column 'email'"
```

### ❌ Anti-Patterns

#### Unfocused Skills
```yaml
# Bad: Tries to do too much
name: Data Management
description: Handles all data tasks including validation, processing, reporting, and visualization
```

#### Vague Instructions
```markdown
## Instructions
1. Do the thing with the data
2. Make it work properly
3. Output the results
```

#### Missing Examples
```markdown
## Examples
(No examples provided)
```

## Packaging Checklist

Before creating the ZIP file:

- [ ] Directory name matches skill name (normalized)
- [ ] Skill.md exists with valid YAML frontmatter
- [ ] Name is ≤ 64 characters
- [ ] Description is ≤ 200 characters
- [ ] All referenced files exist at correct paths
- [ ] Scripts have proper shebangs
- [ ] No hardcoded secrets
- [ ] Dependencies are listed in frontmatter
- [ ] Examples are complete and accurate
- [ ] README.md exists (recommended)
- [ ] Version is specified

Creating the ZIP:
```bash
# From parent directory
zip -r skill-name.zip skill-name/

# Verify structure
unzip -l skill-name.zip
```

Expected output:
```
skill-name/Skill.md
skill-name/README.md
skill-name/resources/...
skill-name/scripts/...
```

## Troubleshooting Guide

### Skill Not Being Invoked

**Symptom**: Claude doesn't use the skill when expected

**Diagnosis**:
1. Check Claude's thinking for why skill wasn't selected
2. Review description for specificity
3. Verify skill is enabled in Settings

**Solutions**:
- Make description more specific
- Add more trigger scenarios
- Reduce description to focus on primary use case
- Test with exact phrases from description

### Skill Loads But Doesn't Work

**Symptom**: Skill is invoked but doesn't produce correct results

**Diagnosis**:
1. Review instructions for clarity
2. Check examples are accurate
3. Verify file paths in references

**Solutions**:
- Add more detailed step-by-step instructions
- Include more examples covering edge cases
- Clarify expected inputs/outputs
- Add error handling guidance

### Scripts Won't Execute

**Symptom**: Scripts fail when Claude tries to run them

**Diagnosis**:
1. Check dependencies are listed in frontmatter
2. Verify script has correct shebang
3. Test script independently
4. Review error messages

**Solutions**:
- Add missing dependencies to frontmatter
- Fix script syntax errors
- Ensure file paths are correct
- Add better error messages in script

### Performance Issues

**Symptom**: Skill loads slowly or uses too many tokens

**Diagnosis**:
1. Check Skill.md size
2. Review how much content is in main file vs REFERENCE.md
3. Check if all content is necessary

**Solutions**:
- Move detailed content to REFERENCE.md
- Split large skills into multiple focused skills
- Remove redundant information
- Optimize examples to be concise

## Version Control Best Practices

### Semantic Versioning
- **MAJOR** (1.0.0 → 2.0.0): Breaking changes, incompatible updates
- **MINOR** (1.0.0 → 1.1.0): New features, backward compatible
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, minor improvements

### Documenting Changes
Keep a changelog in README.md:
```markdown
## Version History
- **1.2.0**: Added support for XML input format
- **1.1.1**: Fixed bug in date parsing
- **1.1.0**: Added validation for email fields
- **1.0.0**: Initial release
```

### Testing After Updates
When updating a skill:
1. Test that existing functionality still works
2. Test new features thoroughly
3. Verify description still accurately reflects behavior
4. Update examples if behavior changed
5. Bump version number appropriately

## Advanced Techniques

### Skill Composition
Skills can work together automatically. Design skills to complement each other:

**Example: Data Workflow**
- Skill 1: "CSV Validator" - Validates input data
- Skill 2: "Data Analyzer" - Analyzes valid data
- Skill 3: "Report Generator" - Creates reports from analysis

Claude can chain these together automatically when the user asks for a complete workflow.

### Conditional Logic
Use clear conditional instructions:
```markdown
## Instructions
1. Check the input format:
   - If CSV: Use pandas to read
   - If JSON: Use json module
   - If XML: Use xml.etree.ElementTree

2. If data size > 10MB:
   - Process in chunks
   - Show progress updates

3. If errors found:
   - Log to error file
   - Continue processing remaining data
```

### Context Awareness
Help Claude understand context:
```markdown
## When to Use This Skill
- When user mentions "sales data" or "revenue reports"
- When user provides CSV files with sales metrics
- When user asks to "analyze sales performance"
- NOT for marketing data (use Marketing Analytics skill instead)
```

## Security Deep Dive

### Secret Management
Never hardcode secrets. Instead:

**Bad:**
```python
API_KEY = "sk-1234567890abcdef"  # NEVER DO THIS
```

**Good:**
```python
import os
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

**Better:**
Use MCP connections for external services.

### Input Validation
Always validate user inputs:

```python
def validate_input(data):
    # Check type
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")

    # Check required fields
    required = ['name', 'email']
    for field in required:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Sanitize strings
    data['name'] = data['name'].strip()[:100]

    return data
```

### File Operations
Be careful with file paths:

```python
from pathlib import Path

def safe_file_read(filepath):
    # Convert to Path object
    path = Path(filepath).resolve()

    # Check path is within expected directory
    base_dir = Path('/allowed/directory').resolve()
    if not path.is_relative_to(base_dir):
        raise ValueError("Access denied: Path outside allowed directory")

    # Verify file exists and is readable
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {filepath}")

    return path.read_text()
```

## Performance Optimization

### Token Efficiency
- Keep Skill.md focused and concise
- Move detailed specs to REFERENCE.md
- Use clear, direct language
- Avoid repetition

### Loading Speed
- Minimize file size where possible
- Structure content hierarchically
- Use progressive disclosure
- Reference external files only when needed

### Script Performance
- Cache expensive operations
- Process data in chunks for large files
- Use efficient libraries (pandas, numpy)
- Add progress indicators for long operations

## Support and Resources

- **Official Documentation**: https://docs.claude.com/claude/docs/skills
- **Example Skills**: https://github.com/anthropics/skills
- **Best Practices Guide**: https://docs.claude.com/claude/docs/skill-authoring-best-practices
- **Community Forum**: Check Anthropic's community resources

## Glossary

**Frontmatter**: YAML metadata at the start of Skill.md

**Progressive Disclosure**: Loading information in stages as needed

**Skill Composition**: Multiple skills working together automatically

**MCP**: Model Context Protocol for external service integration

**Semantic Versioning**: Version numbering scheme (MAJOR.MINOR.PATCH)

**Token**: Unit of text processed by Claude (affects performance and cost)
