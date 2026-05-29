# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ReferenceWebsiteTag(models.Model):
    _name = "reference.website_tag"
    _description = "Website Tag"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, tracking=True, translate=True)
    active = fields.Boolean(default=True, tracking=True)
    category = fields.Many2one("reference.website_tag", string="Category")
    color = fields.Integer(string="Color")
