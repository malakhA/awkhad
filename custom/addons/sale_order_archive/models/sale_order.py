# Copyright 2017-2018 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    active = fields.Boolean(default=True)
