# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PortfolioPortfolio(models.Model):
    _name = "portfolio.portfolio"
    _description = "Portfolio Portfolio"

    name = fields.Char()
    value = fields.Integer()
