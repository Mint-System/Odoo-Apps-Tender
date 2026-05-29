# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioPartnerLevel(models.Model):
    _name = "portfolio.partner_level"
    _description = "Partner Level"
    _order = "sequence, id"

    name = fields.Char(string="Partner Level", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Char(string="Partner Level Description")
    line_ids = fields.One2many("portfolio.partner_level_line", "partner_level_id", string="Lines")
