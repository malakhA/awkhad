# Copyright 2019 Alexandre Díaz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Project Custom Info",
    'summary': "Add custom info in projects",
    'author': "Tecnativa, "
              "Awkhad Community Association (ACA)",
    'website': "https://github.com/ACA/project",
    'category': 'Project',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base_custom_info',
        'project',
    ],
    'data': [
        'views/project_project_view.xml',
    ],
    'application': False,
    'development_status': 'Beta',
    'maintainers': ['Tardo'],
}
