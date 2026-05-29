# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioEntryState(models.Model):
    _name = "portfolio.entry_state"
    _description = "Portfolio Entry State"
    _order = "sequence, id"

    name = fields.Char(string="State", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    state_color = fields.Integer(string="State Color")
    color = fields.Integer(string="State Color")
