# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioBcgMatrix(models.Model):
    _name = "portfolio.bcg_matrix"
    _description = "BCG Matrix"
    _order = "sequence, id"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Html(string="Description")
    image = fields.Binary(string="Image")
