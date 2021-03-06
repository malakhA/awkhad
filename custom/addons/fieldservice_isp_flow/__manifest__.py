# Copyright (C) 2019 - Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service - Flow for ISP',
    'summary': 'Field Service workflow for Internet Service Providers',
    'version': '12.0.1.1.0',
    'category': 'Field Service',
    'author':
        'Open Source Integrators, '
        'Akretion, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
    ],
    'data': [
        'data/fsm_stage.xml',
        'views/fsm_order.xml',
    ],
    'application': False,
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': ['osi-scampbell'],
}
