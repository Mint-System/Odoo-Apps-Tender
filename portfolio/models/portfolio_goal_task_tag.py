# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTaskTag(models.Model):
    _name = "portfolio.goal.task.tag"
    _description = "Goal and Task Tag"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")
    active = fields.Boolean(default=True)
