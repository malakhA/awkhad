# -*- coding: utf-8 -*-

import awkhad

def migrate(cr, version):
    registry = awkhad.registry(cr.dbname)
    from awkhad.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_hr')
