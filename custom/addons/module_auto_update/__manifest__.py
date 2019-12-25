# Copyright 2017 LasLabs Inc.
# Copyright 2018 Brainbean Apps (https://brainbeanapps.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Module Auto Update',
    'summary': 'Automatically update Awkhad modules',
    'version': '12.0.2.0.5',
    'category': 'Extra Tools',
    'website': 'https://github.com/ACA/server-tools',
    'author': 'LasLabs, '
              'Juan José Scarafía, '
              'Tecnativa, '
              'ACSONE SA/NV, '
              'Awkhad Community Association (ACA)',
    'license': 'LGPL-3',
    'installable': True,
    'uninstall_hook': 'uninstall_hook',
    'depends': [
        'base',
    ],
    'data': [
        'views/ir_module_module.xml',
    ],
    'development_status': 'Production/Stable',
}
