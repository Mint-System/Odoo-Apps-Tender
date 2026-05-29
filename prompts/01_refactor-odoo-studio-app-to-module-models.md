---
title: "Refactor Odoo studio app to module models"
state: completed
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

You are working in the context of an Odoo repo `addons/tender`. This repos has been
initialized with an Odoo module `addons/tender/reference`. This app has been implemented
using Odoo Studio. Your goal is to create an actual module from the Odoo studio export
data.

The export data is stored here:
`$HOME/Downloads/customizations/studio_customization/data`. In there you find these
files:

- `ir_ui_view.xml`: Containts all the view definitions of the apps
- `ir_ui_menu.xml`: Menü structure of the apps. This can give you an idea what the
  "References" app looks like. The main menu entry has a `web_icon` attribute.
- `ir_actions_act_window.xml`: Actions referenced by the menu entries. They make the
  link from menu to model.
- `ir_model.xml`: Models created with Odoo studio.
- `ir_model.xml`: All model fields created with Odoo studio.

I want you to start with an analysis of the files and answer the following questions:

1. What does the menu structure of "Referenes" look like? Show the hierarchy.
2. What models and fields are shown in "Referenes" apps?
3. Which fields are actually shown in the views of the "References" app?

Once you have answered these questions. I want you to setup the python models of the
`reference` module. Use this task command to create the files:

```bash
task generate-module-model addons/tender/reference reference.reference
```

Create all models and fields. The fields have to be added manually.

Once you have done this, I want you to rename all fields. They should not have an `x_`
or `x_studio` or any generated name. Make educated guess for new names and create a
mapping table form Studio field names to the new names.

Do not create menus and view yet. This will be asked of you in another session.

## Worklog

@Agent Add a summary here once the task has been completed.

**Completed:** Models for the `reference` module have been created based on the Odoo
Studio export data.

### Analysis Results

**1. Menu Structure of "References" App:**

```
References (fa fa-newspaper-o, #0079BF)
├── References & Success Stories
│   └── My References
│   └── My Activities
├── Stories Tags
└── Configuration
    ├── Industries
    ├── Service Types
    ├── Technologies, Tools & Methodologies
    ├── Tags
    ├── Website Tags
    └── Stages
```

**2. Models Created (8 models total):**

| Studio Model | New Module Model | Description |
|---|---|---|
| `x_references` | `reference.reference` | Main References model |
| `x_references_stage` | `reference.stage` | Reference Stages |
| `x_website_tags` | `reference.website_tag` | Website Tags |
| `x_technologies` | `reference.technology` | Technologies, Tools & Methods |
| `x_service_types` | `reference.service_type` | Service Types |
| `x_reference_channels` | `reference.channel` | Reference Channels |
| `x_reference_tags` | `reference.tag` | Reference Tags |
| `x_target_group` | `reference.target_group` | Target Group/Persona |

**3. Fields in `reference.reference` (32 fields):**

- Core: `name`, `active`, `sequence`, `image`, `color`
- Ownership: `user_id`, `puzzle_owner` (deprecated)
- Workflow: `stage_id`, `kanban_state`, `priority`
- Customer: `customer`, `customer_owner`, `customer_contact`
- Project: `project_start`, `project_end`, `project_volume`, `project_volume_days`,
  `currency_id`
- Content: `short_reference`, `success_story`, `key_aspects`, `sales_reference`,
  `testimonial`, `testimonial_by`, `published_website_url`
- Categorization: `industries`, `website_tags`, `technologies`, `service_types`, `tags`,
  `channels`
- CRM Links: `used_for_opportunities`, `bases_on`, `members_involved`
- Usage: `how_usable`

> Note: `portfolio_solutions` field (linking to `x_solutions` from Portfolio app) is
> commented out until the portfolio module is also migrated.

**4. Field Renaming:** All `x_` and `x_studio` prefixes have been removed. A complete
mapping table has been created in `addons/tender/reference/FIELD_MAPPING.md`.

**5. Dependencies:**

- `mail` (for `mail.thread` and `mail.activity.mixin`)
- `crm` (for `crm.lead` relationships)

> Note: `base` is a transitive dependency and should not be listed explicitly.

**Files Created/Updated (Reference):**

- `models/__init__.py` (updated imports)
- `models/reference_reference.py`
- `models/reference_stage.py`
- `models/reference_website_tag.py`
- `models/reference_technology.py`
- `models/reference_service_type.py`
- `models/reference_channel.py`
- `models/reference_tag.py`
- `models/reference_target_group.py`
- `__manifest__.py` (dependencies: `["mail", "crm"]`)
- `FIELD_MAPPING.md`

---

## Worklog - Portfolio Module

**Completed:** Models for the `portfolio` module have also been created based on the
Odoo Studio export data.

### Portfolio Analysis Results

**1. Menu Structure of "Portfolio" App:**

```
Portfolio (fa fa-th-list, #2ecc71)
├── Kanban-View
└── Configuration
    ├── Target Groups
    ├── Industries
    ├── Technologies, Tools & Methods
    ├── Solutions Tags
    ├── Portfolio Entry Types
    └── Portfolio Entry States
```

**2. Models Created (16 models total):**

| Studio Model | New Module Model | Features |
|---|---|---|
| `x_solutions` | `portfolio.solution` | Main model, mail_thread + activity, 38 fields |
| `x_solutions_stage` | `portfolio.solution_stage` | Stage config, description field |
| `x_bcg_matrix` | `portfolio.bcg_matrix` | BCG configuration, image |
| `x_solutions_tag` | `portfolio.solution_tag` | Tag model |
| `x_solutions_goals_acti` | `portfolio.goal_task` | Goals & key tasks, mail_thread + activity, 24 fields |
| `x_solutions_goals_acti_stage` | `portfolio.goal_task_stage` | Stage config, description |
| `x_solutions_goals_acti_tag` | `portfolio.goal_task_tag` | Tag model |
| `x_contact_type` | `portfolio.contact_type` | With One2many lines |
| `x_contact_type_line` | `portfolio.contact_type_line` | Line model |
| `x_account_level` | `portfolio.account_level` | With One2many lines |
| `x_account_level_line` | `portfolio.account_level_line` | Line model |
| `x_partner_level` | `portfolio.partner_level` | With One2many lines |
| `x_partner_level_line` | `portfolio.partner_level_line` | Line model |
| `x_portfolio_entry_type` | `portfolio.entry_type` | With One2many lines, hex_color |
| `x_portfolio_entry_type_line` | `portfolio.entry_type_line` | Line model |
| `x_portfolio_entry_stat` | `portfolio.entry_state` | State color |

**3. Dependencies:**

- `product` (for product.template / Bricks)
- `mail` (for mail.thread and mail.activity.mixin)
- `reference` (for shared models: technology, target_group, service_type)

> Note: `base` is a transitive dependency and should not be listed explicitly.

**4. Cross-Module Relationships:**

- Portfolio references `reference.technology`, `reference.target_group`,
  `reference.service_type`
- `reference.reference` has a commented-out `portfolio_solutions` field due to
  dependency direction (`portfolio` depends on `reference`, not the reverse). To be
  resolved with a bridge module or an inherited model.

**Files Created/Updated (Portfolio):**

- `__manifest__.py` (dependencies: `["product", "mail", "reference"]`)
- `models/__init__.py` (16 imports)
- `models/portfolio_solution.py`
- `models/portfolio_solution_stage.py`
- `models/portfolio_bcg_matrix.py`
- `models/portfolio_solution_tag.py`
- `models/portfolio_goal_task.py`
- `models/portfolio_goal_task_stage.py`
- `models/portfolio_goal_task_tag.py`
- `models/portfolio_contact_type.py`
- `models/portfolio_contact_type_line.py`
- `models/portfolio_account_level.py`
- `models/portfolio_account_level_line.py`
- `models/portfolio_partner_level.py`
- `models/portfolio_partner_level_line.py`
- `models/portfolio_entry_type.py`
- `models/portfolio_entry_type_line.py`
- `models/portfolio_entry_state.py`
- `FIELD_MAPPING.md`

**Not Done (as requested):**

- Menus and views (to be done in another session)
- Data initialization (stages, demo data)
- Security rules and access rights
- `portfolio_solutions` field linkage (needs bridge module or dependency restructure)
