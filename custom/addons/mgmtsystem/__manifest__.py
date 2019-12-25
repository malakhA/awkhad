# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System",
    "version": "12.0.1.0.0",
    "author": "Savoir-faire Linux,Awkhad Community Association (ACA)",
    "website": "https://github.com/ACA/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'base',
    ],
    "data": [
        'security/mgmtsystem_security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/mgmtsystem_system.xml',
        'views/res_config.xml'
    ],
    "installable": True,
    "application": True,
}
