# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioAccountLevelLine(models.Model):
    _name = "portfolio.account.level.line"
    _description = "Account Level Line"

    account_level_id = fields.Many2one(comodel_name="portfolio.account.level", string="Account Level")
    sequence = fields.Integer()
    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
