# Copyright 2018 Road-Support - Roel Adriaans
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import api, fields, models


class AwkhadModuleVersion(models.Model):
    _inherit = 'awkhad.module.version'

    _AWKHAD_DEVELOPMENT_STATUS_SELECTION = [
        ('alpha', 'Alpha'),
        ('beta', 'Beta'),
        ('production/stable', 'Production/Stable'),
        ('mature', 'Mature'),
    ]

    development_status = fields.Selection(
        string='Module maturity',
        selection=_AWKHAD_DEVELOPMENT_STATUS_SELECTION,
        readonly=True,
    )

    @api.model
    def manifest_2_awkhad(self, info, repository_branch, module):
        res = super(AwkhadModuleVersion, self).manifest_2_awkhad(
            info, repository_branch, module
        )
        if 'development_status' in info:
            res['development_status'] = info['development_status'].lower()
        return res
