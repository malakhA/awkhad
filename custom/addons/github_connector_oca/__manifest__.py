# Copyright 2018 Road-Support - Roel Adriaans
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Github Connector - ACA extension',
    'summary': 'Add ACA specific information to Awkhad modules',
    'version': '12.0.1.0.0',
    'category': 'Connector',
    'license': 'AGPL-3',
    'author': "Awkhad Community Association (ACA), "
              "Road-Support",
    'website': 'https://github.com/ACA/interface-github',
    'depends': [
        'github_connector_awkhad',
    ],
    'data': [
        'views/awkhad_module_version.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
