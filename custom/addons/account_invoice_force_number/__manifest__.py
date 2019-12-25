# Copyright 2011-2016 Agile Business Group
# Copyright 2017 Alex Comba - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Force Invoice Number',
    'version': '12.0.1.0.0',
    'category': 'Accounting & Finance',
    'summary': 'Allows to force invoice numbering on specific invoices',
    'author': 'Agile Business Group, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-invoicing',
    'license': 'AGPL-3',
    'depends': [
        'account'
    ],
    'data': [
        'security/security.xml',
        'views/account_invoice_view.xml'
    ],
    'installable': True,
}
