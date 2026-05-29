---
title: "Refactor Odoo studio app to module models"
---

# Run 01

Note: @Agent refers to the AI agent (you) who is working on this task.

@Agent when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

You are working in the context of an Odoo repo `addons/tender`. This repos has been initialized with an Odoo module `addons/tender/reference`. This app has been implemented using Odoo Studio. Your goal is to create an actual module from the Odoo studio export data.

The export data is stored here: `/home/janikvonrotz/Downloads/customizations/studio_customization/data`. In there you find these files:

- `ir_ui_view.xml`: Containts all the view definitions of the apps
- `ir_ui_menu.xml`: Menü structure of the apps. This can give you an idea what the "References" app looks like. The main menu entry has a `web_icon` attribute.
- `ir_actions_act_window.xml`: Actions referenced by the menu entries. They make the link from menu to model.
- `ir_model.xml`: Models created with Odoo studio.
- `ir_model.xml`: All model fields created with Odoo studio.

I want you to start with an analysis of the files and answer the following questions:

1. What does the menu structure of "Referenes" look like? Show the hierarchy.
2. What models and fields are shown in "Referenes" apps?
3. Which fields are actually shown in the views of the "References" app?

Once you have answered these questions. I want you to setup the python models of the `reference` module. Use this task command to create the files:

```bash
task generate-module-model addons/tender/reference reference.reference
```

Create all models and fields. The fields have to be added manually.

Once you have done this, I want you to rename all fields. They should not have an `x_` or `x_studio` or any generated name. Make educated guess for new names and create a mapping table form Studio field names to the new names.

Do not create menus and view yet. This will be asked of you in another session.

## Worklog

@Agent Add a summary here once the task has been completed.
