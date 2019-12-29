{
    'name' : 'Openbiblica',
    'version' : '1.0',
    'summary': 'OpenBiblica Models',
    'sequence': 1,
    'description': """
    OpenBiblica is a web based bible translation platform.
    This module contents the basic models and backend views.
    Come and visit us at http://www.openbiblica.com
    """,
    'author': "Kusuma Ruslan",
    'website': "http://www.openbiblica.com",
    'category': 'Website',
    'depends' : ['website_forum', 'website_slides'],
    'data': [
        'security/ir.model.access.csv',
        'views/biblica.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

