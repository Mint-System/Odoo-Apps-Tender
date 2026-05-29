# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceTargetGroup(models.Model):
    _name = "reference.target_group"
    _description = "Target Group"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, tracking=True, translate=True)
    active = fields.Boolean(default=True, tracking=True)
    notes = fields.Html(string="Notes")
    image = fields.Binary(string="Image")
    sequence = fields.Integer(string="Sequence")
    category = fields.Many2one("reference.target_group", string="Category")
    color = fields.Integer(string="Color")
