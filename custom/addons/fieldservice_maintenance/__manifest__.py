# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Maintenance',
    'summary': 'Integrate Field Service orders with maintenance requests',
    'version': '12.0.1.0.0',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
        'maintenance',
    ],
    'data': [
        'data/fsm_order_type.xml',
        'views/maintenance_view.xml',
        'views/fsm_equipment_view.xml',
        'views/fsm_order_view.xml',
    ],
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'smangukiya',
        'max3903',
        'bodedra',
    ],
    'installable': True,
}
