# Copyright (C) 2019 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Brand",
    "summary": "Send branded invoices and refunds",
    "version": "12.0.2.1.0",
    "category": "Accounting Management",
    "website": "https://github.com/ACA/account-invoicing",
    "author": "Open Source Integrators, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "depends": [
        'account',
        'brand',
    ],
    "data": [
        "views/account_invoice.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["osi-scampbell"],
}
