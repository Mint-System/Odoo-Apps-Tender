# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioTag(models.Model):
    _name = "portfolio.tag"
    _description = "Portfolio Tag"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string="Color")
