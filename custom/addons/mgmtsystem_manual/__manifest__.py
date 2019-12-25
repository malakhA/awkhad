# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Manual",
    "version": "12.0.1.0.0",
    "author": "Savoir-faire Linux,Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'document_page',
        'mgmtsystem',
    ],
    "data": [
        'data/mgmtsystem_manual.xml',
        'views/mgmtsystem_manual.xml',
        'views/document_page.xml',
    ],
    'installable': True,
}
