# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ReferenceReference(models.Model):
    _name = "reference.reference"
    _description = "Reference"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Title", required=True, translate=True, tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    user_id = fields.Many2one(
        "res.users",
        string="Puzzle Owner",
        domain="[('share', '=', False)]",
        tracking=True,
    )
    image = fields.Binary(string="Image")
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "reference.stage",
        string="Stage",
        required=True,
        tracking=True,
        group_expand="_group_expand_stages",
        ondelete="restrict",
    )
    priority = fields.Boolean(string="High Priority")
    color = fields.Integer(string="Color")
    kanban_state = fields.Selection(
        [
            ("normal", "In Progress"),
            ("done", "Ready"),
            ("blocked", "Blocked"),
        ],
        string="Kanban State",
        default="normal",
    )
    customer = fields.Many2one(
        "res.partner",
        string="Customer",
        domain="[('is_company', '=', True)]",
    )
    short_reference = fields.Html(
        string="Short reference",
        help="Teaser & short reference text with 2 - 3 core statements and formulated as VP (< 200 chars incl. spaces)",
    )
    industries = fields.Many2many("res.partner.industry", string="Industries")
    project_start = fields.Date(string="Duration from", tracking=True)
    project_end = fields.Date(string="Duration to", tracking=True)
    success_story = fields.Html(string="Success Story")
    currency_id = fields.Many2one("res.currency", string="Currency")
    project_volume = fields.Monetary(
        string="Project Volume",
        tracking=True,
        help="Project/order volume (incl. follow-up orders)",
    )
    key_aspects = fields.Html(
        string="Key Aspects",
        help="3-4 figures that confirm the scope/benefits/success of the solution.",
    )
    website_tags = fields.Many2many(
        "reference.website_tag",
        string="Website Tags",
        help="Categories of the website where reference/success story can be used.",
    )
    technologies = fields.Many2many(
        "reference.technology",
        string="Technologies, Tools & Methodologies",
    )
    sales_reference = fields.Html(
        string="Sales Reference",
        help="Keywords or prose divided into important topics. No longer than 1500 characters, short sentences.",
    )
    used_for_opportunities = fields.Many2many(
        "crm.lead",
        string="Used for",
        relation="reference_reference_crm_lead_used_for_rel",
        help="In what opportunities is this reference already used?",
        tracking=True,
    )
    testimonial = fields.Html(
        string="Testimonial",
        help="Customer statement on cooperation",
    )
    testimonial_by = fields.Char(
        string="Testimonial by",
        help="First and last name, job title",
    )
    customer_contact = fields.Many2one(
        "res.partner",
        string="Sales Reference Contact",
        help="Contact giving/approving the testimonial",
        domain="[('is_company', '=', False)]",
        tracking=True,
    )
    portrait_image = fields.Binary(string="Portrait Image")
    service_types = fields.Many2many(
        "reference.service_type",
        string="Service Types",
        help="Service Types used for this project / reference?",
    )
    bases_on = fields.Many2many(
        "crm.lead",
        string="Bases on",
        relation="reference_reference_crm_lead_bases_on_rel",
        help="Opportunities this reference bases on over whole duration.",
        tracking=True,
    )
    project_volume_days = fields.Integer(
        string="Project Volume (Days)",
        help="Total of days PITC worked on this reference?",
        tracking=True,
    )
    # TODO: Uncomment when portfolio module is available
    # portfolio_solutions = fields.Many2many(
    #     "x_solutions", string="Portfolio Solution(s)"
    # )
    customer_owner = fields.Many2one(
        "res.partner",
        string="Customer Owner",
        help="Contact approving the reference",
        domain="[('is_company', '=', False)]",
        tracking=True,
    )
    how_usable = fields.Selection(
        [
            ("internalOnly", "internal use only"),
            ("generalUse", "unrestricted usage"),
            ("restrictedUse", "restricted usage"),
        ],
        string="Allowed usage",
        help="If restricted usage, allowed channels have to be selected",
        tracking=True,
    )
    channels = fields.Many2many(
        "reference.channel",
        string="Allowed channels",
        help="If restricted usage, allowed channels have to be selected",
        tracking=True,
    )
    puzzle_owner = fields.Many2one(
        "res.users",
        string="Puzzle Owner (alt)",
        help="Nicht mehr genutztes Feld!",
        tracking=True,
    )
    members_involved = fields.Many2many(
        "res.users",
        string="Members involved",
        relation="reference_reference_res_users_members_rel",
        tracking=True,
    )
    published_website_url = fields.Char(string="Published (Website-URL)")
    tags = fields.Many2many("reference.tag", string="Tags")

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)
