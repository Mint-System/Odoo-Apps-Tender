---
commit_ref:
title: "Double check model and fields"
author: "Janik von Rotz <login@janikvonrotz.ch>"
session_id:
action: execute
state: draft
date_completed: YYYY-MM-DD
harness:
provider:
model:
input_tokens:
output_tokens:
---

# Double check model and fields

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` to get an understanding of the project
- Read task section and prepare a list of todos
- Update the todo list while working on task

@Clanker When task is completed set frontmatter state to review. If you have access to session info add token count and session id. Prompt the author to verify the results.

## Task

I want you to verify that models of two modules that I have generated from Odoo studio customisations do match.

The customisations are in `tmp/studio_customization/data`.

The models for portfolio are `portfolio/models` and for reference `reference/models`.

Note that the studio customisations contain both. Report any discrepancies.

### Issue install

When I tried to isntall the module on another Odoo enviroment I got this error:

```
ParseError('while parsing %s:%s, somewhere inside\n%s' % ( odoo.tools.convert.ParseError: while parsing /var/lib/odoo/git/github.com/Mint-System/Odoo-Apps-Tender/reference/demo/demo.xml:28, somewhere inside <record id="demo_user_puzzle_member" model="res.users" context="{'no_reset_password': True}"> <field name="name">Puzzle Member (Demo)</field> <field name="login">odoo+demo@puzzle.ch</field> <field name="email">odoo+demo@puzzle.ch</field> <field name="group_ids" eval="[(6, 0, [ref('base.group_user')])]"/> </record> 
```

Demo data is not enabled. Why is trying to load demo data? Is there a real issue with demo data?

### Report remove customisations

Then I would like to know how I can remove the customisation once I have installed the modules and moved data.

Please create a list of records per model that I have to delete to get rid of the reference/portfolio customisations.

Also make sure the order is correct.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info update token count. Finally, update the changelog with the most important changes.
