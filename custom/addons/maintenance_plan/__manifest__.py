# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{'name': 'Maintenance Plan',
 'summary': 'Extends preventive maintenance planning',
 'version': '12.0.1.2.0',
 'author': 'Awkhad Community Association (ACA), Camptocamp SA',
 'license': 'AGPL-3',
 'category': 'Maintenance',
 'website': 'https://github.com/ACA/maintenance',
 'images': [],
 'depends': [
     'maintenance',
     ],
 'data': [
     'security/ir.model.access.csv',
     'views/maintenance.xml'
     ],
 'demo': [
     'data/demo_maintenance_plan.xml'
 ],
 'post_init_hook': 'post_init_hook',
 'installable': True,
 }
