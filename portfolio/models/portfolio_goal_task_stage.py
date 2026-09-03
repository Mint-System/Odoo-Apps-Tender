# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTaskStage(models.Model):
    _name = "portfolio.goal.task.stage"
    _description = "Goal and Task Stage"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    description = fields.Html(string="Description")
    active = fields.Boolean(default=True)
