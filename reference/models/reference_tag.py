# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceTag(models.Model):
    _name = "reference.tag"
    _description = "Reference Tag"
    _order = "name"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
