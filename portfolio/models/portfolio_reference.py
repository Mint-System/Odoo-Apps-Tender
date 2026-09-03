# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioReference(models.Model):
    _name = "portfolio.reference"
    _description = "Reference"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(
        comodel_name="res.users", domain="[('share', '=', False)]", string="Puzzle Owner", tracking=True
    )
    image = fields.Binary(string="Image")
    sequence = fields.Integer()
    stage_id = fields.Many2one(
        comodel_name="portfolio.reference.stage",
        required=True,
        ondelete="restrict",
        group_expand="_read_group_stage_ids",
        tracking=True,
    )
    is_priority = fields.Boolean(string="High Priority")
    color = fields.Integer(string="Color")
    kanban_state = fields.Selection(
        selection=[("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")], string="Kanban State"
    )
    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer")
    short_reference = fields.Html(string="Short Reference")
    industry_ids = fields.Many2many(comodel_name="res.partner.industry", string="Industries")
    project_start = fields.Date(string="Duration From", tracking=True)
    project_end = fields.Date(string="Duration To", tracking=True)
    success_story = fields.Html(string="Success Story")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    project_volume = fields.Monetary(string="Project Volume", currency_field="currency_id", tracking=True)
    key_aspects = fields.Html(string="Key Aspects")
    website_tag_ids = fields.Many2many(comodel_name="portfolio.website.tag", string="Website Tags")
    technology_ids = fields.Many2many(comodel_name="portfolio.technology", string="Technologies, Tools & Methods")
    sales_reference = fields.Html(string="Sales Reference")
    used_for_opportunity_ids = fields.Many2many(
        comodel_name="crm.lead",
        relation="portfolio_reference_used_for_opportunity_rel",
        column1="reference_id",
        column2="opportunity_id",
        string="Used For Opportunities",
        tracking=True,
    )
    testimonial = fields.Html(string="Testimonial")
    testimonial_by = fields.Char(string="Testimonial By")
    customer_contact_id = fields.Many2one(comodel_name="res.partner", string="Sales Reference Contact", tracking=True)
    portrait_image = fields.Binary(string="Portrait Image")
    service_type_ids = fields.Many2many(comodel_name="portfolio.service.type", string="Service Types")
    opportunity_ids = fields.Many2many(
        comodel_name="crm.lead",
        relation="portfolio_reference_opportunity_rel",
        column1="reference_id",
        column2="opportunity_id",
        string="Bases On",
        tracking=True,
    )
    project_volume_days = fields.Integer(string="Project Volume (Days)", tracking=True)
    portfolio_solution_ids = fields.Many2many(comodel_name="portfolio.portfolio", string="Portfolio Solutions")
    customer_owner_id = fields.Many2one(comodel_name="res.partner", string="Customer Owner", tracking=True)
    usage_type = fields.Selection(
        selection=[
            ("internalOnly", "Internal Use Only"),
            ("generalUse", "Unrestricted Usage"),
            ("restrictedUse", "Restricted Usage"),
        ],
        string="Allowed Usage",
        tracking=True,
    )
    channel_ids = fields.Many2many(comodel_name="portfolio.reference.channel", string="Allowed Channels", tracking=True)
    member_ids = fields.Many2many(comodel_name="res.users", string="Members Involved", tracking=True)
    website_url = fields.Char(string="Published Website URL")
    tag_ids = fields.Many2many(comodel_name="portfolio.reference.tag", string="Tags")

    def _read_group_stage_ids(self, stages, domain):
        return self.env["portfolio.reference.stage"].search([])
