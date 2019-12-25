# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Service Google Map',
    'summary': 'This module displays map views on the order and location using'
    ' Google Map View module.',
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'category': 'Field Service',
    'author': 'Open Source Integrators, Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/field-service',
    'depends': [
        'fieldservice',
        'web_view_google_map',
    ],
    'data': [
        'views/fsm_order.xml',
        'views/fsm_location.xml',
    ],
    'development_status': 'Beta',
    'maintainers': [
        'wolfhall',
        'max3903',
    ],
}
