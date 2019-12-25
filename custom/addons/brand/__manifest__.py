# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Brand',
    'summary': """
        This is a base addon for brand modules. It adds the brand object and
        its menu and define an abstract model to be inherited from branded
        objects""",
    'version': '12.0.1.1.0',
    'license': 'AGPL-3',
    'author': 'Awkhad Community Association (ACA),'
              'ACSONE SA/NV',
    'website': 'https://github.com/ACA/brand',
    'depends': ['base_setup'],
    'data': [
        'views/res_config_settings.xml',
        'security/res_brand.xml',
        'views/res_brand.xml',
    ],
}
