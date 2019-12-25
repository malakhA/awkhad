# Copyright 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR Employee Document',
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'website': 'https://github.com/ACA/hr',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'Documents attached to the employee profile',
    'depends': [
        'hr',
        'document',
    ],
    'data': [
        'views/hr_employee.xml',
    ],
}
