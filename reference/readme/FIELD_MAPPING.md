# Field Mapping

## Overview

This document tracks the mapping between original Odoo Studio field/model names and the new names in the `reference` module.

## Notes

- `x_stories_tags` model is referenced by a Studio menu/action but does not appear in the model export (no `ir.model` record, no fields, no views). It is omitted from this module.
- `x_studio_portfolio_solutions` (M2M to `x_solutions`) is omitted because `x_solutions` belongs to the "Portfolio" app and is not included in this module.
- Standard models such as `res.partner.industry` are used as-is and not recreated.

## Models

| Studio Model | New Model | Notes |
|--------------|-----------|-------|
| `x_references` | `reference.reference` | Main model |
| `x_references_stage` | `reference.stage` | |
| `x_website_tags` | `reference.website.tag` | |
| `x_technologies` | `reference.technology` | |
| `x_service_types` | `reference.service.type` | |
| `x_reference_channels` | `reference.channel` | |
| `x_reference_tags` | `reference.tag` | |
| `x_target_group` | `reference.target.group` | Also used by Contacts app |

## Fields

### reference.reference (x_references)

| Studio Field | New Field | Type | Relation |
|--------------|-----------|------|----------|
| `x_name` | `name` | Char | |
| `x_active` | `active` | Boolean | |
| `x_color` | `color` | Integer | |
| `x_studio_sequence` | `sequence` | Integer | |
| `x_studio_stage_id` | `stage_id` | Many2one | `reference.stage` |
| `x_studio_kanban_state` | `kanban_state` | Selection | |
| `x_studio_user_id` | `user_id` | Many2one | `res.users` |
| `x_studio_puzzle_owner` | `puzzle_owner_id` | Many2one | `res.users` |
| `x_studio_members_involved` | `member_ids` | Many2many | `res.users` |
| `x_studio_image` | `image` | Binary (Image) | |
| `x_studio_portrait_image` | `portrait_image` | Binary (Image) | |
| `x_studio_short_reference` | `short_reference` | Html | |
| `x_studio_sales_reference` | `sales_reference` | Html | |
| `x_studio_key_aspects` | `key_aspects` | Html | |
| `x_studio_success_story` | `success_story` | Html | |
| `x_studio_testimonial` | `testimonial` | Html | |
| `x_studio_testimonial_by` | `testimonial_author` | Char | |
| `x_studio_customer` | `customer_id` | Many2one | `res.partner` |
| `x_studio_customer_contact` | `contact_id` | Many2one | `res.partner` |
| `x_studio_customer_owner` | `customer_owner_id` | Many2one | `res.partner` |
| `x_studio_published_website_url` | `website_url` | Char | |
| `x_studio_project_start` | `project_start` | Date | |
| `x_studio_project_end` | `project_end` | Date | |
| `x_studio_project_volume` | `project_volume` | Monetary | |
| `x_studio_project_volume_days` | `project_volume_days` | Integer | |
| `x_studio_currency_id` | `currency_id` | Many2one | `res.currency` |
| `x_studio_how_usable` | `usage_type` | Selection | |
| `x_studio_channels` | `channel_ids` | Many2many | `reference.channel` |
| `x_studio_industries` | `industry_ids` | Many2many | `res.partner.industry` |
| `x_studio_service_types` | `service_type_ids` | Many2many | `reference.service.type` |
| `x_studio_tags` | `tag_ids` | Many2many | `reference.tag` |
| `x_studio_technologies` | `technology_ids` | Many2many | `reference.technology` |
| `x_studio_website_tags` | `website_tag_ids` | Many2many | `reference.website.tag` |
| `x_studio_bases_on` | `opportunity_source_ids` | Many2many | `crm.lead` |
| `x_studio_used_for_opportunities` | `opportunity_usage_ids` | Many2many | `crm.lead` |
| `x_studio_priority` | `priority` | Boolean | |
| `x_studio_portfolio_solutions` | *omitted* | Many2many | `x_solutions` (Portfolio) |

### reference.stage (x_references_stage)

| Studio Field | New Field | Type |
|--------------|-----------|------|
| `x_name` | `name` | Char |
| `x_studio_sequence` | `sequence` | Integer |

### reference.website.tag (x_website_tags)

| Studio Field | New Field | Type | Notes |
|--------------|-----------|------|-------|
| `x_name` | `name` | Char | |
| `x_active` | `active` | Boolean | |
| `x_color` | `color` | Integer | Unused in views but preserved |
| `x_studio_category` | `category_id` | Many2one | Self-referential (`reference.website.tag`) |
| `x_studio_color` | `display_color` | Integer | Visible in list view |

### reference.technology (x_technologies)

| Studio Field | New Field | Type | Notes |
|--------------|-----------|------|-------|
| `x_name` | `name` | Char | |
| `x_active` | `active` | Boolean | |
| `x_studio_category` | `category_id` | Many2one | Self-referential (`reference.technology`) |
| `x_studio_color` | `color` | Integer | Visible in list view |
| `x_studio_integer_field_63m_1jd1dnjmh` | `sort_order` | Integer | Unused in views |
| `x_studio_user_id` | `user_id` | Many2one | `res.users` |

### reference.service.type (x_service_types)

| Studio Field | New Field | Type |
|--------------|-----------|------|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_sequence` | `sequence` | Integer |

### reference.channel (x_reference_channels)

| Studio Field | New Field | Type |
|--------------|-----------|------|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |
| `x_studio_sequence` | `sequence` | Integer |

### reference.tag (x_reference_tags)

| Studio Field | New Field | Type |
|--------------|-----------|------|
| `x_name` | `name` | Char |
| `x_active` | `active` | Boolean |

### reference.target.group (x_target_group)

| Studio Field | New Field | Type | Notes |
|--------------|-----------|------|-------|
| `x_name` | `name` | Char | |
| `x_active` | `active` | Boolean | |
| `x_studio_sequence` | `sequence` | Integer | |
| `x_color` | `color` | Integer | Unused in views |
| `x_studio_category` | `category_id` | Many2one | Self-referential (`reference.target.group`) |
| `x_studio_color` | `display_color` | Integer | Visible in list/form views |
| `x_studio_image` | `image` | Image | |
| `x_studio_notes` | `notes` | Html | |
