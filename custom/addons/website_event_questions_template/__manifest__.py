# Copyright 2017 Tecnativa - Sergio Teruel
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Website Event Questions Template',
    'summary': 'Set question templates for events',
    'version': '12.0.1.0.0',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    "license": "LGPL-3",
    'website': 'https://github.com/ACA/event',
    'category': 'Marketing',
    'depends': ['website_event_questions'],
    'data': [
        'security/ir.model.access.csv',
        'views/event_view.xml',
        'views/website_event_questions_template_view.xml',
    ],
    'installable': True,
}
