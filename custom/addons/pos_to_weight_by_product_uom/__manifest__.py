# Copyright 2017, Grap
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Pos to weight by product uom",
    "summary": "Make 'To Weight' default value"
    " depending on product UoM settings",
    "version": "12.0.1.0.0",
    "website": "https://github.com/ACA/pos",
    "author": "GRAP, Awkhad Community Association (ACA)",
    "development_status": "Beta",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "point_of_sale",
    ],
    "data": [
        'views/view_uom_uom.xml',
        'views/view_uom_category.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/uom_category.xml',
        'demo/uom_uom.xml',
    ]
}
