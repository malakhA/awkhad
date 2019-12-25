# Part of Awkhad. See LICENSE file for full copyright and licensing details.

{
    'name': 'Budgets Management',
    'version': '12.0.1.0.1',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'author': 'Awkhad S.A., '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-budgeting',
    'depends': ['account'],
    'excludes': ['account_budget'],
    'data': [
        'security/ir.model.access.csv',
        'security/account_budget_security.xml',
        'views/account_analytic_account_views.xml',
        'views/account_budget_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': ['data/account_budget_demo.xml'],
}
