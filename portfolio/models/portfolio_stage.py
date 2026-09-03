# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioStage(models.Model):
    _name = "portfolio.stage"
    _description = "Portfolio Stage"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    description = fields.Html()
    active = fields.Boolean(default=True)
