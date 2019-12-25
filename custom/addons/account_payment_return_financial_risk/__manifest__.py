# Copyright 2016-2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Partner Payment Return Risk',
    'version': '12.0.1.0.0',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'category': 'Sales Management',
    'website': 'https://github.com/ACA/credit-control',
    'license': 'AGPL-3',
    'depends': [
        'account_financial_risk',
        'account_payment_return',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
