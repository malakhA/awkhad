# Copyright (C) 2018 Pavlov Media
# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Maintenance Agreements',
    'summary': 'Manage maintenance agreements and contracts',
    'author': 'Pavlov Media, '
              'Open Source Integrators, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/contract',
    'category': 'Maintenance',
    'license': 'AGPL-3',
    'version': '12.0.1.1.0',
    'depends': [
        'maintenance',
        'agreement_serviceprofile',
    ],
    'data': [
        'views/agreement_view.xml',
        'views/agreement_serviceprofile_view.xml',
        'views/maintenance_request_view.xml',
        'views/maintenance_equipment_view.xml',
    ],
    'development_status': 'Beta',
    'maintainers': ['max3903'],
}
