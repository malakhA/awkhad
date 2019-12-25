# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Stock Secondary Unit',
    'summary': 'Get product quantities in a secondary unit',
    'version': '12.0.1.0.0',
    'development_status': 'Beta',
    'category': 'stock',
    'website': 'https://github.com/ACA/sale-workflow',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale_order_secondary_unit',
        'stock_secondary_unit',
    ],
    'auto_install': True,
}
