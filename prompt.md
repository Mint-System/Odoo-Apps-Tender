---
title: "Fix security and access rules"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-09
model: moonshotai/Kimi-K2.6
input_tokens: 27708
output_tokens: 4729
---

# Fix security and access rules

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

### Reference

I have installed the `addons/tender/reference` app. When I remove my user from the the
security groups I can still see the app.

Ensure that the app is not visible if a user is not in group User or Admin.

Note that the module shows `res.partner.industry` in the configuration. Assume the user
has access to this model. Nonetheless the menu entry should not be visible if the user
does not have access to reference.

### Portfolio

I have installed the `addons/tender/portfolio` app. When I remove my user from the the
security groups I can still see the app and the the module creates another menu entry
for `reference`.

- reference.menu_root -> Correct
- portfolio.menu_references_root -> Not needed

Remove the menu structure created from `portfolio`.

Note that the module shows `res.partner.industry` in the configuration. Assume the user
has access to this model. Nonetheless the menu entry should not be visible if the user
does not have access to portflio.

## Worklog

- Fixed `reference` module:
  - `views/reference_menus.xml`: Changed `reference.menu_root` groups from
    `sales_team.group_sale_manager,base.group_user` to
    `reference.group_user,reference.group_manager` so the app is only visible to
    Reference users and admins.
  - `security/ir.model.access.csv`: Replaced all `base.group_user` and
    `base.group_erp_manager` references with `reference.group_user` and
    `reference.group_manager`, ensuring model access is gated by the module-specific
    groups.
- Fixed `portfolio` module:
  - `views/menu.xml`: Changed `menu_portfolio_root` groups from `base.group_user` to
    `portfolio.group_user,portfolio.group_manager`, so the Portfolio app is only visible
    to Portfolio users and admins.
  - `views/menu.xml`: Removed the entire duplicate "References App" menu structure
    (`menu_references_root` and all its children), as the Reference module already
    provides `reference.menu_root`.

@Clanker Set frontmatter state to completed and update date and model. If you have
access to session info also add token count.
