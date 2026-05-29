# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioAccountLevel(models.Model):
    _name = "portfolio.account_level"
    _description = "Account Level"
    _order = "sequence, id"

    name = fields.Char(string="Account Level", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Char(string="Account Level Description")
    line_ids = fields.One2many(
        "portfolio.account_level_line", "account_level_id",
        string="Lines"
    )
