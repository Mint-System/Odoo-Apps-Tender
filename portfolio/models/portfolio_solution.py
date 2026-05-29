# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioSolution(models.Model):
    _name = "portfolio.solution"
    _description = "Solution"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "priority desc, sequence asc, id desc"

    name = fields.Char(string="Solution Name", required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one("res.users", string="Owner", domain="[('share', '=', False)]", tracking=True)
    notes = fields.Html(string="Notes")
    image = fields.Binary(string="Image")
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "portfolio.solution_stage",
        string="Stage",
        required=True,
        tracking=True,
        group_expand="_group_expand_stages",
        ondelete="restrict",
    )
    priority = fields.Boolean(string="High Priority")
    color = fields.Integer(string="Color")
    kanban_state = fields.Selection(
        [
            ("draft", "in Development / Draft"),
            ("done", "Active"),
            ("blocked", "Blocked"),
        ],
        string="Kanban State",
        default="draft",
    )
    description_long = fields.Html(string="Description (extended)")
    description = fields.Text(string="Description", tracking=True)
    target_groups_personas = fields.Many2many(
        "reference.target_group",
        string="Target Groups / Personas",
        relation="portfolio_solution_target_group_rel",
        help="Important target groups and personas",
        tracking=True,
    )
    target_industries = fields.Many2many(
        "res.partner.industry",
        string="Target Industries",
        relation="portfolio_solution_industry_rel",
        help="Important targeted industries",
        tracking=True,
    )
    divisions = fields.Many2many(
        "res.partner", string="Bases / Divisions", relation="portfolio_solution_division_rel", tracking=True
    )
    tags = fields.Many2many(
        "portfolio.solution_tag", string="Tags", relation="portfolio_solution_tag_rel", tracking=True
    )
    technologies_tools_methods = fields.Many2many(
        "reference.technology",
        string="Technologies, Tools & Methods",
        relation="portfolio_solution_technology_rel",
        tracking=True,
    )
    bcgs_matrix_present = fields.Many2one("portfolio.bcg_matrix", string="BCG Matrix (Present)")
    goal_bcg_matrix = fields.Many2one("portfolio.bcg_matrix", string="BCG Matrix: Goal", tracking=True)
    today_bcg_matrix = fields.Many2one("portfolio.bcg_matrix", string="BCG Matrix: Today", tracking=True)
    entry_type = fields.Many2one("portfolio.entry_type", string="Type")
    entry_state = fields.Many2one(
        "portfolio.entry_state", string="Status/Health", help="On Track / At Risk / Off Track"
    )
    entry_state_color = fields.Integer(string="State Color", compute="_compute_entry_state_color", store=True)
    hex_color = fields.Char(string="Color", related="entry_type.hex_color", readonly=True)
    revenue_current = fields.Integer(string="Current Revenue [CHF]", help="Laufendes Jahr")
    revenue_target = fields.Integer(string="Revenue Target [CHF]", help="Jahresziel (aus OKR)")
    profit_margin = fields.Float(string="Profit margin [%]", help="Aktuelle Marge")
    next_review = fields.Date(string="Next review", help="Quartalsweise Reviews")
    next_milestone_date = fields.Date(string="Next milestone", help="z.B. 'Gate Review Scale', 'Launch Q3'")
    next_milestone = fields.Char(string="Next milestone", help="z.B. 'Gate Review Scale', 'Launch Q3'")
    solution_lead_stv = fields.Many2one("res.users", string="Lead Stv.", help="Stellvertretung", tracking=True)
    product_partner_manager = fields.Many2one("res.users", string="Partner Manager")
    key_members = fields.Many2many(
        "res.users", string="Key Members", relation="portfolio_solution_key_members_rel", tracking=True
    )
    partners = fields.Many2many(
        "res.partner", string="Partners", relation="portfolio_solution_partner_rel", tracking=True
    )
    bricks = fields.Many2many(
        "product.template", string="Bricks", relation="portfolio_solution_product_rel", tracking=True
    )
    goal_ids = fields.One2many(
        "portfolio.goal_task",
        "solution_id",
        string="Goals",
        domain=lambda self: ["&", "|", ("stage_id", "in", [2]), ("stage_id", "in", [1]), ("type", "=", "goal")],
        tracking=True,
    )
    key_task_ids = fields.One2many(
        "portfolio.goal_task",
        "solution_id",
        string="Key Tasks",
        domain=lambda self: ["&", "|", ("stage_id", "in", [2]), ("stage_id", "in", [1]), ("type", "=", "task")],
        tracking=True,
    )
    links = fields.Html(string="Links")

    @api.depends("entry_state")
    def _compute_entry_state_color(self):
        for rec in self:
            if rec.entry_state:
                rec.entry_state_color = rec.entry_state.state_color
            else:
                rec.entry_state_color = 0

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)
