# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Project: require Project on Task',
    'summary': """
        Set project on task as a mandatory field""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/project',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_task.xml',
        'views/res_config_settings.xml',
    ],
}
