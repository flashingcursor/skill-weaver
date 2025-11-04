---
name: your-skill-name
description: Brief description of what this Skill does and when Claude should use it. Include specific triggers and keywords. Use third person. Max 1024 characters. Example - "Processes CSV files and generates reports. Use when analyzing data, working with spreadsheets, or when user mentions CSV, data analysis, or reports."
version: 1.0.0
---

# IMPORTANT: Name must use lowercase-with-hyphens, max 64 chars, gerund form preferred
# IMPORTANT: Description must be specific, include triggers, use third person, max 1024 chars

# Your Skill Name

## Overview
Explain what this Skill does and its purpose. Be concise—assume Claude is intelligent. Only include information Claude doesn't already have.

## When to Use This Skill
Be specific about triggers and contexts:
- When user mentions [specific keywords]
- When working with [specific file types or contexts]
- When asked about [specific topic or action]

## Instructions
Provide clear instructions. Match detail level to task fragility:
- **High freedom**: Multiple valid approaches → General guidance
- **Low freedom**: Fragile operations → Specific steps

1. **Step 1**: Do this first
2. **Step 2**: Then do this
3. **Step 3**: Finally do this

**For complex workflows, add a checklist:**
```
Progress:
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3
```

## Guidelines
Any specific rules or guidelines Claude should follow:
- Guideline 1
- Guideline 2
- Guideline 3

## Examples

Show concrete examples with actual input/output pairs:

### Example 1: Basic Case
**Input:** User asks: "..."
**Output:**
```
Claude should respond with: "..."
```

### Example 2: Variation
**Input:** User provides: "..."
**Output:**
```
Claude should: "..."
```

## Best Practices Checklist
Before publishing this Skill:
- [ ] Name uses lowercase-with-hyphens (max 64 chars)
- [ ] Description includes what it does AND when to use it (max 1024 chars)
- [ ] Description written in third person
- [ ] Skill.md body under 500 lines
- [ ] Examples are concrete, not abstract
- [ ] Consistent terminology throughout
- [ ] No Windows-style paths (use forward slashes)
- [ ] No time-sensitive information
- [ ] Tested with target models (Haiku, Sonnet, Opus)

## Notes
Additional context. Keep concise—only what Claude doesn't already know.
