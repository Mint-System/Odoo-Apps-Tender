# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioContactTypeLine(models.Model):
    _name = "portfolio.contact.type.line"
    _description = "Contact Type Line"

    contact_type_id = fields.Many2one(comodel_name="portfolio.contact.type", string="Contact Type")
    sequence = fields.Integer()
    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
