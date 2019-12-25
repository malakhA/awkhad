# Copyright 2018 Tecnativa - Carlos Dauden
# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Move Quick Lot',
    'summary': 'Set lot name and end date directly on picking operations',
    'version': '12.0.1.0.0',
    'category': 'Stock',
    'website': 'https://github.com/ACA/stock-logistics-workflow',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'product_expiry',
    ],
    'data': [
        'views/stock_view.xml',
    ],
}
