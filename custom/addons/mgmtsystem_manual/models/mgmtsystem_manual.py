# Copyright 2019 Awkhad Community Association
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import models, fields


class MgmtSystemManual(models.Model):
    _inherit = 'mgmtsystem.system'

    manual_id = fields.Many2one(
        'document.page',
        string='Manual'
    )
