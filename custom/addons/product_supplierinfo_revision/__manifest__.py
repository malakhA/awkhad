# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2018 Vicent Cubells <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Supplierinfo Revision",
    "version": "12.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/ACA/product-attribute/",
    "author": "Tecnativa, "
              "Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "views/product_supplierinfo_view.xml",
        "wizards/supplierinfo_duplicate_wizard_view.xml",
    ],
}
