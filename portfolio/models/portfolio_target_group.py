# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioTargetGroup(models.Model):
    _name = "portfolio.target.group"
    _description = "Target Group"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    notes = fields.Html(string="Notes")
    image = fields.Binary(string="Image")
    sequence = fields.Integer()
    category_id = fields.Many2one(comodel_name="portfolio.target.group", string="Category")
    color = fields.Integer(string="Color")
