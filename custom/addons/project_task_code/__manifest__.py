# Copyright 2016 Tecnativa <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sequential Code for Tasks',
    'version': '12.0.1.0.1',
    'category': 'Project Management',
    'author': 'AwkhadMRP team, '
              'AvanzOSC, '
              'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/project',
    'license': 'AGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        'data/task_sequence.xml',
        'views/project_view.xml',
    ],
    'installable': True,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
}
