# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class PortfolioContactType(models.Model):
    _name = "portfolio.contact_type"
    _description = "Contact Type"
    _order = "sequence, id"

    name = fields.Char(string="Contact Type", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Char(string="Contact Type Description")
    line_ids = fields.One2many(
        "portfolio.contact_type_line", "contact_type_id",
        string="Lines"
    )
