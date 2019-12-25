# Copyright 2016-2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Sale Financial Risk',
    'summary': 'Manage partner risk in sales orders',
    'version': '12.0.1.0.1',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/credit-control',
    'depends': ['sale', 'account_financial_risk'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
