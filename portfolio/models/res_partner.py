# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    contact_user_ids = fields.Many2many(comodel_name="res.users", string="Contact Of")
    industry_ids = fields.Many2many(comodel_name="res.partner.industry", string="Industries")
    target_group_ids = fields.Many2many(
        comodel_name="portfolio.target.group",
        relation="res_partner_target_group_rel",
        column1="partner_id",
        column2="target_group_id",
        string="Target Groups (Personas)",
    )
    company_target_group_ids = fields.Many2many(
        comodel_name="portfolio.target.group",
        relation="res_partner_company_target_group_rel",
        column1="partner_id",
        column2="target_group_id",
        string="Target Groups",
    )
    contact_type_id = fields.Many2one(comodel_name="portfolio.contact.type", string="Contact Type", tracking=True)
    account_manager_id = fields.Many2one(comodel_name="res.users", string="Account Manager", tracking=True)
    executive_sponsor_id = fields.Many2one(comodel_name="res.users", string="Executive Sponsor", tracking=True)
    account_level_id = fields.Many2one(comodel_name="portfolio.account.level", string="Account Level", tracking=True)
    customer_satisfaction = fields.Float(string="Customer Satisfaction", tracking=True)
    partner_manager_id = fields.Many2one(comodel_name="res.users", string="Partner Manager", tracking=True)
    partner_level_id = fields.Many2one(comodel_name="portfolio.partner.level", string="Partner Level")
    partner_score = fields.Float(string="Partner Score", tracking=True)
    technology_ids = fields.Many2many(comodel_name="portfolio.technology", string="Partner Topics", tracking=True)
    partner_sponsor_id = fields.Many2one(comodel_name="res.users", string="Partner Sponsor", tracking=True)
