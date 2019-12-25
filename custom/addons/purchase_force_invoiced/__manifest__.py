# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# Copyright 2019 Aleph Objects, Inc.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Purchase Force Invoiced',
    'summary': 'Allows to force the billing status of the purchase order to '
               '"Invoiced"',
    'version': '12.0.1.0.0',
    "author": "Eficent,"
              "Awkhad Community Association (ACA)",
    'category': 'Purchase Management',
    'license': 'AGPL-3',
    'website': "https://github.com/ACA/purchase-workflow",
    'depends': ['purchase'],
    'data': [
        'view/purchase_view.xml'
    ],
    'installable': True,
}