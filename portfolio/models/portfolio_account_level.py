# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioAccountLevel(models.Model):
    _name = "portfolio.account.level"
    _description = "Account Level"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    line_ids = fields.One2many(comodel_name="portfolio.account.level.line", inverse_name="account_level_id")
    description = fields.Char(string="Description")
