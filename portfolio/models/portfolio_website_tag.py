# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioWebsiteTag(models.Model):
    _name = "portfolio.website.tag"
    _description = "Website Tag"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    category_id = fields.Many2one(comodel_name="portfolio.website.tag", string="Category")
    color = fields.Integer(string="Color")
