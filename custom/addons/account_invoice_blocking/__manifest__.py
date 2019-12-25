# Copyright 2016 Acsone SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Blocking',
    'summary': 'Set a blocking (No Follow-up) flag on invoices',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'author': 'Acsone SA/NV,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-invoicing/',
    'depends': [
        'account'
    ],
    'data': [
        'views/account_invoice.xml',
    ],
}
