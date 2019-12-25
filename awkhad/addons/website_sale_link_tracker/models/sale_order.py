# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from awkhad import models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ['utm.mixin', 'sale.order']
