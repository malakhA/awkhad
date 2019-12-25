# Copyright 2018 Tecnativa - Vicent Cubells <vicent.cubells@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3

{
    'name': 'Purchase Order Line Deep Sort',
    'version': '12.0.1.0.0',
    "author": "Tecnativa,"
              "Awkhad Community Association (ACA)",
    'license': 'AGPL-3',
    'category': 'Purchase Management',
    'website': 'https://github.com/ACA/purchase-workflow',
    'summary': 'Purchase Order Line Sort',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
}
