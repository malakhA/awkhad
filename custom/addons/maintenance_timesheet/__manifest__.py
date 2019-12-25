# © 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Maintenance Timesheets",
    "summary": "Adds timesheets to maintenance requests",
    "author": "Awkhad Community Association (ACA), Solvos",
    "license": "AGPL-3",
    "version": "12.0.1.0.1",
    "category": "Human Resources",
    "website": "https://github.com/ACA/maintenance",
    "depends": [
        "maintenance_project",
        "hr_timesheet",
    ],
    "data": [
        "security/maintenance_timesheet_security.xml",
        "views/hr_timesheet_views.xml",
        "views/maintenance_request_views.xml",
    ],
    "demo": [
        "data/demo_maintenance_timesheet.xml",
    ],
    'installable': True,
}
