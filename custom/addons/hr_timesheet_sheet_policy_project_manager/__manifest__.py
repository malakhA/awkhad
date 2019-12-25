# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'HR Timesheet Sheet: Project Manager Policy',
    'version': '12.0.1.1.0',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/timesheet/',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'Allows setting Project Manager as Reviewer',
    'depends': [
        'hr_timesheet_sheet',
    ],
    'data': [
        'views/hr_timesheet_sheet.xml',
    ],
    'installable': True,
}
