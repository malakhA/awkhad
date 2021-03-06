# Copyright 2017 Syvain Van Hoof (Okia sprl) <sylvainvh@okia.be>
# Copyright 2016-2019 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock Location Zone',
    'version': '12.0.1.0.0',
    'author': "BCIM, Okia, Camptocamp, Awkhad Community Association (ACA)",
    'website': "https://github.com/ACA/stock-logistics-warehouse",
    'summary': "Add coordinate attributes on stock location. "
               "Define picking zone with links to picking type.",
    'category': 'Stock Management',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking_zone.xml',
        'views/stock_location.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'development_status': 'Alpha',
    'license': 'AGPL-3',
}
