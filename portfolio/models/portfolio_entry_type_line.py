# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryTypeLine(models.Model):
    _name = "portfolio.entry.type.line"
    _description = "Portfolio Entry Type Line"

    entry_type_id = fields.Many2one(comodel_name="portfolio.entry.type", string="Entry Type")
    sequence = fields.Integer()
    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
