# -*- coding: utf-8 -*-

import awkhad

def migrate(cr, version):
    registry = awkhad.registry(cr.dbname)
    from awkhad.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
