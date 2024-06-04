{
    "name": "Real Estate Ads",
    "version": "1.0",
    "website": "https://www.first_odoo.com",
    "author": "ardi",
    "description": """
        Real Estate module to show available properties
    """,
    "category": "Sales",
    "depends": ["base"],
    "data": [
        # groups
        "security/ir.model.access.csv",
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',

        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/property_offer_view.xml",
        "views/menu_items.xml",

        # Data Files
        # "data/property_type.xml",
        "data/estate.property.type.csv",
    ],
    "demo": [
        'demo/property_tag.xml'
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
