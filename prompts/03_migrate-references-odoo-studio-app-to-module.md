---
title: "Migrate References Odoo Studio app to module"
state: completed
---

# Run 03

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

You are working in the context of an Odoo repo `addons/tender`. This repos has been
initialized with an Odoo module `addons/tender/reference`.

There is Odoo Studio app with the name "References". The export all Studio
customisations are stored here
`$HOME/Odoo-Build/tmp/customizations/studio_customization/data`.

Your goal is to create an actual module from the Odoo studio export.

In the Studio export you find these files:

- `ir_ui_view.xml`: Containts all the view definitions of the apps
- `ir_ui_menu.xml`: Menü structure of the apps. This can give you an idea what the
  "References" app looks like. The main menu entry has a `web_icon` attribute.
- `ir_actions_act_window.xml`: Actions referenced by the menu entries. They make the
  link from menu to model.
- `ir_model.xml`: Models created with Odoo studio.
- `ir_model_fields.xml`: All model fields created with Odoo studio.

I want you to start with an analysis of the files and answer the following questions:

1. What does the menu structure of "Referenes" look like? Show the hierarchy.
2. What models and fields are shown in "Referenes" apps?
3. Which fields are actually shown in the views of the "References" app?

### Models

Once you have answered these questions. I want you to setup the python models of the
`reference` module. Use this task command to create the files:

```bash
task generate-module-model addons/tender/reference reference.reference
```

Create all models and fields. The fields have to be added manually.

For the `reference.reference` model I have already generated skeleton code.

### Rename Fields

Once you have done this, I want you to rename all fields. They should not have an `x_`
or `x_studio` or any generated name. Make educated guess for new names and create a
mapping table form Studio field names to the new names.

Do not create menus and view yet.

Keep track of the original and new field names. Create a file
`reference/readme/FIELD_MAPPING.md` and document all models and fields. This document
will be used to generate the data migratio script.

### Access Rules

For all models create the access rules. Use
`task generate-module-security addons/tender/reference reference.reference` to generate
the rules.

I have already created one example.

### Menus

Now create the menu structure. The relevant data is in `ir_ui_menu.xml`. It Contains
root and sub menu items.

### Views

The `ir_ui_view.xml` contains the view definitions and xml edits from Odoo Studio.

For all models generate default views with
`task generate-module-views addons/tender/reference reference.reference`. As usual I
have already created an example.

Update the view definitions according to the definitions of the Studio app.

When naming `group` tags, give a fitting name and not the generic Studio name.

Note that the new views must not have any xml edits. Xml edit can be identified by the
`position` attribute. Try to reconstruct the final views.

### Testing

Run `task lint` in `addons/tender`. I will start the Odoo db and install the module.

## Worklog

- Analysed the Studio export located in
  `~/Downloads/customizations/studio_customization/data`.
- Identified the "References" app menu hierarchy, models (`x_references`,
  `x_references_stage`, `x_website_tags`, `x_technologies`, `x_service_types`,
  `x_reference_channels`, `x_reference_tags`, `x_target_group`), and all fields.
- Reconstructed the final views from Studio's default + xpath customisations (removed
  all xml edits).
- Renamed all models and fields from `x_studio_*` / `x_*` to clean, meaningful names
  (e.g. `reference.reference`, `stage_id`, `customer_id`, `usage_type`).
- Created `FIELD_MAPPING.md` documenting the mapping for future data migration.
- Generated model skeletons and populated them with the correct fields; added mail
  thread/activity mixins where needed.
- Generated access rules for all models using `task generate-module-security`.
- Created menus matching the original hierarchy (root "References" with web icon,
  sub-menus incl. Configuration).
- Created list, form, kanban, and search views for `reference.reference` and all
  supporting models.
- Renamed all generic `studio_group_*` names to meaningful group names.
- Fixed XML ordering: moved `reference_reference_search_view` before the actions that
  reference it to avoid forward-reference errors during module installation.
- Added demo data in `demo/demo.xml` with a sample reference record, partners,
  industries, technologies, website tags, and service types.
- Added a default kanban stage "New" in `data/reference_stage_data.xml` and wired it as
  the default `stage_id` on `reference.reference` via `_default_stage_id()`.
- Ran `task lint` successfully (all pre-commit hooks passed).
