# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceWebsiteTag(models.Model):
    _name = "reference.website.tag"
    _description = "Reference Website Tag"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer()
    category_id = fields.Many2one("reference.website.tag", string="Category")
    display_color = fields.Integer()
