# Sharing Guide

This guide helps you distribute the **skill-creator** skill to your team, organization, or the public.

## Table of Contents

- [Quick Start](#quick-start)
- [Sharing Methods](#sharing-methods)
  - [claude.ai Distribution](#claudeai-distribution)
  - [Claude Code Distribution](#claude-code-distribution)
- [Team Rollout Guide](#team-rollout-guide)
- [Sharing Templates](#sharing-templates)
- [Best Practices](#best-practices)

---

## Quick Start

Choose your distribution method based on your platform and team size:

| Platform | Team Size | Recommended Method |
|----------|-----------|-------------------|
| claude.ai | 1-10 | Share release URL |
| claude.ai | 10-50 | Internal documentation + ZIP |
| claude.ai | 50+ | Automated onboarding + support |
| Claude Code | 1-5 | Git repository (project skills) |
| Claude Code | 5-20 | Plugin marketplace |
| Claude Code | 20+ | Plugin + automated setup |
| Both | Any | Multiple methods + documentation |

---

## Sharing Methods

### claude.ai Distribution

#### Method 1: Share Release URL (Simplest)

**Best for**: Small teams, quick sharing

**Steps**:

1. **Get the latest release URL**:
   ```
   https://github.com/flashingcursor/skill-weaver/releases/latest
   ```

2. **Share with your team** via:
   - Email
   - Slack/Teams message
   - Internal wiki
   - Team chat

3. **Provide these instructions**:
   ```
   📥 Install skill-creator:

   1. Download: https://github.com/flashingcursor/skill-weaver/releases/latest
   2. Go to claude.ai → Settings → Capabilities → Skills
   3. Click "Upload skill" and select the ZIP file
   4. Enable the skill
   5. Test: "Create a skill for code reviews"

   Questions? See: https://github.com/flashingcursor/skill-weaver/blob/master/INSTALLATION.md
   ```

**Time Investment**: 5 minutes setup, 2 minutes per person

---

#### Method 2: Internal Documentation (Professional)

**Best for**: Medium to large teams, recurring onboarding

**Steps**:

1. **Create internal documentation page** (Confluence, Notion, etc.)

2. **Include**:
   - Purpose: Why this skill helps the team
   - Download link with version number
   - Step-by-step installation with screenshots
   - Common use cases for your team
   - Support contact/channel
   - FAQ section

3. **Example structure**:
   ```markdown
   # Claude AI: skill-creator Installation

   ## What is it?
   A skill that helps you create custom AI capabilities for Claude.

   ## Why use it?
   - Standardize our team's AI workflows
   - Create reusable expertise
   - Share AI capabilities across the team

   ## Installation
   [Screenshots + steps]

   ## Use Cases for Our Team
   - Create code review skills
   - Build data analysis workflows
   - Standardize documentation generation

   ## Support
   Questions? Ask in #ai-help Slack channel
   ```

4. **Distribute link** through:
   - Onboarding checklist
   - Team newsletter
   - Weekly standup announcements
   - Slack channel pin

**Time Investment**: 1-2 hours setup, 0 minutes per person (self-service)

---

#### Method 3: Managed Rollout (Enterprise)

**Best for**: Large organizations, compliance requirements

**Steps**:

1. **Pilot Phase** (Week 1-2):
   - Select 5-10 early adopters
   - Gather feedback
   - Refine documentation
   - Identify champions

2. **Department Rollout** (Week 3-6):
   - Roll out to departments
   - Host training sessions
   - Create use case library
   - Monitor adoption

3. **Organization-Wide** (Week 7+):
   - Announce broadly
   - Continuous support
   - Track metrics
   - Iterate on documentation

4. **Track metrics**:
   - Number of users installed
   - Usage frequency
   - Skills created
   - Support requests
   - User feedback

**Time Investment**: 2-4 hours setup + ongoing management

---

### Claude Code Distribution

#### Method 1: Git Repository - Project Skills (Team Sync)

**Best for**: Development teams using git, project-specific needs

**Setup Steps**:

1. **Add skill to your project**:
   ```bash
   cd your-project
   mkdir -p .claude/skills
   cp -r /path/to/skill-weaver/skill-creator .claude/skills/
   ```

2. **Commit to repository**:
   ```bash
   git add .claude/skills/skill-creator
   git commit -m "Add skill-creator v0.1.0-alpha.4"
   git push origin master
   ```

3. **Document in README**:
   ```markdown
   ## Claude Code Skills

   This project includes custom skills in `.claude/skills/`:

   - **skill-creator**: Creates custom Claude skills

   Skills are loaded automatically when Claude Code starts.
   Restart Claude Code if you just pulled this update.
   ```

4. **Notify team**:
   ```
   📢 New Claude Code Skill Available

   We've added the skill-creator to our project!

   To use:
   1. git pull
   2. Restart Claude Code
   3. Try: "Create a skill for our API testing workflow"

   Docs: .claude/skills/weaver-create/README.md
   ```

**Team members get it via**: `git pull` + Claude Code restart

**Updates**: Same process, team members pull updates

**Time Investment**: 30 minutes setup, 1 minute per person

---

#### Method 2: Plugin Marketplace (Professional)

**Best for**: Multiple teams, organization-wide distribution, automatic updates

**Setup Steps**:

1. **Create plugin repository** (one-time):
   ```bash
   # See detailed guide in next section
   # Creates: flashingcursor/skill-creator-plugin
   ```

2. **Create marketplace repository** (one-time):
   ```bash
   # See detailed guide in next section
   # Creates: flashingcursor/skill-weaver-marketplace
   ```

3. **Share installation command**:
   ```bash
   /plugin marketplace add flashingcursor/skill-weaver-marketplace
   /plugin install skill-creator@skill-weaver-marketplace
   ```

4. **For automatic team installation**, add to project's `.claude/settings.json`:
   ```json
   {
     "extraKnownMarketplaces": {
       "company-skills": {
         "source": {
           "source": "github",
           "repo": "your-org/skill-marketplace"
         }
       }
     }
   }
   ```

5. **Notify team**:
   ```
   📦 New Plugin Available: skill-creator

   Install with:
   /plugin marketplace add your-org/skill-marketplace
   /plugin install skill-creator

   Or it will auto-install when you trust the project folder.
   ```

**Team members get it via**: Plugin command or auto-install

**Updates**: Plugin update mechanism

**Time Investment**: 2-3 hours initial setup, 0 minutes per person

---

## Team Rollout Guide

### Pre-Rollout Checklist

- [ ] Test skill on both platforms (if applicable)
- [ ] Create installation documentation
- [ ] Prepare use case examples relevant to team
- [ ] Set up support channel (Slack, email, etc.)
- [ ] Identify team champions/early adopters
- [ ] Prepare announcement message
- [ ] Schedule training session (optional)

### Week 1: Soft Launch

**Monday**:
- [ ] Announce to early adopters (5-10 people)
- [ ] Share installation link/instructions
- [ ] Host office hours for questions

**Wednesday**:
- [ ] Check in with early adopters
- [ ] Gather initial feedback
- [ ] Document FAQ items
- [ ] Fix any installation issues

**Friday**:
- [ ] Compile success stories
- [ ] Refine documentation
- [ ] Prepare for broader rollout

### Week 2-3: Broad Rollout

**Announcement**:
```
🎉 Introducing: skill-creator for Claude

Create custom AI capabilities for your workflows!

📦 For claude.ai users:
   Download: [release link]
   Guide: [installation docs]

🔌 For Claude Code users:
   Run: /plugin marketplace add your-org/marketplace
   Or: See git installation in project README

📚 Documentation: [link]
📺 Demo video: [link] (if available)
💬 Questions: #ai-help channel
🎯 Try it: "Create a skill for code reviews"

Training session: [date/time/link]
```

**Training Session Agenda** (30-45 minutes):
1. Introduction (5 min): What is skill-creator, why it's useful
2. Demo (10 min): Live skill creation example
3. Q&A (15 min): Answer questions
4. Hands-on (15 min): Attendees try creating a skill
5. Next steps (5 min): Resources, support, feedback

### Week 4+: Ongoing Support

- [ ] Monitor adoption metrics
- [ ] Respond to support requests
- [ ] Share success stories
- [ ] Create skill library/examples
- [ ] Iterate on documentation
- [ ] Plan updates and new features

---

## Sharing Templates

### Email Template

```
Subject: New AI Capability: skill-creator for Claude

Hi [Team/Name],

I'm excited to share a new tool that will help us leverage Claude more effectively: **skill-creator**.

**What is it?**
skill-creator is a custom skill for Claude that guides you through creating reusable AI capabilities tailored to your workflows.

**Why use it?**
- Standardize common tasks (code reviews, documentation, data analysis)
- Share expertise across the team
- Make Claude more useful for our specific needs

**How to install:**

For claude.ai:
1. Download: [release URL]
2. Settings → Capabilities → Skills → Upload
3. Enable and test

For Claude Code:
1. [installation method]
2. Restart Claude Code

**Quick start:**
Try asking Claude: "Create a skill for reviewing pull requests"

**Resources:**
- Full guide: [INSTALLATION.md link]
- Examples: [link to examples]
- Support: [Slack channel or email]

**Training session:**
Join us [date/time] for a live demo and Q&A: [meeting link]

Questions? Reply to this email or ask in [support channel].

Best,
[Your name]
```

---

### Slack/Teams Message Template

```
:tada: **New Tool: skill-creator for Claude**

Create custom AI capabilities for your workflows!

:claude: **For claude.ai users:**
• Download: [release URL]
• Guide: [installation link]

:computer: **For Claude Code users:**
• Run: `/plugin marketplace add your-org/marketplace`
• Or see: [git installation link]

:book: **Resources:**
• Docs: [link]
• Examples: [link]
• Support: #ai-help

:rocket: **Try it:**
"Create a skill for code reviews"

:calendar: **Training:**
[Date/time] - [meeting link]

Questions? Thread below :point_down:
```

---

### Internal Wiki Template

```markdown
# skill-creator Installation & Usage

## Overview

skill-creator is a custom Claude skill that helps you create reusable AI capabilities.

**Version**: 0.1.0-alpha.4
**Last Updated**: [date]
**Owner**: [team/person]
**Support**: [channel/email]

## Quick Start

### claude.ai
1. Download: [link]
2. Upload: Settings → Capabilities → Skills
3. Enable and test

### Claude Code
1. Install plugin: `/plugin install skill-creator@your-marketplace`
2. Or clone: [git instructions]
3. Restart Claude Code

## Use Cases

### For Our Team

1. **Code Review Skills**
   - Example: "Create a skill for reviewing Python code"
   - Standardizes review criteria
   - Focuses on our coding standards

2. **Documentation Skills**
   - Example: "Create a skill for API documentation"
   - Follows our doc template
   - Includes required sections

3. **Data Analysis Skills**
   - Example: "Create a skill for analyzing user metrics"
   - Uses our standard KPIs
   - Formats for our dashboards

## Training Materials

- [Video tutorial] (if available)
- [Written guide] (INSTALLATION.md)
- [FAQ section]

## Examples & Templates

[Link to shared folder with example skills created by team]

## Troubleshooting

**Issue**: Skill doesn't load
**Solution**: [steps]

**Issue**: Not invoking correctly
**Solution**: [steps]

More help: [support channel]

## Feedback & Suggestions

Have ideas for improvements? Share in [feedback channel/form].

## Version History

- **0.1.0-alpha.4** (Nov 2025): Initial rollout
- [future versions]
```

---

### Team Training Slide Deck Outline

**Slide 1: Title**
- skill-creator for Claude
- Create Custom AI Capabilities
- [Your Organization]

**Slide 2: The Challenge**
- Claude is powerful but generic
- Your workflows are specific
- Need repeatable processes

**Slide 3: The Solution**
- skill-creator: guided skill creation
- Follows best practices automatically
- Works on claude.ai and Claude Code

**Slide 4: What You Can Build**
- Code review assistants
- Documentation generators
- Data analysis tools
- Domain-specific helpers
- [Your team's examples]

**Slide 5: How It Works** (with screenshots)
- Simple prompt: "Create a skill for..."
- Guided process
- Ready-to-use output

**Slide 6: Installation** (platform-specific)
- claude.ai: 3 steps
- Claude Code: 1 command or git pull

**Slide 7: Live Demo**
- [Screen share creating a skill]
- Show actual usage
- Highlight key features

**Slide 8: Your Turn**
- Hands-on exercise
- Create a skill for [relevant use case]
- Ask questions as you go

**Slide 9: Resources**
- Documentation links
- Support channel
- Example library

**Slide 10: Next Steps**
- Install today
- Try creating one skill
- Share your creations
- Give feedback

---

## Best Practices

### Do's

✅ **Start small**: Roll out to a pilot group first
✅ **Provide examples**: Show skills relevant to your team's work
✅ **Offer support**: Make it easy to get help
✅ **Track adoption**: Know who's using it and how
✅ **Iterate**: Improve based on feedback
✅ **Share success stories**: Highlight wins to encourage adoption
✅ **Keep updated**: Share new versions and improvements
✅ **Document use cases**: Build a library of team-created skills

### Don'ts

❌ **Don't force adoption**: Make it optional and useful
❌ **Don't skip training**: Even simple tools need explanation
❌ **Don't ignore feedback**: Users know what they need
❌ **Don't forget updates**: Keep the skill current
❌ **Don't silo knowledge**: Share learnings across team
❌ **Don't overcomplicate**: Keep instructions simple
❌ **Don't assume expertise**: Provide beginner-friendly guidance

### Success Metrics

Track these to measure adoption:

**Installation Metrics**:
- Number of users installed
- Installation completion rate
- Time to first install
- Platform breakdown (claude.ai vs Claude Code)

**Usage Metrics**:
- Skills created per user
- Active users per week
- Repeat usage rate
- Most common skill types

**Quality Metrics**:
- Support requests
- Installation issues
- User satisfaction scores
- Skill quality (if reviewable)

**Business Impact**:
- Time saved on repetitive tasks
- Consistency improvements
- Knowledge sharing increase
- Productivity gains

---

## Distribution Channels

### Internal Channels

**Slack/Teams**:
- Announcement in general/engineering channel
- Dedicated #ai-tools channel
- Pin important messages
- Regular reminders

**Email**:
- Company/team newsletter
- Direct email to relevant groups
- Onboarding emails for new hires
- Update announcements

**Documentation**:
- Internal wiki (Confluence, Notion)
- Developer handbook
- Onboarding guides
- Tool directory

**Meetings**:
- Team all-hands
- Engineering sync
- Lunch & learns
- Office hours

### External Channels (if public)

**GitHub**:
- README with prominent installation section
- Releases with detailed notes
- Discussions for community
- Wiki for extended docs

**Social Media**:
- LinkedIn post
- Twitter announcement
- Company blog
- Tech community forums

**Developer Relations**:
- Conference talks
- Blog posts/tutorials
- Developer newsletters
- Community events

---

## Update Distribution

When releasing new versions:

1. **Prepare Release Notes**:
   - What's new
   - What's fixed
   - Breaking changes
   - Migration guide (if needed)

2. **Announce Through Channels**:
   ```
   📦 skill-creator v0.2.0 Released!

   New features:
   - [feature 1]
   - [feature 2]

   Improvements:
   - [improvement 1]
   - [improvement 2]

   Update now:
   claude.ai: Download new version and re-upload
   Claude Code: git pull or /plugin update

   Full changelog: [link]
   ```

3. **Support Migration**:
   - Address questions quickly
   - Document common issues
   - Provide rollback instructions if needed

4. **Track Adoption**:
   - Monitor update rate
   - Identify blockers
   - Assist stragglers

---

## Getting Help

If you need assistance with distribution:

1. **Check this guide** first
2. **Review INSTALLATION.md** for technical details
3. **Open GitHub issue** for bugs or feature requests
4. **GitHub Discussions** for questions and ideas
5. **Contact maintainer**: [contact info]

---

## Appendix: Creating Plugin Marketplace

Detailed step-by-step guide for setting up professional distribution.

**[This section would include the detailed technical steps from the research,
formatted as a clear tutorial for creating the plugin and marketplace repositories]**

---

**Version**: This guide applies to skill-creator v0.1.0-alpha.4 and later.

**Last Updated**: 2025-11-06

**Maintainer**: [Your name/team]
