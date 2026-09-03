---
title: "Migrate Portfolio Odoo Studio app to module"
state: draft
model:
input_tokens:
---

# Run 05

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

You are working in the context of an Odoo repo `addons/tender`. This repos has been
initialized with an Odoo module `addons/tender/portfolio`.

There is a Odoo Studio app with the name "Portfolio". The export all Studio
customisations are stored here `$HOME/Odoo-Build/tmp/studio_customization/data`.

Your goal is to create an actual module from the Odoo studio export.

In the Studio export you find these files:

- `ir_ui_view.xml`: Containts all the view definitions of the apps
- `ir_ui_menu.xml`: Menu structure of the apps. This can give you an idea what the
  "Portfolio" app looks like. The main menu entry has a `web_icon` attribute.
- `ir_actions_act_window.xml`: Actions referenced by the menu entries. They make the
  link from menu to model.
- `ir_model.xml`: Models created with Odoo studio.
- `ir_model_fields.xml`: All model fields created with Odoo studio.

I want you to start with an analysis of the files and answer the following questions:

1. What does the menu structure of "Portfolio" look like? Show the hierarchy.
2. What models and fields are shown in "Portfolio" apps?
3. Which fields are actually shown in the views of the "Portfolio" app?

### Models

Once you have answered these questions. I want you to setup the python models of the
`portfolio` module. Use this task command to create the files:

```bash
task generate-module-model addons/tender/portfolio portfolio.portfolio
```

Create all models and fields. The fields have to be added manually.

For the `portfolio.portfolio` model I have already generated skeleton code.

### Rename Fields

Once you have done this, I want you to rename all fields. They should not have an `x_`
or `x_studio` or any generated name. Make an educated guess for new names and create a
mapping table form Studio field names to the new names.

Do not create menus and views yet.

Keep track of the original and new field names. Create a file
`portfolio/readme/FIELD_MAPPING.md` and document all models and fields. This document
will be used to generate the data migration script.

### Access Rules

For all models create access rules. Use
`task generate-module-security addons/tender/portfolio portfolio.portfolio` to generate
the rules.

I have already created one example.

### Menus

Now create the menu structure. The relevant data is in `ir_ui_menu.xml`. It Contains
root and sub menu items.

### Views

The `ir_ui_view.xml` contains the view definitions and xml edits from Odoo Studio.

For all models generate default views with
`task generate-module-views addons/tender/portfolio portfolio.portfolio`. As usual I
have already created an example.

Update the view definitions according to the definitions of the Studio app.

When naming `group` tags, give a fitting name and not the generic Studio name.

Note that the new views must not have any xml edits. Xml edit can be identified by the
`position` attribute. Try to reconstruct the final views.

### Demo

Create demo xml data for a portfolio and linked records like tags, target group and so
on. The demo data should be stored in `addons/tender/portfolio/demo/demo.xml`.

### Testing

Run `task lint` in `addons/tender`.

I will start the Odoo db and install the module myself.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update info about model and token usage.
