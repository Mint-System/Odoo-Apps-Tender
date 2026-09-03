# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioReferenceStage(models.Model):
    _name = "portfolio.reference.stage"
    _description = "Reference Stage"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    active = fields.Boolean(default=True)
