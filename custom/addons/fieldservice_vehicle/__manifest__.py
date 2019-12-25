# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service Vehicles',
    'summary': 'Manage Field Service vehicles and assign drivers',
    'version': '12.0.2.0.0',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/fsm_vehicle.xml',
        'views/menu.xml',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'wolfhall',
        'max3903',
    ],
    'installable': True,
}
