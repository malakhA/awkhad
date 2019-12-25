# Copyright 2019 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Website Event Require Login',
    'version': '12.0.1.0.0',
    'author': 'Tecnativa, '
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/event',
    'category': 'Event',
    'depends': [
        'website_event',
    ],
    'data': [
        'views/event_views.xml',
        'views/website_event_templates.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
