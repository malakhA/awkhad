# Copyright 2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Enqueue sales order invoicing',
    'version': '12.0.1.0.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-invoicing',
    'depends': [
        'sale',
        'queue_job',
    ],
    'data': [
        'views/queue_job_views.xml',
        'views/sale_order_views.xml',
        'wizards/sale_advance_payment_inv_views.xml',
    ],
    'installable': True,
}
