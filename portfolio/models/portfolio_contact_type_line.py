# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioContactTypeLine(models.Model):
    _name = "portfolio.contact_type_line"
    _description = "Contact Type Line"
    _order = "sequence, id"

    contact_type_id = fields.Many2one("portfolio.contact_type", string="Contact Type", required=True)
    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Description", required=True, translate=True)
