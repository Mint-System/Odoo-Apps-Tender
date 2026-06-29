# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceTargetGroup(models.Model):
    _name = "reference.target.group"
    _description = "Reference Target Group"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    color = fields.Integer()
    category_id = fields.Many2one("reference.target.group", string="Category")
    display_color = fields.Integer(widget="color_picker")
    image = fields.Image()
    notes = fields.Html()
