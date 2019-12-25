# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    'name': 'Account Document Reversal',
    'summary': 'Create reversed journal entries when cancel document',
    'version': '12.0.1.0.0',
    'author': 'Ecosoft,'
              'Eficent,'
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-financial-tools',
    'category': 'Accounting & Finance',
    'depends': ['account_cancel'],
    'data': [
        'wizard/reverse_account_document_wizard.xml',
        'views/account_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'development_status': 'beta',
    'maintainers': ['kittiu'],
}
