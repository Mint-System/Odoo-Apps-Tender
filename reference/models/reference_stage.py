# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceStage(models.Model):
    _name = "reference.stage"
    _description = "Reference Stage"
    _order = "sequence, id"

    name = fields.Char(required=True)
    sequence = fields.Integer()
