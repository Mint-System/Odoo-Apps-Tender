# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryTypeLine(models.Model):
    _name = "portfolio.entry_type_line"
    _description = "Portfolio Entry Type Line"
    _order = "sequence, id"

    entry_type_id = fields.Many2one(
        "portfolio.entry_type", string="Portfolio Entry Type", required=True
    )
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Description", required=True, translate=True)
