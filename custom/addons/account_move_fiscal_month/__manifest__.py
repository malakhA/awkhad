# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Move Fiscal Month',
    'summary': """Display the fiscal month on journal entries/item""",
    'version': '12.0.1.1.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/account-financial-tools',
    'depends': [
        'account_fiscal_month',
    ],
    'data': [
        'views/account_move.xml',
        'views/account_move_line.xml',
    ],
}
