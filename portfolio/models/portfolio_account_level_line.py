# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioAccountLevelLine(models.Model):
    _name = "portfolio.account_level_line"
    _description = "Account Level Line"
    _order = "sequence, id"

    account_level_id = fields.Many2one("portfolio.account_level", string="Account Level", required=True)
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Description", required=True, translate=True)
