{
    'name' : 'Website Openbiblica',
    'version' : '1.0',
    'summary': 'OpenBiblica Website Module',
    'sequence': 2,
    'description': """
    OpenBiblica is a web based bible translation platform
    This module contents the website features of Openbiblica
    - Upload and install usfm files
    - Translate bible
    - Forum Integration
    Come and visit us at http://www.openbiblica.com
    """,
    'author': "Kusuma Ruslan",
    'website': 'https://www.openbiblica.com',
    'category': 'Website',
    'depends' : ['openbiblica'],
    'data': [
        'views/portal_templates.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

