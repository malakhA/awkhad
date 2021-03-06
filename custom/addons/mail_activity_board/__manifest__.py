# Copyright 2018 David Juaneda - <djuaneda@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Activities board',
    'summary': 'Add Activity Boards',
    'version': '12.0.1.0.0',
    'development_status': 'Beta',
    'category': 'Social Network',
    'website': 'https://github.com/ACA/social',
    'author': 'SDi, David Juaneda, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'calendar',
        'board',
    ],
    'data': [
        'views/templates.xml',
        'views/mail_activity_view.xml',
    ],
    'qweb': [
        'static/src/xml/inherit_chatter.xml',
    ]
}
