# Copyright 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Partner phonecalls schedule",
    "summary": "Track the time and days your partners expect phone calls",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://github.com/ACA/partner-contact",
    "author": "Tecnativa, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "resource",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
    ],
}