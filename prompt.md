---
title: "Fix portfolio and reference modules"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: draft
date_completed: YYYY-MM-DD
model:
input_tokens:
output_tokens:
---

# Fix portfolio and reference modules

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

### Potfolio

The `addons/tender/portfolio` module has been created from Odoo studio data `addons/tender/tmp/studio_customization/data`.

I am comparing the implementend module and the studio app.

- The module is missing the "Products (Bricks)" menu entry.
- The first menu item is calledn "Kanban-View" instead of "Portfolio Management"
- The configuration menu is very different:

The studio has the configuratio menu entries:

1	Portfolio Type	
2	Solutions Tag	
3	Goals & Key Task Tags	
4	Target Groups	
5	Technologies, Tools & Methods	
6	Industries	
7	Boston Consulting Group Matrix	
8	Portfolio Stages	
9	Portfolio Entry Type	
10	Goals & Key Task Stages

The module has only these entries:

1	Target Groups	
2	Technologies, Tools & Methods	
3	Industries	
4	Boston Consulting Group Matrix	
5	Portfolio Stages	
6	Portfolio Entry Types	
7	Portfolio Entry States

So missing is:

1	Portfolio Type	
2	Solutions Tag	
3	Goals & Key Task Tags	
10	Goals & Key Task Stages

And this can be removed:

7	Portfolio Entry States

Check if the models for these menu entries are available. If not you have to create them. See `addons/tender/tmp/prompt-log/2026-09-03_migrate-portfolio-odoo-studio-app-to-module.md` for how this was done.

### References

The `addons/tender/reference` module has been created from Odoo studio data `addons/tender/tmp/studio_customization/data`.

I am comparing the implementend module and the studio app.

- The module is missing the "Website-Tags" menu entry.
- 

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update date and model. If you have access to session info also add token count.
