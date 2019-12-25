# Copyright 2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sales Timesheet: exclude Task from Sale Order',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'website': 'https://github.com/ACA/timesheet',
    'author':
        'Brainbean Apps, '
        'Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'Exclude Task and related Timesheets from Sale Order',
    'depends': [
        'sale_timesheet',
    ],
    'data': [
        'views/project_task.xml',
    ],
}
