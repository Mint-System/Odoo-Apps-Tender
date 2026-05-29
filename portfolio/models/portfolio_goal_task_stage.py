# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTaskStage(models.Model):
    _name = "portfolio.goal_task_stage"
    _description = "Goal & Key Task Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage Name", required=True, translate=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Html(string="Description")
