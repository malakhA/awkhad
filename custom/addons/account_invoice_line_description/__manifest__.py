# Copyright 2015 Agile Business Group sagl
# (<http://www.agilebg.com>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Account invoice line description',
    'version': '12.0.1.0.0',
    'category': 'Generic Modules/Accounting',
    'author':   "Agile Business Group, "
                "Tecnativa, "
                "Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/account-invoicing',
    'license': 'AGPL-3',
    "depends": [
        'account',
    ],
    "data": [
        'security/invoice_security.xml',
        'wizards/res_config_view.xml',
    ],
    'installable': True,
}
