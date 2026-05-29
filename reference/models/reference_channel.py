# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceChannel(models.Model):
    _name = "reference.channel"
    _description = "Reference Channel"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
