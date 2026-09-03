# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioBcgMatrix(models.Model):
    _name = "portfolio.bcg.matrix"
    _description = "BCG Matrix"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    description = fields.Html(string="Description")
    image = fields.Binary(string="Image")
