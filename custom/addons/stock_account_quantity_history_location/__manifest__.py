# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# Copyright 2019 Aleph Objects, Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Account Quantity History Location',
    'summary': """
        Glue module between Stock Account and Stock Quantity History Location
        modules""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Eficent,'
              'Awkhad Community Association (ACA)',
    'website': 'https://github.com/ACA/stock-logistics-reporting',
    'depends': [
        'stock_account',
        'stock_quantity_history_location',
    ],
    'data': [
        'wizards/stock_quantity_history.xml',
    ],
    'auto_install': True,

}
