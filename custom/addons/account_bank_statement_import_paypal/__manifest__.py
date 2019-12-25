# Copyright 2014-2017 Akretion (http://www.akretion.com).
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Import Paypal Bank Statements",
    'summary': 'Import Paypal CSV files as Bank Statements in Awkhad',
    "version": "12.0.1.0.1",
    "category": "Accounting",
    "website": "https://github.com/ACA/bank-statement-import",
    "author": " Akretion, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account_bank_statement_import",
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/paypal_map_data.xml",
        "wizards/create_map_lines_from_file_views.xml",
        "wizards/account_bank_statement_import_view.xml",
        "views/account_journal_views.xml",
        "views/paypal_map_views.xml",
    ]
}
