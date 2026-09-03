# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioPartnerLevelLine(models.Model):
    _name = "portfolio.partner.level.line"
    _description = "Partner Level Line"

    partner_level_id = fields.Many2one(comodel_name="portfolio.partner.level", string="Partner Level")
    sequence = fields.Integer()
    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
