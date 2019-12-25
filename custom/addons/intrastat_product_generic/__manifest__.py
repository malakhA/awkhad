# Copyright 2009-2018 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Generic Intrastat Product Declaration',
    'version': '12.0.1.0.0',
    'category': 'Accounting & Finance',
    'website': 'https://github.com/ACA/intrastat',
    'author': 'Noviat,'
              'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'intrastat_product',
    ],
    'data': [
        'security/intrastat_security.xml',
        'views/intrastat_product.xml'
    ],
}
