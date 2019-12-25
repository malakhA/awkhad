# Copyright 2016 Ucamco - Wim Audenaert <wim.audenaert@ucamco.com>
# Copyright 2016-19 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'MRP Multi Level',
    'version': '12.0.1.0.1',
    'development_status': 'Beta',
    'license': 'LGPL-3',
    'author': 'Ucamco, '
              'Eficent, '
              'Awkhad Community Association (ACA)',
    'maintainers': ['jbeficent', 'lreficent'],
    'summary': 'Adds an MRP Scheduler',
    'website': 'https://github.com/ACA/manufacture',
    'category': 'Manufacturing',
    'depends': [
        'mrp',
        'purchase_stock',
        'mrp_warehouse_calendar',
    ],
    'data': [
        'security/mrp_multi_level_security.xml',
        'security/ir.model.access.csv',
        'views/mrp_area_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/product_mrp_area_views.xml',
        'views/stock_location_views.xml',
        'wizards/mrp_inventory_procure_views.xml',
        'views/mrp_inventory_views.xml',
        'wizards/mrp_multi_level_views.xml',
        'views/mrp_menuitem.xml',
        'data/mrp_multi_level_cron.xml',
        'data/mrp_area_data.xml',
    ],
    'demo': [
        'demo/product_category_demo.xml',
        'demo/product_product_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/product_supplierinfo_demo.xml',
        'demo/product_mrp_area_demo.xml',
        'demo/mrp_bom_demo.xml',
        'demo/initial_on_hand_demo.xml',
    ],
    'installable': True,
    'application': True,
}
