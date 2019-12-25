# Copyright 2019 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Website Sale Product Minimal Price',
    'summary': 'Display minimal price for products that has variants',
    'version': '12.0.1.0.0',
    'development_status': 'Production/Stable',
    'maintainers': ['sergio-teruel'],
    'category': 'Website',
    'website': 'https://github.com/ACA/e-commerce',
    'author': 'Tecnativa, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/assets.xml',
        'views/templates.xml',
    ],
}
