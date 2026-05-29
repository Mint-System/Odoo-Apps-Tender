# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioGoalTaskTag(models.Model):
    _name = "portfolio.goal_task_tag"
    _description = "Goal & Key Task Tag"

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
