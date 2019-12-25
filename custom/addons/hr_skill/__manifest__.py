# Copyright 2013 Savoir-faire Linux
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Skills Management",
    "summary": "Manage your employee skills",
    "version": "12.0.1.2.0",
    "category": "Human Resources",
    "license": "AGPL-3",
    "author": (
        "Savoir-faire Linux, "
        "Brainbean Apps, "
        "Awkhad Community Association (ACA)"
    ),
    "website": "https://github.com/ACA/hr",
    "depends": [
        "hr"
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/hr_skill.xml",
        "views/hr_employee.xml",
        "views/hr_employee_skill.xml",
    ],
    'installable': True,
}
