---
title: "Create demo data for Reference app"
state: completed
---

# Run 04

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

It was built in run
`addons/tender/prompts/03_migrate-references-odoo-studio-app-to-module.md` from Odoo
Studio app with the name "References". The export all Studio customisations are stored
here `$HOME/Odoo-Build/tmp/customizations/studio_customization/data`.

Your goal is to create demo xml data for a reference and linked instances like tags and
so on. The demo data should be stored in `addons/tender/reference/demo/demo.xml`.

The source for demo data are exports from a live system. they are stored in
`$HOME/Odoo-Build/tmp/customizations/studio_customization/demo_data`. The main export
file for the demo reference is `references.csv`. The columns of these in file denote
relations to other models of the reference app created in
`addons/tender/prompts/03_migrate-references-odoo-studio-app-to-module.md` . Take into
account that field names were changed when the reference module was created fro Odoo
studio customization.

The data of related models are in the excel files in
`$HOME/Odoo-Build/tmp/customizations/studio_customization/demo_data`.

For `reference.website.tag` and `reference.technology` create only minimum instances for
working demo reference.

The default stage needed for a reference even if no demo data are provided is
`New (Short Reference)`. It should be stored in
`addons/tender/reference/data/reference_stage_data.xml`.

The industries data are odoo standard industries defined in
`odoo/addons/base/data/res_partner_data.xml` so there is no need to create them. Just
link to these industries instances.

## Worklog

- Read and parsed the main CSV export `references.csv` containing the demo reference
  instance "Demo Referenz XY". Columns were mapped from Studio field names to the clean
  module field names using `FIELD_MAPPING.md`.
- Parsed all related-model Excel exports (xlsx files) by unzipping and reading the Open
  XML format.
- **Generated `reference/demo/demo.xml`** containing:
  - 1 demo `reference.reference` record with all fields (dates, volumes, HTML
    descriptions in `CDATA`, usage type, website URL, etc.) and mapped relations.
  - 2 demo `res.users`: "Puzzle Member (Demo)" (also set as `user_id` and `member_ids`)
    and "Bernhard Wyss" (set as `puzzle_owner_id`).
  - 3 demo `res.partner` records: customer "Muster AG", contact "Max Meister", and
    customer owner "Martin Müller".
  - 6 demo `reference.stage` records (sequence 0–5) from the stages export.
  - 8 demo `reference.channel` records from the channels export.
  - 1 demo `reference.website.tag` record ("Digital Transformation") — the minimum
    instance needed by the demo reference.
  - 4 demo `reference.technology` records (Memcached, Jenkins, Odoo, Odoo Studio) — the
    minimum instances needed by the demo reference.
  - 6 demo `reference.service.type` records from the service types export.
- **Fixed Odoo 19 compatibility**: changed `groups_id` → `group_ids` on `res.users` demo
  records.
- **Removed duplicate industries** from `demo.xml`. The base module already creates
  standard NOGA `res.partner.industry` records in `data/res_partner_data.xml`; creating
  them again would produce 42 entries (21 base + 21 duplicate). Updated the demo
  reference to link to the existing `base.res_partner_industry_P` for Education.
- **Updated `data/reference_stage_data.xml`**: renamed the default stage to "New (Short
  Reference)" and set its sequence to `eval="0"` to match the stage export.
- Ensured all HTML/special-character content is wrapped in `CDATA` to avoid XML parsing
  issues.
