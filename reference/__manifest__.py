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
    "depends": ["mail", "crm"],
    "data": ["security/security.xml", "views/reference_reference_views.xml", "security/ir.model.access.csv"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
    "demo": ["demo/demo.xml"],
}
