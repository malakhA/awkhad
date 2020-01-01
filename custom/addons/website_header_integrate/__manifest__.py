# -*- coding: utf-8 -*-

{
    'name' : 'Website Integration',
    'version': '12.0.0.1.0',
    'summary': 'Integrate tools/third party apps to website',
    'category': 'Website',
    'description': """Integrate any tools or third party 
    apps which needs to insert Js code to website page header
    For ex. To integrate Tawk.to to website page you only need to
    paste code in website header given by Tawk.to to user""",
    'author': 'Nikunj Dhameliya',
    'website': '',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/company.xml',
        'views/website_templates.xml',
    ],
    'images': ['static/description/banner.png'],
    'qweb': []
}


