# © 2013-2014 Nicolas Bessi (Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Base Comments Templates",
    "summary": "Comments templates on documents",
    "version": "12.0.2.0.0",
    "category": "Sale",
    "website": "https://github.com/ACA/account-invoice-reporting",
    "author": "Camptocamp, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base"
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/comment_view.xml",
        "views/res_partner.xml",
    ],
}
