# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR Employee Service',
    'version': '12.0.1.0.1',
    'category': 'Human Resources',
    'website': 'https://github.com/ACA/hr',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'Employee service information & duration',
    'depends': [
        'hr',
    ],
    'external_dependencies': {
        'python': [
            'dateutil',
        ],
    },
    'data': [
        'views/hr_employee.xml',
    ],
}
