# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import api, fields, models


class Agreement(models.Model):
    _inherit = "agreement"

    mr_count = fields.Integer('# Maintenance Requests',
                              compute='_compute_mr_count')

    @api.multi
    def _compute_mr_count(self):
        for ag_rec in self:
            ag_rec.mr_count = self.env['maintenance.request'].search_count(
                [('agreement_id', 'in', ag_rec.ids)])
