# Copyright (C) 2019 Open Source Integrators
# Copyright (C) 2019 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    consolidated_by_id = fields.Many2one('account.invoice',
                                         string='Consolidated In',
                                         readonly=True, ondelete='restrict',
                                         copy=False)
