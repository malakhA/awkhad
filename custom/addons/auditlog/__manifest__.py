# Copyright 2015 ABF OSIELL <https://osiell.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': "Audit Log",
    'version': "12.0.1.0.0",
    'author': "ABF OSIELL,Awkhad Community Association (ACA)",
    'license': "AGPL-3",
    'website': "https://github.com/ACA/server-tools/",
    'category': "Tools",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/auditlog_view.xml',
        'views/http_session_view.xml',
        'views/http_request_view.xml',
    ],
    'application': True,
    'installable': True,
}
