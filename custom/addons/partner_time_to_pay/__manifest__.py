# Copyright 2017 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Time to Pay',
    'summary': 'Add receivables and payables statistics to partners',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'development_status': "Beta",
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'category': 'Accounting & Finance',
    'website': 'https://github.com/ACA/account-invoice-reporting',
    "maintainers": ['max3903'],
    'depends': [
        'account'
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}
