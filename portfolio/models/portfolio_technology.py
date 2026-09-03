# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioTechnology(models.Model):
    _name = "portfolio.technology"
    _description = "Technology"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, translate=True)
    active = fields.Boolean(default=True)
    user_id = fields.Many2one(comodel_name="res.users", domain="[('share', '=', False)]", string="Responsible")
    category_id = fields.Many2one(comodel_name="portfolio.technology", string="Category")
    color = fields.Integer(string="Color")
