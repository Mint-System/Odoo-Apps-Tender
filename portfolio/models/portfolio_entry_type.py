# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryType(models.Model):
    _name = "portfolio.entry_type"
    _description = "Portfolio Entry Type"
    _order = "sequence, id"

    name = fields.Char(string="Portfolio Entry Type", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    hex_color = fields.Char(string="Hex Color")
    line_ids = fields.One2many("portfolio.entry_type_line", "entry_type_id", string="Lines")
