# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class ReferenceTechnology(models.Model):
    _name = "reference.technology"
    _description = "Technology, Tool & Method"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, tracking=True, translate=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(
        "res.users", string="Responsible",
        domain="[('share', '=', False)]", tracking=True
    )
    category = fields.Many2one("reference.technology", string="Category")
    color = fields.Integer(string="Color")
