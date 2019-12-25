# Copyright 2018 Forest and Biomass Romania
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Group Menu',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': "Adds menu entries for Account Group and Tax Group",
    'author': "Forest and Biomass Romania, Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/account-financial-tools',
    'depends': ['account'],
    'data': ['views/account_group.xml',
             'views/account_tax_group.xml'],
    'demo': ['demo/account_group.xml',
             'demo/account_tax_group.xml'],
    'installable': True,
}
