---
title: "Refactor Odoo studio data to module views"
state: ready
---

# Run 02

Note: @Clanker refers to the AI agent (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

In the last session you have completed the prompt
`addons/tender/prompts/01_refactor-odoo-studio-app-to-module-models.md`. Study the file
carefully.

Now I would like to create the following module resources:

- access rules
- menu structure
- views

The relevant data is in:

- `ir_ui_view.xml`: Has initial view definitions and xml edits.
- `ir_ui_menu.xml`: Contains root and sub menu items.

Start by creating the access rules for each model. Use
`task generate-module-security addons/tender/reference reference.reference` generate the
rules.

Then create default views for each model with
`task generate-module-views addons/tender/reference reference.reference`. Update the
view definitions according to the definitions of the Studio apps.

Note that the new views must not have any xml edits. Xml edit can be identified by the
`position` attribute. Try to reconstruct the final views.

While re-creating the views keep in mind that all field names have been mapped to new
names `FIELD_MAPPING.md`.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed.
