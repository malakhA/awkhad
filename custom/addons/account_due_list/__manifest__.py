# Part of Awkhad. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payments Due list',
    'version': '12.0.1.0.0',
    'category': 'Generic Modules/Payment',
    'development_status': 'Beta',
    'author': 'Awkhad Community Association (ACA)',
    'summary': 'List of open credits and debits, with due date',
    'website': 'https://github.com/ACA/account-payment',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/payment_view.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
    'auto_install': False,
}
