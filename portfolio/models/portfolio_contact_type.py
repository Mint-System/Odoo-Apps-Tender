# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioContactType(models.Model):
    _name = "portfolio.contact.type"
    _description = "Contact Type"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    line_ids = fields.One2many(comodel_name="portfolio.contact.type.line", inverse_name="contact_type_id")
    description = fields.Char(string="Description")
