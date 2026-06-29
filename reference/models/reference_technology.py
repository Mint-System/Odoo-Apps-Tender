# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceTechnology(models.Model):
    _name = "reference.technology"
    _description = "Reference Technology"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one("reference.technology", string="Category")
    color = fields.Integer()
    sort_order = fields.Integer()
    user_id = fields.Many2one("res.users", string="Responsible")
