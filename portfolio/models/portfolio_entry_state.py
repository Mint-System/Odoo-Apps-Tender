# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryState(models.Model):
    _name = "portfolio.entry.state"
    _description = "Portfolio Entry State"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    color = fields.Integer(string="State Color")
