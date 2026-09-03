# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryType(models.Model):
    _name = "portfolio.entry.type"
    _description = "Portfolio Entry Type"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    line_ids = fields.One2many(comodel_name="portfolio.entry.type.line", inverse_name="entry_type_id")
    hex_color = fields.Char(string="Hex Color")
