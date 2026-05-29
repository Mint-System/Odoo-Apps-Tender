# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class ReferenceServiceType(models.Model):
    _name = "reference.service_type"
    _description = "Service Type"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
