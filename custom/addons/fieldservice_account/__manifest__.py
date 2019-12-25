# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Accounting',
    'summary': 'Track invoices linked to Field Service orders',
    'version': '12.0.2.0.3',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/fsm_order.xml',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'osimallen',
        'brian10048',
        'bodedra',
    ],
}
