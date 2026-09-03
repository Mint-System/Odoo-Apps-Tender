# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTask(models.Model):
    _name = "portfolio.goal.task"
    _description = "Goal and Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(
        comodel_name="res.users", domain="[('share', '=', False)]", string="Responsible", tracking=True
    )
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    value = fields.Monetary(string="Value", currency_field="currency_id", tracking=True)
    sequence = fields.Integer()
    stage_id = fields.Many2one(
        comodel_name="portfolio.goal.task.stage",
        required=True,
        ondelete="restrict",
        group_expand="_read_group_stage_ids",
        tracking=True,
    )
    is_priority = fields.Boolean(string="High Priority")
    color = fields.Integer(string="Color")
    kanban_state = fields.Selection(
        selection=[("normal", "In Development / Draft"), ("done", "Active"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    tag_ids = fields.Many2many(comodel_name="portfolio.goal.task.tag", string="Tags", tracking=True)
    portfolio_id = fields.Many2one(comodel_name="portfolio.portfolio", string="Solution", tracking=True)
    start_date = fields.Date(string="Start Date", tracking=True)
    due_date = fields.Date(string="Due Date", tracking=True)
    period_date = fields.Date(string="Period")
    task_type = fields.Selection(
        selection=[("goal", "Goal"), ("task", "Key Task")],
        string="Type",
        tracking=True,
    )
    _indicator_selection = [
        ("Qualitative", "Qualitative"),
        ("Revenue", "Revenue"),
        ("FTE", "FTE"),
        ("Customers", "Customers"),
        ("Other", "Other"),
    ]
    indicator = fields.Selection(
        selection=_indicator_selection,
        string="Indicator",
        tracking=True,
    )
    commit_text = fields.Text(string="Commit (Text)", tracking=True)
    target_text = fields.Text(string="Target (Text)", tracking=True)
    description = fields.Html(string="Description", tracking=True)
    commit_num = fields.Integer(string="Commit (Num)", tracking=True)
    target_num = fields.Integer(string="Target (Num)", tracking=True)
    closing_comment = fields.Text(string="Closing Comment", tracking=True)

    def _read_group_stage_ids(self, stages, domain):
        return self.env["portfolio.goal.task.stage"].search([])
