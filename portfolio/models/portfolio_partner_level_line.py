# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioPartnerLevelLine(models.Model):
    _name = "portfolio.partner_level_line"
    _description = "Partner Level Line"
    _order = "sequence, id"

    partner_level_id = fields.Many2one(
        "portfolio.partner_level", string="Partner Level", required=True
    )
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Description", required=True, translate=True)
