# -*- coding: utf-8 -*-

from awkhad import fields, models, _

from awkhad.tools.float_utils import float_is_zero

from awkhad.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    stock_move_id = fields.Many2one('stock.move', string='Stock Move')
