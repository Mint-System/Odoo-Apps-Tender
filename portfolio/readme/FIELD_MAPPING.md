# Field Mapping

This document maps the original Odoo Studio field names to the new field names used in the `portfolio` module.

## Models

| Studio Model | Module Model | Description |
|---|---|---|
| `x_solutions` | `portfolio.portfolio` | Solutions Portfolio |
| `x_solutions_stage` | `portfolio.stage` | Portfolio Stage |
| `x_references` | `portfolio.reference` | Reference & Success Story |
| `x_references_stage` | `portfolio.reference.stage` | Reference Stage |
| `x_website_tags` | `portfolio.website.tag` | Website Tag |
| `x_technologies` | `portfolio.technology` | Technology, Tool & Method |
| `x_service_types` | `portfolio.service.type` | Service Type |
| `x_reference_channels` | `portfolio.reference.channel` | Reference Channel |
| `x_reference_tags` | `portfolio.reference.tag` | Reference Tag |
| `x_target_group` | `portfolio.target.group` | Target Group |
| `x_bcg_matrix` | `portfolio.bcg.matrix` | BCG Matrix |
| `x_solutions_tag` | `portfolio.tag` | Portfolio Tag |
| `x_solutions_goals_acti` | `portfolio.goal.task` | Goal & Key Task |
| `x_solutions_goals_acti_stage` | `portfolio.goal.task.stage` | Goal & Task Stage |
| `x_solutions_goals_acti_tag` | `portfolio.goal.task.tag` | Goal & Task Tag |
| `x_contact_type` | `portfolio.contact.type` | Contact Type |
| `x_contact_type_line_ac124` | `portfolio.contact.type.line` | Contact Type Line |
| `x_account_level` | `portfolio.account.level` | Account Level |
| `x_account_level_line_ef13c` | `portfolio.account.level.line` | Account Level Line |
| `x_partner_level` | `portfolio.partner.level` | Partner Level |
| `x_partner_level_line_e603e` | `portfolio.partner.level.line` | Partner Level Line |
| `x_portfolio_entry_type` | `portfolio.entry.type` | Portfolio Entry Type |
| `x_portfolio_entry_type_line_a6fe2` | `portfolio.entry.type.line` | Portfolio Entry Type Line |
| `x_portfolio_entry_stat` | `portfolio.entry.state` | Portfolio Entry State |

## portfolio.portfolio

| Studio Field | Module Field | Type |
|---|---|---|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_user_id` | `user_id` | Many2one (res.users) |
| `x_studio_notes` | `notes` | Html |
| `x_studio_image` | `image` | Binary |
| `x_studio_sequence` | `sequence` | Integer |
| `x_studio_stage_id` | `stage_id` | Many2one (portfolio.stage) |
| `x_studio_priority` | `is_priority` | Boolean |
| `x_color` | `color` | Integer |
| `x_studio_kanban_state` | `kanban_state` | Selection |
| `x_studio_description_long` | `description_long` | Html |
| `x_studio_description` | `description` | Text |
| `x_studio_html_field_2bb_1jd0oa5so` | `content` | Html |
| `x_studio_links` | `links` | Html |
| `x_studio_target_groups_personas` | `target_group_ids` | Many2many |
| `x_studio_target_industries` | `target_industry_ids` | Many2many |
| `x_studio_technologies_tools_methods` | `technology_ids` | Many2many |
| `x_studio_bcg_matrix_present` | `bcg_matrix_id` | Many2one |
| `x_studio_goal_bcg_matrix` | `bcg_matrix_goal_id` | Many2one |
| `x_studio_present_bcg_matrix` | `bcg_matrix_current_id` | Many2one |
| `x_studio_today_bcg_matrix` | `bcg_matrix_today_id` | Many2one |
| `x_studio_tags` | `tag_ids` | Many2many |
| `x_studio_divisions` | `division_ids` | Many2many |
| `x_studio_goals` | `goal_ids` | One2many |
| `x_studio_key_tasks` | `key_task_ids` | One2many |
| `x_studio_key_members` | `key_member_ids` | Many2many |
| `x_studio_partners` | `partner_ids` | Many2many |
| `x_studio_bricks` | `product_ids` | Many2many |
| `x_studio_solution_lead_stv` | `lead_deputy_id` | Many2one |
| `x_studio_portfolio_entry_type` | `entry_type_id` | Many2one |
| `x_studio_portfolio_type_hex_color` | `type_hex_color` | Char (related) |
| `x_studio_revenue_current` | `revenue_current` | Integer |
| `x_studio_revenue_target` | `revenue_target` | Integer |
| `x_studio_profit_margin` | `profit_margin` | Float |
| `x_studio_next_review` | `next_review` | Date |
| `x_studio_next_milestone_date` | `next_milestone_date` | Date |
| `x_studio_next_milestone` | `next_milestone` | Char |
| `x_studio_product_partner_manager` | `product_partner_manager_id` | Many2one |
| `x_studio_portfolio_entry_state` | `entry_state_id` | Many2one |
| `x_studio_portfolio_entry_state_color` | `entry_state_color` | Integer (related) |
| `x_studio_knowledge_article` | `knowledge_article_id` | Many2one |

## portfolio.reference

| Studio Field | Module Field | Type |
|---|---|---|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_user_id` | `user_id` | Many2one |
| `x_studio_image` | `image` | Binary |
| `x_studio_sequence` | `sequence` | Integer |
| `x_studio_stage_id` | `stage_id` | Many2one |
| `x_studio_priority` | `is_priority` | Boolean |
| `x_color` | `color` | Integer |
| `x_studio_kanban_state` | `kanban_state` | Selection |
| `x_studio_customer` | `customer_id` | Many2one |
| `x_studio_short_reference` | `short_reference` | Html |
| `x_studio_industries` | `industry_ids` | Many2many |
| `x_studio_project_start` | `project_start` | Date |
| `x_studio_project_end` | `project_end` | Date |
| `x_studio_success_story` | `success_story` | Html |
| `x_studio_currency_id` | `currency_id` | Many2one |
| `x_studio_project_volume` | `project_volume` | Monetary |
| `x_studio_key_aspects` | `key_aspects` | Html |
| `x_studio_website_tags` | `website_tag_ids` | Many2many |
| `x_studio_technologies` | `technology_ids` | Many2many |
| `x_studio_sales_reference` | `sales_reference` | Html |
| `x_studio_used_for_opportunities` | `used_for_opportunity_ids` | Many2many |
| `x_studio_testimonial` | `testimonial` | Html |
| `x_studio_testimonial_by` | `testimonial_by` | Char |
| `x_studio_customer_contact` | `customer_contact_id` | Many2one |
| `x_studio_portrait_image` | `portrait_image` | Binary |
| `x_studio_service_types` | `service_type_ids` | Many2many |
| `x_studio_bases_on` | `opportunity_ids` | Many2many |
| `x_studio_project_volume_days` | `project_volume_days` | Integer |
| `x_studio_portfolio_solutions` | `portfolio_solution_ids` | Many2many |
| `x_studio_customer_owner` | `customer_owner_id` | Many2one |
| `x_studio_how_usable` | `usage_type` | Selection |
| `x_studio_channels` | `channel_ids` | Many2many |
| `x_studio_members_involved` | `member_ids` | Many2many |
| `x_studio_published_website_url` | `website_url` | Char |
| `x_studio_tags` | `tag_ids` | Many2many |

## portfolio.goal.task

| Studio Field | Module Field | Type |
|---|---|---|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_user_id` | `user_id` | Many2one |
| `x_studio_currency_id` | `currency_id` | Many2one |
| `x_studio_value` | `value` | Monetary |
| `x_studio_sequence` | `sequence` | Integer |
| `x_studio_stage_id` | `stage_id` | Many2one |
| `x_studio_priority` | `is_priority` | Boolean |
| `x_color` | `color` | Integer |
| `x_studio_kanban_state` | `kanban_state` | Selection |
| `x_studio_tag_ids` | `tag_ids` | Many2many |
| `x_studio_solution` | `portfolio_id` | Many2one |
| `x_studio_start_date` | `start_date` | Date |
| `x_studio_due_date` | `due_date` | Date |
| `x_studio_periode` | `period_date` | Date |
| `x_studio_type` | `task_type` | Selection |
| `x_studio_indicator` | `indicator` | Selection |
| `x_studio_commit_text` | `commit_text` | Text |
| `x_studio_target_text` | `target_text` | Text |
| `x_studio_description` | `description` | Html |
| `x_studio_commit_num` | `commit_num` | Integer |
| `x_studio_target_num` | `target_num` | Integer |
| `x_studio_closing_comment` | `closing_comment` | Text |

## Other Models

All other configuration models follow the same simple pattern:

| Studio Field | Module Field | Type |
|---|---|---|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_sequence` | `sequence` | Integer |
| `x_studio_description` | `description` | Html / Char |
| `x_studio_notes` | `notes` | Html |
| `x_studio_image` | `image` | Binary |
| `x_studio_category` | `category_id` | Many2one |
| `x_studio_color` | `color` | Integer |
| `x_studio_user_id` | `user_id` | Many2one |
| `x_studio_portfolio_type_hex_color` | `hex_color` | Char |
| `x_studio_portfolio_entry_state_color` | `color` | Integer |
| Line parent IDs | `contact_type_id`, `account_level_id`, `partner_level_id`, `entry_type_id` | Many2one |
| Line inverse names | `line_ids` | One2many |

## Inherited Models

### res.partner

| Studio Field | Module Field | Type |
|---|---|---|
| `x_studio_contact_of` | `contact_user_ids` | Many2many (res.users) |
| `x_studio_industries` | `industry_ids` | Many2many |
| `x_studio_target_group` | `target_group_ids` | Many2many |
| `x_studio_target_groups` | `company_target_group_ids` | Many2many |
| `x_studio_contact_type_field` | `contact_type_id` | Many2one |
| `x_studio_account_manager_field` | `account_manager_id` | Many2one |
| `x_studio_executive_account_manager` | `executive_sponsor_id` | Many2one |
| `x_studio_account_level` | `account_level_id` | Many2one |
| `x_studio_customer_satisfaction` | `customer_satisfaction` | Float |
| `x_studio_partner_manager` | `partner_manager_id` | Many2one |
| `x_studio_partner_level` | `partner_level_id` | Many2one |
| `x_studio_partner_score` | `partner_score` | Float |
| `x_studio_partner_topics` | `technology_ids` | Many2many |
| `x_studio_partner_sponsor` | `partner_sponsor_id` | Many2one |

### crm.lead

| Studio Field | Module Field | Type |
|---|---|---|
| `x_studio_solutions` | `portfolio_solution_ids` | Many2many |
| `x_studio_divisions` | `division_ids` | Many2many |
| `x_studio_referral_by` | `referral_partner_id` | Many2one |

### res.partner.category

| Studio Field | Module Field | Type |
|---|---|---|
| `x_studio_description` | `description` | Text |
