# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Reference",
    "summary": """
        Manage references for tender applications.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mail", "crm", "contacts", "sales_team"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/reference_stage_data.xml",
        "views/reference_reference_views.xml",
        "views/reference_stage_views.xml",
        "views/reference_channel_views.xml",
        "views/reference_service_type_views.xml",
        "views/reference_tag_views.xml",
        "views/reference_technology_views.xml",
        "views/reference_website_tag_views.xml",
        "views/reference_target_group_views.xml",
        "views/reference_menus.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
    "demo": ["demo/demo.xml"],
}
