# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Secondary Unit',
    'summary': 'Get product quantities in a secondary unit',
    'version': '12.0.1.0.2',
    'development_status': 'Beta',
    'category': 'stock',
    'website': 'https://github.com/ACA/stock-logistics-warehouse',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'stock',
        'product_secondary_unit',
    ],
    'data': [
        'views/product_views.xml',
        'views/stock_move_views.xml',
        'views/stock_picking_views.xml',
        'report/report_deliveryslip.xml',
    ],
}
