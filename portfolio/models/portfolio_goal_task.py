# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTask(models.Model):
    _name = "portfolio.goal_task"
    _description = "Goal & Key Task"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"

    name = fields.Char(string="Name", required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(
        "res.users", string="Responsible",
        domain="[('share', '=', False)]", tracking=True
    )
    currency_id = fields.Many2one("res.currency", string="Currency")
    value = fields.Monetary(string="Value", tracking=True)
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "portfolio.goal_task_stage", string="Stage",
        required=True, tracking=True,
        group_expand="_group_expand_stages", ondelete="restrict"
    )
    priority = fields.Boolean(string="High Priority")
    color = fields.Integer(string="Color")
    kanban_state = fields.Selection(
        [
            ("normal", "In Development / Draft"),
            ("done", "Active"),
            ("blocked", "Blocked"),
        ],
        string="Kanban State",
        default="normal",
    )
    tag_ids = fields.Many2many(
        "portfolio.goal_task_tag", string="Tags",
        relation="portfolio_goal_task_tag_rel", tracking=True
    )
    solution_id = fields.Many2one(
        "portfolio.solution", string="Solution", tracking=True
    )
    start_date = fields.Date(string="Time Period", tracking=True)
    due_date = fields.Date(string="Due Date", tracking=True)
    period = fields.Date(string="Periode")
    type = fields.Selection(
        [("goal", "Goal"), ("task", "Key Task")],
        string="Type",
        default="goal",
        tracking=True
    )
    indicator = fields.Selection(
        [
            ("Qualitative", "Qualitative"),
            ("Revenue", "Revenue"),
            ("FTE", "FTE"),
            ("Customers", "Customers"),
            ("Other", "Other"),
        ],
        string="Indicator",
        tracking=True
    )
    commit_text = fields.Text(string="Commit (Text)", tracking=True)
    target_text = fields.Text(string="Target (Text)", tracking=True)
    description = fields.Html(string="Description", tracking=True)
    commit_num = fields.Integer(string="Commit (Num)", tracking=True)
    target_num = fields.Integer(string="Target (Num)", tracking=True)
    closing_comment = fields.Text(string="Closing Comment", tracking=True)

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)
