# Copyright (C) 2019 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Sale Backorder Report',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'summary': 'Report of Un-Invoice Goods Delivered and Backorders',
    'category': 'Sale',
    'website': 'https://github.com/ACA/sale-reporting',
    'depends': [
        'sale_management',
        'sale_stock'
    ],
    'data': [
        'views/so_backorder_view.xml',
        'views/sale_view.xml',
        'report/so_backorder_report.xml',
        'wizard/so_backorder_wizard_view.xml',
    ],
    'installable': True,
    'development_status': 'Beta',
    'maintainers': ['smangukiya'],
}
