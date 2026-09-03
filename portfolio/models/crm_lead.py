# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = "crm.lead"

    portfolio_solution_ids = fields.Many2many(
        comodel_name="portfolio.portfolio", string="Solutions & Products", tracking=True
    )
    division_ids = fields.Many2many(comodel_name="res.partner", string="Bases / Divisions", tracking=True)
    referral_partner_id = fields.Many2one(comodel_name="res.partner", string="Referral By")
