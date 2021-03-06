# Copyright 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Order Product Recommendation",
    "summary": "Recommend products to sell to customer based on history",
    "version": "12.0.1.0.0",
    "category": "Sales",
    "website": "https://github.com/ACA/sale-workflow",
    "author": "Tecnativa, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
    ],
    "data": [
        "wizards/sale_order_recommendation_view.xml",
        "views/sale_order_view.xml",
    ],
}
