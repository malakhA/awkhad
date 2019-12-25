# Copyright 2018 Eska Yazılım ve Danışmanlık A.Ş (www.eskayazilim.com.tr)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Remove Awkhad Enterprise',
    'summary': 'Remove enterprise modules and setting items',
    'version': '12.0.1.1.0',
    'category': 'Maintenance',
    'author': 'Eska, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/server-brand/',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'data/ir_module_module.xml',
    ],
    'installable': True,
    'auto_install': False,
}
