# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from awkhad import fields, models


class PurchaseApprovalBlockReason(models.Model):
    _name = 'purchase.approval.block.reason'
    _description = 'Purchase Approval Block Reason'

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)
