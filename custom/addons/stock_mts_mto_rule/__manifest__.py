# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock MTS+MTO Rule',
    'summary': 'Add a MTS+MTO route',
    'version': '12.0.1.0.1',
    'development_status': 'Mature',
    'category': 'Warehouse',
    'website': 'https://github.com/ACA/stock-logistics-warehouse',
    'author': 'Akretion,Awkhad Community Association (ACA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'stock',
    ],
    'data': [
        'data/stock_data.xml',
        'view/pull_rule.xml',
        'view/warehouse.xml',
    ],
}
