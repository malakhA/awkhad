# Copyright 2013-2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Partner Relations",
    "version": "12.0.1.0.0",
    "author": "Therp BV,Camptocamp,Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/partner-contact",
    "complexity": "normal",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "depends": [
        'contacts',
        'sales_team',
    ],
    "demo": [
        "data/demo.xml",
    ],
    "data": [
        'security/ir.model.access.csv',
        "views/res_partner_relation_all.xml",
        'views/res_partner.xml',
        'views/res_partner_relation_type.xml',
        'views/menu.xml',
    ],
    "auto_install": False,
    "installable": True,
}
