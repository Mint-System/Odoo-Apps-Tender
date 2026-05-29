# Field Mapping Table: Studio Fields to Portfolio Module Fields

This document maps the original Odoo Studio field names (with `x_` and `x_studio`
prefixes) to the new clean field names used in the `portfolio` module.

## Model: `portfolio.solution` (was `x_solutions`)

| Studio Field Name                      | New Field Name               | Type                                | Notes                               |
| -------------------------------------- | ---------------------------- | ----------------------------------- | ----------------------------------- |
| `x_name`                               | `name`                       | Char                                | Solution Name, required, translated |
| `x_active`                             | `active`                     | Boolean                             |                                     |
| `x_studio_user_id`                     | `user_id`                    | Many2one (res.users)                | Owner                               |
| `x_studio_notes`                       | `notes`                      | Html                                |                                     |
| `x_studio_image`                       | `image`                      | Binary                              |                                     |
| `x_studio_sequence`                    | `sequence`                   | Integer                             |                                     |
| `x_studio_stage_id`                    | `stage_id`                   | Many2one (portfolio.solution_stage) | Required                            |
| `x_studio_priority`                    | `priority`                   | Boolean                             | High Priority                       |
| `x_color`                              | `color`                      | Integer                             |                                     |
| `x_studio_kanban_state`                | `kanban_state`               | Selection                           | draft/done/blocked                  |
| `x_studio_description_long`            | `description_long`           | Html                                | Description (extended)              |
| `x_studio_description`                 | `description`                | Text                                |                                     |
| `x_studio_target_groups_personas`      | `target_groups_personas`     | Many2many (reference.target_group)  |                                     |
| `x_studio_target_industries`           | `target_industries`          | Many2many (res.partner.industry)    |                                     |
| `x_studio_divisions`                   | `divisions`                  | Many2many (res.partner)             | Bases / Divisions                   |
| `x_studio_tags`                        | `tags`                       | Many2many (portfolio.solution_tag)  |                                     |
| `x_studio_technologies_tools_methods`  | `technologies_tools_methods` | Many2many (reference.technology)    |                                     |
| `x_studio_bcg_matrix_present`          | `bcgs_matrix_present`        | Many2one (portfolio.bcg_matrix)     | BCG Matrix (Present)                |
| `x_studio_goal_bcg_matrix`             | `goal_bcg_matrix`            | Many2one (portfolio.bcg_matrix)     | BCG Matrix: Goal                    |
| `x_studio_today_bcg_matrix`            | `today_bcg_matrix`           | Many2one (portfolio.bcg_matrix)     | BCG Matrix: Today                   |
| `x_studio_portfolio_entry_type`        | `entry_type`                 | Many2one (portfolio.entry_type)     | Type                                |
| `x_studio_portfolio_entry_state`       | `entry_state`                | Many2one (portfolio.entry_state)    | Status/Health                       |
| `x_studio_portfolio_entry_state_color` | `entry_state_color`          | Integer                             | Computed from entry_state           |
| `x_studio_portfolio_type_hex_color`    | `hex_color`                  | Char                                | Related to entry_type.hex_color     |
| `x_studio_revenue_current`             | `revenue_current`            | Integer                             | Current Revenue [CHF]               |
| `x_studio_revenue_target`              | `revenue_target`             | Integer                             | Revenue Target [CHF]                |
| `x_studio_profit_margin`               | `profit_margin`              | Float                               | Profit margin [%]                   |
| `x_studio_next_review`                 | `next_review`                | Date                                |                                     |
| `x_studio_next_milestone_date`         | `next_milestone_date`        | Date                                |                                     |
| `x_studio_next_milestone`              | `next_milestone`             | Char                                |                                     |
| `x_studio_solution_lead_stv`           | `solution_lead_stv`          | Many2one (res.users)                | Lead Stv.                           |
| `x_studio_product_partner_manager`     | `product_partner_manager`    | Many2one (res.users)                | Partner Manager                     |
| `x_studio_key_members`                 | `key_members`                | Many2many (res.users)               |                                     |
| `x_studio_partners`                    | `partners`                   | Many2many (res.partner)             |                                     |
| `x_studio_bricks`                      | `bricks`                     | Many2many (product.template)        |                                     |
| `x_studio_goals`                       | `goal_ids`                   | One2many (portfolio.goal_task)      | Goals filtered by stage+type        |
| `x_studio_key_tasks`                   | `key_task_ids`               | One2many (portfolio.goal_task)      | Key Tasks filtered by stage+type    |
| `x_studio_links`                       | `links`                      | Html                                |                                     |

## Model: `portfolio.solution_stage` (was `x_solutions_stage`)

| Studio Field Name      | New Field Name | Type    | Notes                            |
| ---------------------- | -------------- | ------- | -------------------------------- |
| `x_name`               | `name`         | Char    | Stage Name, required, translated |
| `x_studio_sequence`    | `sequence`     | Integer |                                  |
| `x_studio_description` | `description`  | Html    |                                  |

## Model: `portfolio.bcg_matrix` (was `x_bcg_matrix`)

| Studio Field Name      | New Field Name | Type    | Notes                |
| ---------------------- | -------------- | ------- | -------------------- |
| `x_name`               | `name`         | Char    | Required, translated |
| `x_active`             | `active`       | Boolean |                      |
| `x_studio_sequence`    | `sequence`     | Integer |                      |
| `x_studio_description` | `description`  | Html    |                      |
| `x_avatar_image`       | `image`        | Binary  |                      |

## Model: `portfolio.solution_tag` (was `x_solutions_tag`)

| Studio Field Name | New Field Name | Type    | Notes                |
| ----------------- | -------------- | ------- | -------------------- |
| `x_name`          | `name`         | Char    | Required, translated |
| `x_active`        | `active`       | Boolean |                      |
| `x_studio_color`  | `color`        | Integer |                      |

## Model: `portfolio.goal_task` (was `x_solutions_goals_acti`)

| Studio Field Name          | New Field Name    | Type                                 | Notes                                   |
| -------------------------- | ----------------- | ------------------------------------ | --------------------------------------- |
| `x_name`                   | `name`            | Char                                 | Required, translated                    |
| `x_active`                 | `active`          | Boolean                              |                                         |
| `x_studio_user_id`         | `user_id`         | Many2one (res.users)                 | Responsible                             |
| `x_studio_currency_id`     | `currency_id`     | Many2one (res.currency)              |                                         |
| `x_studio_value`           | `value`           | Monetary                             |                                         |
| `x_studio_sequence`        | `sequence`        | Integer                              |                                         |
| `x_studio_stage_id`        | `stage_id`        | Many2one (portfolio.goal_task_stage) | Required                                |
| `x_studio_priority`        | `priority`        | Boolean                              | High Priority                           |
| `x_color`                  | `color`           | Integer                              |                                         |
| `x_studio_kanban_state`    | `kanban_state`    | Selection                            | normal/done/blocked                     |
| `x_studio_tag_ids`         | `tag_ids`         | Many2many (portfolio.goal_task_tag)  |                                         |
| `x_studio_solution`        | `solution_id`     | Many2one (portfolio.solution)        |                                         |
| `x_studio_start_date`      | `start_date`      | Date                                 | Time Period                             |
| `x_studio_due_date`        | `due_date`        | Date                                 | Due Date                                |
| `x_studio_periode`         | `period`          | Date                                 | Periode                                 |
| `x_studio_type`            | `type`            | Selection                            | goal/task                               |
| `x_studio_indicator`       | `indicator`       | Selection                            | Qualitative/Revenue/FTE/Customers/Other |
| `x_studio_commit_text`     | `commit_text`     | Text                                 |                                         |
| `x_studio_target_text`     | `target_text`     | Text                                 |                                         |
| `x_studio_description`     | `description`     | Html                                 |                                         |
| `x_studio_commit_num`      | `commit_num`      | Integer                              |                                         |
| `x_studio_target_num`      | `target_num`      | Integer                              |                                         |
| `x_studio_closing_comment` | `closing_comment` | Text                                 |                                         |

## Model: `portfolio.goal_task_stage` (was `x_solutions_goals_acti_stage`)

| Studio Field Name      | New Field Name | Type    | Notes                            |
| ---------------------- | -------------- | ------- | -------------------------------- |
| `x_name`               | `name`         | Char    | Stage Name, required, translated |
| `x_studio_sequence`    | `sequence`     | Integer |                                  |
| `x_studio_description` | `description`  | Html    |                                  |

## Model: `portfolio.goal_task_tag` (was `x_solutions_goals_acti_tag`)

| Studio Field Name | New Field Name | Type    | Notes    |
| ----------------- | -------------- | ------- | -------- |
| `x_name`          | `name`         | Char    | Required |
| `x_color`         | `color`        | Integer |          |

## Model: `portfolio.contact_type` (was `x_contact_type`)

| Studio Field Name               | New Field Name | Type                                   | Notes                              |
| ------------------------------- | -------------- | -------------------------------------- | ---------------------------------- |
| `x_name`                        | `name`         | Char                                   | Contact Type, required, translated |
| `x_active`                      | `active`       | Boolean                                |                                    |
| `x_studio_sequence`             | `sequence`     | Integer                                |                                    |
| `x_studio_description`          | `description`  | Char                                   | Contact Type Description           |
| `x_contact_type_line_ids_0c01d` | `line_ids`     | One2many (portfolio.contact_type_line) | Lines                              |

## Model: `portfolio.contact_type_line` (was `x_contact_type_line_ac124`)

| Studio Field Name   | New Field Name    | Type                              | Notes                             |
| ------------------- | ----------------- | --------------------------------- | --------------------------------- |
| `x_contact_type_id` | `contact_type_id` | Many2one (portfolio.contact_type) | Required                          |
| `x_studio_sequence` | `sequence`        | Integer                           |                                   |
| `x_name`            | `name`            | Char                              | Description, required, translated |

## Model: `portfolio.account_level` (was `x_account_level`)

| Studio Field Name                      | New Field Name | Type                                    | Notes                               |
| -------------------------------------- | -------------- | --------------------------------------- | ----------------------------------- |
| `x_name`                               | `name`         | Char                                    | Account Level, required, translated |
| `x_active`                             | `active`       | Boolean                                 |                                     |
| `x_studio_sequence`                    | `sequence`     | Integer                                 |                                     |
| `x_studio_account_level_description_1` | `description`  | Char                                    | Account Level Description           |
| `x_account_level_line_ids_e5666`       | `line_ids`     | One2many (portfolio.account_level_line) | Lines                               |

## Model: `portfolio.account_level_line` (was `x_account_level_line_ef13c`)

| Studio Field Name    | New Field Name     | Type                               | Notes                             |
| -------------------- | ------------------ | ---------------------------------- | --------------------------------- |
| `x_account_level_id` | `account_level_id` | Many2one (portfolio.account_level) | Required                          |
| `x_studio_sequence`  | `sequence`         | Integer                            |                                   |
| `x_name`             | `name`             | Char                               | Description, required, translated |

## Model: `portfolio.partner_level` (was `x_partner_level`)

| Studio Field Name                      | New Field Name | Type                                    | Notes                               |
| -------------------------------------- | -------------- | --------------------------------------- | ----------------------------------- |
| `x_name`                               | `name`         | Char                                    | Partner Level, required, translated |
| `x_active`                             | `active`       | Boolean                                 |                                     |
| `x_studio_sequence`                    | `sequence`     | Integer                                 |                                     |
| `x_studio_partner_level_description_1` | `description`  | Char                                    | Partner Level Description           |
| `x_partner_level_line_ids_1b853`       | `line_ids`     | One2many (portfolio.partner_level_line) | Lines                               |

## Model: `portfolio.partner_level_line` (was `x_partner_level_line_e603e`)

| Studio Field Name    | New Field Name     | Type                               | Notes                             |
| -------------------- | ------------------ | ---------------------------------- | --------------------------------- |
| `x_partner_level_id` | `partner_level_id` | Many2one (portfolio.partner_level) | Required                          |
| `x_studio_sequence`  | `sequence`         | Integer                            |                                   |
| `x_name`             | `name`             | Char                               | Description, required, translated |

## Model: `portfolio.entry_type` (was `x_portfolio_entry_type`)

| Studio Field Name                       | New Field Name | Type                                 | Notes                                      |
| --------------------------------------- | -------------- | ------------------------------------ | ------------------------------------------ |
| `x_name`                                | `name`         | Char                                 | Portfolio Entry Type, required, translated |
| `x_active`                              | `active`       | Boolean                              |                                            |
| `x_studio_sequence`                     | `sequence`     | Integer                              |                                            |
| `x_studio_portfolio_type_hex_color`     | `hex_color`    | Char                                 | Hex Color                                  |
| `x_portfolio_entry_type_line_ids_9ce77` | `line_ids`     | One2many (portfolio.entry_type_line) | Lines                                      |

## Model: `portfolio.entry_type_line` (was `x_portfolio_entry_type_line_a6fe2`)

| Studio Field Name           | New Field Name  | Type                            | Notes                             |
| --------------------------- | --------------- | ------------------------------- | --------------------------------- |
| `x_portfolio_entry_type_id` | `entry_type_id` | Many2one (portfolio.entry_type) | Required                          |
| `x_studio_sequence`         | `sequence`      | Integer                         |                                   |
| `x_name`                    | `name`          | Char                            | Description, required, translated |

## Model: `portfolio.entry_state` (was `x_portfolio_entry_stat`)

| Studio Field Name                      | New Field Name | Type    | Notes                       |
| -------------------------------------- | -------------- | ------- | --------------------------- |
| `x_name`                               | `name`         | Char    | State, required, translated |
| `x_active`                             | `active`       | Boolean |                             |
| `x_studio_sequence`                    | `sequence`     | Integer |                             |
| `x_studio_portfolio_entry_state_color` | `state_color`  | Integer | State Color                 |
| `x_studio_state_color`                 | `color`        | Integer | State Color (merged)        |

## Cross-Module Field Relationships

The following fields use models from the `reference` module:

| Model                | Field                        | Related Model            |
| -------------------- | ---------------------------- | ------------------------ |
| `portfolio.solution` | `target_groups_personas`     | `reference.target_group` |
| `portfolio.solution` | `technologies_tools_methods` | `reference.technology`   |

The following field in `reference.reference` references `portfolio.solution` but is
commented out due to dependency direction (portfolio depends on reference):

| Model                 | Field                 | Related Model        | Status                                                   |
| --------------------- | --------------------- | -------------------- | -------------------------------------------------------- |
| `reference.reference` | `portfolio_solutions` | `portfolio.solution` | **TODO** (needs bridge module or dependency restructure) |
