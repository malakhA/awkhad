# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Sale Invoice Group Method",
    "summary": "This module allows you to combine several"
               "Sales Orders into a single invoice,"
               "if they meet the group criteria defined by the "
               "'Invoice Group Method'",
    "author": "Eficent, Awkhad Community Association (ACA)",
    "version": "12.0.1.0.0",
    "category": "Sale Workflow",
    "website": "https://github.com/ACA/sale-workflow",
    "license": 'LGPL-3',
    "depends": [
        'account',
        'sale_order_action_invoice_create_hook',
    ],
    "data": [
        'security/ir.model.access.csv',
        'view/res_partner_view.xml',
        'view/sale_order_view.xml',
        'view/sale_invoice_group_method_view.xml',
        'view/menu.xml',
    ],
    "installable": True
}
