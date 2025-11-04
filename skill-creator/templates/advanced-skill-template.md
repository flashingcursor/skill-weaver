---
name: Your Advanced Skill Name
description: Brief description of what this Skill does and when Claude should use it
version: 1.0.0
dependencies: python>=3.8, pandas>=1.5.0, requests>=2.28.0
---

# Your Advanced Skill Name

## Overview
Detailed explanation of what this Skill does, its purpose, and the problems it solves.

## When to Use This Skill
- Scenario 1: When the user needs [specific complex task]
- Scenario 2: When processing [specific data types]
- Scenario 3: When integrating with [specific systems]
- Scenario 4: When asked to [specific action]

## Prerequisites
List any setup requirements:
- Required software or tools
- API keys or credentials (via MCP, never hardcoded)
- Expected file formats or structures
- Environmental setup

## Instructions

### Phase 1: Preparation
1. Validate inputs meet required format
2. Check dependencies are available
3. Load necessary resources

### Phase 2: Processing
1. Execute main workflow steps
2. Handle errors gracefully
3. Log progress and results

### Phase 3: Output
1. Format results appropriately
2. Provide summary of actions taken
3. Suggest next steps if applicable

## Scripts

### script_name.py
Located in `scripts/script_name.py`, this script:
- Purpose: What it does
- Inputs: What it expects
- Outputs: What it produces
- Usage: `python scripts/script_name.py --input data.csv --output results.json`

Example:
```python
# See scripts/script_name.py for full implementation
# Usage: python scripts/script_name.py --arg1 value1 --arg2 value2
```

### another_script.js
Located in `scripts/another_script.js`, this script:
- Purpose: What it does
- Inputs: What it expects
- Outputs: What it produces
- Usage: `node scripts/another_script.js input.json`

## Resources

### Reference Files
- `REFERENCE.md`: Detailed technical specifications
- `resources/examples/`: Sample inputs and outputs
- `resources/templates/`: Templates for common use cases
- `resources/data/`: Reference data files

### External Resources
- Documentation: [Link to relevant docs]
- API Reference: [Link to API docs]
- Related tools: [Link to related resources]

## Guidelines

### Quality Standards
- Output must meet [specific criteria]
- Follow [specific style guide]
- Validate results against [specific requirements]

### Error Handling
- If [condition], do [action]
- For errors in [scenario], [fallback approach]
- Always provide clear error messages

### Performance Considerations
- Optimize for [specific metric]
- Cache [specific data] when possible
- Limit [resource] usage to [threshold]

## Examples

### Example 1: Basic Usage
**Input:**
```
User request: "..."
Data: {...}
```

**Process:**
1. Step by step what happens
2. Including any script calls
3. And resource references

**Output:**
```
Expected result format
```

### Example 2: Advanced Usage
**Input:**
```
Complex scenario description
Multiple data sources
```

**Process:**
1. How this case is handled differently
2. Which scripts are invoked
3. How resources are utilized

**Output:**
```
Expected comprehensive result
```

### Example 3: Edge Case
**Input:**
```
Edge case scenario
```

**Handling:**
- How this is detected
- Special processing applied
- Expected behavior

## Troubleshooting

### Common Issues

#### Issue 1: [Problem description]
**Symptoms:** What the user sees
**Cause:** Why this happens
**Solution:** How to fix it

#### Issue 2: [Problem description]
**Symptoms:** What the user sees
**Cause:** Why this happens
**Solution:** How to fix it

## Security Considerations
- Never hardcode sensitive data
- Use MCP connections for external services
- Validate all user inputs
- Sanitize outputs
- Follow principle of least privilege

## Version History
- **1.0.0**: Initial release with [features]

## Notes
Additional context, tips, or advanced usage patterns.
