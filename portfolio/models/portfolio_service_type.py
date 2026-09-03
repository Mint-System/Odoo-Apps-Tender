# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioServiceType(models.Model):
    _name = "portfolio.service.type"
    _description = "Service Type"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    description = fields.Char(string="Description")
