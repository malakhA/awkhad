# Copyright 2013 Michael Telahun Makonnen <mmakonnen@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'HR Job Employee Categories',
    'version': '12.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': 'Adds tags to employee trough contract and job position',
    'author': "Michael Telahun Makonnen <mmakonnen@gmail.com>, "
              "Savoir-faire Linux, "
              "Fekete Mihai (FBSR), "
              "Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/hr',
    'license': 'AGPL-3',
    'depends': [
        'hr_contract',
    ],
    'data': [
        'views/hr_view.xml',
    ],
    'installable': True,
}
