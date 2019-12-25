# Copyright 2014 ACSONE SA/NV (http://acsone.eu)
# @author Stéphane Bidoul <stephane.bidoul@acsone.eu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Test suite for base_import_async',
    'version': '12.0.1.0.0',
    'author': 'ACSONE SA/NV, Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'website': 'https://github.com/ACA/queue',
    'category': 'Generic Modules',
    'summary': """Test suite for base_import_async.

    Normally you don't need to install this.
    """,
    'depends': [
        'base_import_async',
        'account',
    ],
    'data': [
        'tests/data.xml',
    ],
    'installable': True,
    'development_status': 'Stable',
}
