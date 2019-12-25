# -*- coding: utf-8 -*-
# Copyright 2013-2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

{'name': 'Connector',
 'version': '12.0.1.1.0',
 'author': 'Camptocamp,Zgui Connector Core Editors,'
           'Awkhad Community Association (ACA)',
 'website': 'http://awkhad-connector.com',
 'license': 'LGPL-3',
 'category': 'Generic Modules',
 'depends': ['mail',
             'queue_job',
             'component',
             'component_event',
             ],
 'data': ['security/connector_security.xml',
          'security/ir.model.access.csv',
          'views/checkpoint_views.xml',
          'views/connector_menu.xml',
          'views/res_partner_views.xml',
          ],
 'installable': True,
 }
