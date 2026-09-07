# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ReferenceReference(models.Model):
    _name = "reference.reference"
    _description = "Reference"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"

    @api.model
    def _default_stage_id(self):
        return self.env.ref("reference.reference_stage_new", raise_if_not_found=False)

    # Basic fields
    name = fields.Char(required=True, help="Reference title, will be used on Website (> 30 chars)")
    active = fields.Boolean(default=True)
    color = fields.Integer()
    sequence = fields.Integer()

    # Stage & Kanban state
    stage_id = fields.Many2one(
        "reference.stage",
        string="Stage",
        default=lambda self: self._default_stage_id(),
    )
    kanban_state = fields.Selection(
        [
            ("normal", "In Progress"),
            ("done", "Ready"),
            ("blocked", "Blocked"),
        ]
    )

    # Ownership / responsible
    user_id = fields.Many2one(
        "res.users",
        string="Puzzle Owner",
        help="Puzzle member who leads the reference (PM, AM, BL etc.)",
    )
    puzzle_owner_id = fields.Many2one("res.users", string="Puzzle Owner")
    member_ids = fields.Many2many(
        "res.users",
        string="Members Involved",
        help="Puzzle members which were involved in project",
    )

    # Images
    image = fields.Image()
    portrait_image = fields.Image()

    # Content
    short_reference = fields.Html()
    sales_reference = fields.Html(
        help=(
            "Keywords or prose divided into important topics. "
            "No longer than 1500 characters, short sentences. "
            "Basis for success stories or usable in offers."
        ),
    )
    key_aspects = fields.Html(
        help="3-4 figures that confirm the scope/benefits/success of the solution. Used for success story on website.",
    )
    success_story = fields.Html(
        help="Project description; used on the website (< 1000 characters incl. Spaces)",
    )
    testimonial = fields.Html(help="Customer statement on cooperation")
    testimonial_author = fields.Char(help="First and last name, job title")

    # Customer details
    customer_id = fields.Many2one(
        "res.partner",
        string="Customer",
        domain=[("is_company", "=", True)],
    )
    contact_id = fields.Many2one(
        "res.partner",
        string="Sales Reference Contact",
        domain=[("is_company", "=", False)],
    )
    customer_owner_id = fields.Many2one(
        "res.partner",
        string="Customer Owner",
        domain=[("is_company", "=", False)],
        help="Contact person approving the reference/success story",
    )

    # Publishing / Website
    website_url = fields.Char(help="Published website URL")
    website_tag_ids = fields.Many2many(
        "reference.website.tag",
        string="Website Tags",
        help="Categories of the website where reference/success story can be used.",
    )

    # Project / volume
    project_start = fields.Date()
    project_end = fields.Date()
    project_volume = fields.Monetary(
        currency_field="currency_id",
        help="Project/order volume (incl. follow-up orders)",
    )
    project_volume_days = fields.Integer(
        help="Total of days PITC worked on this reference?",
    )
    currency_id = fields.Many2one("res.currency")

    # Usage / approval
    usage_type = fields.Selection(
        [
            ("internalOnly", "Internal use only"),
            ("generalUse", "Unrestricted usage"),
            ("restrictedUse", "Restricted usage"),
        ],
        string="Allowed usage",
        help="If restricted usage, allowed channels have to be selected",
    )
    channel_ids = fields.Many2many(
        "reference.channel",
        string="Allowed channels",
        help="If restricted usage, allowed channels have to be selected",
    )

    # Categorisation
    industry_ids = fields.Many2many(
        "res.partner.industry",
        string="Industries",
        help="Based on NOGA industries",
    )
    service_type_ids = fields.Many2many(
        "reference.service.type",
        string="Service Types",
        help="Service Types used for this project / reference?",
    )
    technology_ids = fields.Many2many(
        "reference.technology",
        string="Technologies, Tools & Methodologies",
        help="Select all relevant tags. Additional can be added if relevant/important enough for the future",
    )
    tag_ids = fields.Many2many(
        "reference.tag",
        string="Tags",
        help="Tags to work/filter on references",
    )

    # CRM linkage
    opportunity_source_ids = fields.Many2many(
        "crm.lead",
        relation="reference_reference_crm_lead_source_rel",
        column1="reference_id",
        column2="lead_id",
        string="Source Opportunities",
        domain=[("active", "in", [True, False])],
        help="Opportunities this reference bases on over whole duration.",
    )
    opportunity_usage_ids = fields.Many2many(
        "crm.lead",
        relation="reference_reference_crm_lead_usage_rel",
        column1="reference_id",
        column2="lead_id",
        string="Used in Opportunities",
        domain=[("active", "in", [True, False])],
        help="In what opportunities is this reference already used?",
    )

    # Priority
    priority = fields.Boolean()
