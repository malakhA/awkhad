# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    qc_team_id = fields.Many2one(
        comodel_name='qc.team', string='Quality Control Team')
