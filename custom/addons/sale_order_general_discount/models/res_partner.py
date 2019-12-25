# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import fields, models
from awkhad.addons import decimal_precision as dp


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_discount = fields.Float(
        digits=dp.get_precision('Discount'),
        string='Discount (%)',
        company_dependent=True,
    )
