# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioSolutionTag(models.Model):
    _name = "portfolio.solution_tag"
    _description = "Solution Tag"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string="Color")
