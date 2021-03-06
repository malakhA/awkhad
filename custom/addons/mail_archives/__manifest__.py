{
    "name": "Mail archives",
    "summary": """Adds menu to find old messages""",
    "category": "Discuss",
    "images": ['images/1.jpg'],
    "version": "12.0.1.0.1",

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    'price': 40.00,
    'currency': 'EUR',

    "depends": [
        "mail",
    ],

    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    'installable': True,
}
