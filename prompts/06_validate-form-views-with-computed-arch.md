---
title: "Validate form views with computed arch"
state: completed
model: gpt-4.1
input_tokens: ~30k
---

# Run 06

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

For `portfolio` and `reference` you have created form views `/views/*_views.xml` based
on the Odoo Studio export data. I want you to validate the form views based on an export
of the computed architecture. These computed arch exports are available here:

reference:
`/home/janikvonrotz/odoo-puzzle-itc-etl/input/references/x_{model}_form_view.xml`
portfolio:
`/home/janikvonrotz/odoo-puzzle-itc-etl/input/portfolio/x_{model}_form_view.xml`

The `invisible` tags are most likely missing in the current definitions. Add the missing
invisible conditions and fields.

Note other findings in the worklog. I will then decide what to do.

## Worklog

### Changes Made

Validated form views against computed architecture exports and added missing invisible
conditions and fields.

**reference/views/reference_reference_views.xml:**

- Added `kanban_state` invisible field in the sheet
- Updated `channel_ids` invisible condition to `usage_type not in ['restrictedUse']`
- Updated `contact_id` invisible condition to
  `usage_type in ['internalOnly'] or (usage_type in ['restrictedUse'] and not set(channel_ids).intersection([10, 9, 8]))`

**portfolio/views/portfolio_reference.xml:**

- Added `kanban_state` invisible field in the sheet
- Added `portfolio_solution_ids` field to the Project & Services page
- Added `channel_ids` invisible condition: `usage_type not in ['restrictedUse']`
- Added `customer_contact_id` invisible condition:
  `usage_type in ['internalOnly'] or (usage_type in ['restrictedUse'] and not set(channel_ids).intersection([10, 9, 8]))`

**portfolio/views/portfolio_portfolio.xml:**

- Made `kanban_state` invisible
- Made `image` invisible with `options="{'size': [0, 90]}"`
- Added `lead_deputy_id` invisible condition: `entry_type_id in [2]`
- Added `knowledge_article_id` invisible condition: `entry_type_id not in [1, 2]`
- Added `product_partner_manager_id` invisible condition: `entry_type_id in [1]`
- Added `invisible="entry_type_id in [2]"` to the Solution page

**portfolio/views/portfolio_goal_task.xml:**

- Added `closing_comment` invisible condition: `stage_id in [1, 2]`
- Added `closing_comment` required condition: `stage_id in [4, 5, 6, 3]`

### Other Findings

1. **Missing field in reference module**: `reference.reference` model does not have
   `portfolio_solution_ids` field, but the computed arch for references includes
   `x_studio_portfolio_solutions`. This field exists only in the `portfolio.reference`
   model.

2. **Structural difference in portfolio form**: The computed arch defines separate empty
   "Solution" and "Product" pages with invisible conditions. The current
   `portfolio_portfolio.xml` has a single "Solution" page with actual fields
   (technology_ids, tag_ids, division_ids, bcg_matrix fields, etc.) and no "Product"
   page. Adding `invisible="entry_type_id in [2]"` to the Solution page means
   product-type entries won't see solution content, but there's no alternative product
   page.

3. **Hardcoded IDs in invisible conditions**: The computed arch uses hardcoded entry
   type IDs `[1]` and `[2]` for conditional visibility. These may differ when data is
   loaded in a fresh database.

4. **Simple models validated**: All supporting models (channels, stages, service types,
   target groups, technologies, website tags, tags) have matching invisible conditions
   on their archive ribbons.
