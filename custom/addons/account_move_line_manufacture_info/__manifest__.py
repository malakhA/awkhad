# © 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Account Move Line Manufacture Information",
    "version": "12.0.1.0.0",
    "depends": [
        "stock_account",
        "mrp"
    ],
    "author": "Eficent,"
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/manufacture",
    "category": "Manufacture Management",
    "installable": True,
    "license": "AGPL-3",
    "data": [
        'security/ir.model.access.csv',
        'views/account_move_line_view.xml',
        'views/mrp_production_views.xml',
        'views/mrp_unbuild_views.xml',
    ]
}
