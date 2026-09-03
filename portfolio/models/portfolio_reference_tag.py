# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioReferenceTag(models.Model):
    _name = "portfolio.reference.tag"
    _description = "Reference Tag"

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
