# -*- coding: utf-8 -*-
# copyright Awkhad SA
# copyright ACA
# Licence : LGPL-3

{
    'name': 'POS report Session Summary',
    'version': '12.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Adds a Session Summary PDF report on the POS session',
    'author': 'Akretion, Awkhad SA, Awkhad Community Association (ACA)',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [
        'views/session_summary_report.xml',
        'views/report_session_summary.xml',
    ],
    'installable': True,
    'application': False,
    'website': 'https://github.com/ACA/pos',
    'auto_install': False,
}
