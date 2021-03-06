# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Storage Media Product",
    "summary": "Link media to products and categories",
    "version": "10.0.2.0.0",
    "category": "Storage",
    "website": "https://www.github.com/ACA/storage",
    "author": " Akretion, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "installable": False,
    "depends": ["storage_media", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/product.xml",
        "views/product_category.xml",
    ],
}
