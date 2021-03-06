# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Stock Account',
    'version': '12.0.1.0.1',
    'category': 'Field Service',
    'summary': 'Invoice inventory items delivered with Field Service orders',
    'author': 'Open Source Integrators, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice_account',
        'fieldservice_stock',
        'account_invoice_report_hide_line',
    ],
    'data': [],
    'installable': True,
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'bodedra',
        'max3903',
    ],
}
