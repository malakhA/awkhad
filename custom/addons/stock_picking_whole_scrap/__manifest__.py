# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Picking Whole Scrap',
    'summary': 'Create whole scrap from a picking for move lines',
    'version': '12.0.1.0.0',
    'development_status': 'Production/Stable',
    'category': 'Warehouse',
    'website': 'https://github.com/ACA/stock-logistics-workflow',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'stock',
    ],
    'data': [
        'wizards/stock_picking_whole_scrap.xml',
        'views/stock_picking_views.xml',
    ],
    'maintainers': ['sergio-teruel'],
}
