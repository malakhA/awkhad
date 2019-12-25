# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Stock Picking Note',
    'summary': 'Add picking note in sale and purchase order',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'website': 'https://github.com/ACA/sale-workflow',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock',
    ],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
}
