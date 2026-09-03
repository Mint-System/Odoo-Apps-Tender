# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioPortfolio(models.Model):
    _name = "portfolio.portfolio"
    _description = "Portfolio"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(comodel_name="res.users", domain="[('share', '=', False)]", string="Owner", tracking=True)
    notes = fields.Html()
    image = fields.Binary()
    sequence = fields.Integer()
    stage_id = fields.Many2one(
        comodel_name="portfolio.stage",
        required=True,
        ondelete="restrict",
        group_expand="_read_group_stage_ids",
        tracking=True,
    )
    is_priority = fields.Boolean(string="High Priority")
    color = fields.Integer()
    kanban_state = fields.Selection(
        selection=[("draft", "In Development / Draft"), ("done", "Active"), ("blocked", "Blocked")],
    )
    description_long = fields.Html(string="Description (Extended)")
    description = fields.Text(tracking=True)
    content = fields.Html()
    links = fields.Html()
    target_group_ids = fields.Many2many(
        comodel_name="portfolio.target.group", string="Target Groups / Personas", tracking=True
    )
    target_industry_ids = fields.Many2many(
        comodel_name="res.partner.industry", string="Target Industries", tracking=True
    )
    technology_ids = fields.Many2many(
        comodel_name="portfolio.technology", string="Technologies, Tools & Methods", tracking=True
    )
    bcg_matrix_id = fields.Many2one(comodel_name="portfolio.bcg.matrix", string="BCG Matrix (Present)")
    bcg_matrix_goal_id = fields.Many2one(comodel_name="portfolio.bcg.matrix", string="BCG Matrix: Goal", tracking=True)
    bcg_matrix_current_id = fields.Many2one(comodel_name="portfolio.bcg.matrix", string="BCG Matrix: Present")
    bcg_matrix_today_id = fields.Many2one(
        comodel_name="portfolio.bcg.matrix", string="BCG Matrix: Today", tracking=True
    )
    tag_ids = fields.Many2many(comodel_name="portfolio.tag", string="Tags", tracking=True)
    division_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="portfolio_portfolio_division_rel",
        column1="portfolio_id",
        column2="partner_id",
        string="Bases / Divisions",
        tracking=True,
    )
    goal_ids = fields.One2many(
        comodel_name="portfolio.goal.task",
        inverse_name="portfolio_id",
        domain="[('task_type', '=', 'goal')]",
        string="Goals",
        tracking=True,
    )
    key_task_ids = fields.One2many(
        comodel_name="portfolio.goal.task",
        inverse_name="portfolio_id",
        domain="[('task_type', '=', 'task')]",
        string="Key Tasks",
        tracking=True,
    )
    key_member_ids = fields.Many2many(
        comodel_name="res.users",
        relation="portfolio_portfolio_member_rel",
        column1="portfolio_id",
        column2="user_id",
        string="Key Members",
        tracking=True,
    )
    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="portfolio_portfolio_partner_rel",
        column1="portfolio_id",
        column2="partner_id",
        string="Partners",
        tracking=True,
    )
    product_ids = fields.Many2many(comodel_name="product.template", string="Bricks", tracking=True)
    lead_deputy_id = fields.Many2one(comodel_name="res.users", string="Lead Deputy", tracking=True)
    entry_type_id = fields.Many2one(comodel_name="portfolio.entry.type")
    type_hex_color = fields.Char(string="Type Color", related="entry_type_id.hex_color", readonly=True)
    revenue_current = fields.Integer(string="Current Revenue [CHF]")
    revenue_target = fields.Integer(string="Revenue Target [CHF]")
    profit_margin = fields.Float(string="Profit Margin [%]")
    next_review = fields.Date()
    next_milestone_date = fields.Date()
    next_milestone = fields.Char()
    product_partner_manager_id = fields.Many2one(comodel_name="res.users", string="Product Partner Manager")
    entry_state_id = fields.Many2one(comodel_name="portfolio.entry.state", string="Status/Health")
    entry_state_color = fields.Integer(string="State Color", related="entry_state_id.color", readonly=True)
    knowledge_article_id = fields.Many2one(comodel_name="knowledge.article")

    def _read_group_stage_ids(self, stages, domain):
        # pylint: disable=no-search-all
        return self.env["portfolio.stage"].search([])
