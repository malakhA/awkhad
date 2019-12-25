# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class FSMEquipment(models.Model):
    _inherit = 'fsm.equipment'

    agreement_id = fields.Many2one('agreement', string='Agreement')
    serviceprofile_id = fields.Many2one('agreement.serviceprofile',
                                        'Service Profile')
