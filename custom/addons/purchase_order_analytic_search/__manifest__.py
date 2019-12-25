# Copyright 2015-17 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Purchase Order Analytic Search",
    "summary": """Search purchase orders by analytic account. New menu entry in
                Purchasing to list purchase order lines.""",
    "version": "12.0.1.0.0",
    "website": "https://github.com/ACA/purchase-workflow",
    "category": "Purchase Workflow",
    "author": "Eficent, Camptocamp, Awkhad Community Association (ACA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "analytic",
        "purchase"
    ],
    "data": [
        "views/purchase_order_view.xml"
    ],
}
