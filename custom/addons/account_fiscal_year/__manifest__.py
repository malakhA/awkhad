# Copyright 2016 Camptocamp SA
# Copyright 2018 Lorenzo Battistini <https://github.com/eLBati>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Account Fiscal Year",
    "summary": "Create a menu for Account Fiscal Year",
    "version": "12.0.1.0.0",
    "development_status": "Beta",
    "category": "Accounting",
    "website": "https://github.com/ACA/account-financial-tools",
    "author": "Agile Business Group, Camptocamp SA, "
              "Awkhad Community Association (ACA)",
    "maintainers": ["eLBati"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "date_range",
    ],
    "data": [
        "data/date_range_type.xml",
        "views/account_views.xml"
    ],
}
