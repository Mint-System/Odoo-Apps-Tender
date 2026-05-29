# Field Mapping Table: Studio Fields to Reference Module Fields

This document maps the original Odoo Studio field names (with `x_` and `x_studio`
prefixes) to the new clean field names used in the `reference` module.

## Model: `reference.reference` (was `x_references`)

| Studio Field Name                 | New Field Name           | Type                               | Notes                                         |
| --------------------------------- | ------------------------ | ---------------------------------- | --------------------------------------------- |
| `x_name`                          | `name`                   | Char                               | Title, required, translated                   |
| `x_active`                        | `active`                 | Boolean                            |                                               |
| `x_studio_user_id`                | `user_id`                | Many2one (res.users)               | Puzzle Owner                                  |
| `x_studio_image`                  | `image`                  | Binary                             |                                               |
| `x_studio_sequence`               | `sequence`               | Integer                            |                                               |
| `x_studio_stage_id`               | `stage_id`               | Many2one (reference.stage)         | Required                                      |
| `x_studio_priority`               | `priority`               | Boolean                            | High Priority                                 |
| `x_color`                         | `color`                  | Integer                            |                                               |
| `x_studio_kanban_state`           | `kanban_state`           | Selection                          | normal/done/blocked                           |
| `x_studio_customer`               | `customer`               | Many2one (res.partner)             |                                               |
| `x_studio_short_reference`        | `short_reference`        | Html                               |                                               |
| `x_studio_industries`             | `industries`             | Many2many (res.partner.industry)   |                                               |
| `x_studio_project_start`          | `project_start`          | Date                               | Duration from                                 |
| `x_studio_project_end`            | `project_end`            | Date                               | Duration to                                   |
| `x_studio_success_story`          | `success_story`          | Html                               |                                               |
| `x_studio_currency_id`            | `currency_id`            | Many2one (res.currency)            |                                               |
| `x_studio_project_volume`         | `project_volume`         | Monetary                           |                                               |
| `x_studio_key_aspects`            | `key_aspects`            | Html                               |                                               |
| `x_studio_website_tags`           | `website_tags`           | Many2many (reference.website_tag)  |                                               |
| `x_studio_technologies`           | `technologies`           | Many2many (reference.technology)   |                                               |
| `x_studio_sales_reference`        | `sales_reference`        | Html                               |                                               |
| `x_studio_used_for_opportunities` | `used_for_opportunities` | Many2many (crm.lead)               |                                               |
| `x_studio_testimonial`            | `testimonial`            | Html                               |                                               |
| `x_studio_testimonial_by`         | `testimonial_by`         | Char                               |                                               |
| `x_studio_customer_contact`       | `customer_contact`       | Many2one (res.partner)             | Sales Reference Contact                       |
| `x_studio_portrait_image`         | `portrait_image`         | Binary                             |                                               |
| `x_studio_service_types`          | `service_types`          | Many2many (reference.service_type) |                                               |
| `x_studio_bases_on`               | `bases_on`               | Many2many (crm.lead)               |                                               |
| `x_studio_project_volume_days`    | `project_volume_days`    | Integer                            |                                               |
| `x_studio_portfolio_solutions`    | `portfolio_solutions`    | Many2many                          | **Commented out** (requires portfolio module) |
| `x_studio_customer_owner`         | `customer_owner`         | Many2one (res.partner)             |                                               |
| `x_studio_how_usable`             | `how_usable`             | Selection                          | Allowed usage                                 |
| `x_studio_channels`               | `channels`               | Many2many (reference.channel)      |                                               |
| `x_studio_puzzle_owner`           | `puzzle_owner`           | Many2one (res.users)               | Old/alternative field                         |
| `x_studio_members_involved`       | `members_involved`       | Many2many (res.users)              |                                               |
| `x_studio_published_website_url`  | `published_website_url`  | Char                               |                                               |
| `x_studio_tags`                   | `tags`                   | Many2many (reference.tag)          |                                               |

## Model: `reference.stage` (was `x_references_stage`)

| Studio Field Name   | New Field Name | Type    | Notes                            |
| ------------------- | -------------- | ------- | -------------------------------- |
| `x_name`            | `name`         | Char    | Stage Name, required, translated |
| `x_studio_sequence` | `sequence`     | Integer |                                  |

## Model: `reference.website_tag` (was `x_website_tags`)

| Studio Field Name   | New Field Name | Type                             | Notes                          |
| ------------------- | -------------- | -------------------------------- | ------------------------------ |
| `x_name`            | `name`         | Char                             | Required, translated           |
| `x_active`          | `active`       | Boolean                          |                                |
| `x_studio_category` | `category`     | Many2one (reference.website_tag) | Self-reference                 |
| `x_studio_color`    | `color`        | Integer                          |                                |
| `x_color`           | `color`        | Integer                          | Merged into single color field |

## Model: `reference.technology` (was `x_technologies`)

| Studio Field Name                      | New Field Name | Type                            | Notes                                |
| -------------------------------------- | -------------- | ------------------------------- | ------------------------------------ |
| `x_name`                               | `name`         | Char                            | Required, translated                 |
| `x_active`                             | `active`       | Boolean                         |                                      |
| `x_studio_user_id`                     | `user_id`      | Many2one (res.users)            | Responsible                          |
| `x_studio_category`                    | `category`     | Many2one (reference.technology) | Self-reference                       |
| `x_studio_integer_field_63m_1jd1dnjmh` | —              | Integer                         | **Removed** (unused generated field) |
| `x_studio_color`                       | `color`        | Integer                         |                                      |

## Model: `reference.service_type` (was `x_service_types`)

| Studio Field Name   | New Field Name | Type    | Notes                |
| ------------------- | -------------- | ------- | -------------------- |
| `x_name`            | `name`         | Char    | Required, translated |
| `x_active`          | `active`       | Boolean |                      |
| `x_studio_sequence` | `sequence`     | Integer |                      |

## Model: `reference.channel` (was `x_reference_channels`)

| Studio Field Name   | New Field Name | Type    | Notes                |
| ------------------- | -------------- | ------- | -------------------- |
| `x_name`            | `name`         | Char    | Required, translated |
| `x_active`          | `active`       | Boolean |                      |
| `x_studio_sequence` | `sequence`     | Integer |                      |

## Model: `reference.tag` (was `x_reference_tags`)

| Studio Field Name | New Field Name | Type    | Notes                |
| ----------------- | -------------- | ------- | -------------------- |
| `x_name`          | `name`         | Char    | Required, translated |
| `x_active`        | `active`       | Boolean |                      |

## Model: `reference.target_group` (was `x_target_group`)

| Studio Field Name   | New Field Name | Type                              | Notes                          |
| ------------------- | -------------- | --------------------------------- | ------------------------------ |
| `x_name`            | `name`         | Char                              | Required, translated           |
| `x_active`          | `active`       | Boolean                           |                                |
| `x_studio_notes`    | `notes`        | Html                              |                                |
| `x_studio_image`    | `image`        | Binary                            |                                |
| `x_studio_sequence` | `sequence`     | Integer                           |                                |
| `x_studio_category` | `category`     | Many2one (reference.target_group) | Self-reference                 |
| `x_studio_color`    | `color`        | Integer                           |                                |
| `x_color`           | `color`        | Integer                           | Merged into single color field |
