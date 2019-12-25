# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Website Sale Product Attribute Filter Visibility',
    'summary': 'Allow hide any attributes in shop attributes filter',
    'version': '12.0.1.0.0',
    'development_status': 'Beta',
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
        'views/product_attribute_views.xml',
    ],
}
