# Copyright 2015-17 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Picking Show Backorder',
    'version': '12.0.1.0.0',
    'category': 'Warehouse Management',
    'summary': "Provides a new field on stock pickings, allowing to display "
               "the corresponding backorders.",
    'author': "Eficent, "
              "Awkhad Community Association (ACA)",
    'website': 'https://github.com/ACA/stock-logistics-workflow',
    'depends': ['stock'],
    'data': [
        'views/stock_view.xml',
    ],
    'installable': True,
    'license': "AGPL-3",
}
