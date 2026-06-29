# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceReference(models.Model):
    _name = "reference.reference"
    _description = "Reference Reference"

    name = fields.Char()
    value = fields.Integer()
