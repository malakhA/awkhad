# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Agreement - MRP',
    'summary': 'Link manufacturing orders to an agreement',
    'version': '12.0.1.0.0',
    'category': 'Contract',
    'author': 'Open Source Integrators, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/contract',
    'depends': [
        'agreement_serviceprofile',
        'mrp',
    ],
    'data': [
        'views/agreement_view.xml',
        'views/mrp_view.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
    'development_status': 'Beta',
    'maintainers': [
        'smangukiya',
        'max3903',
    ],
}
