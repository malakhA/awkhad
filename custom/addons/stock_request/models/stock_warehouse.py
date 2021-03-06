# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from awkhad import api, models, _
from awkhad.exceptions import ValidationError


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    @api.constrains('company_id')
    def _check_company_stock_request(self):
        if any(self.env['stock.request'].search(
                [('company_id', '!=', rec.company_id.id),
                 ('warehouse_id', '=', rec.id)], limit=1)
               for rec in self):
            raise ValidationError(
                _('You cannot change the company of the warehouse, as it is '
                  'already assigned to stock requests that belong to '
                  'another company.'))
        if any(self.env['stock.request.order'].search(
                [('company_id', '!=', rec.company_id.id),
                 ('warehouse_id', '=', rec.id)], limit=1)
               for rec in self):
            raise ValidationError(
                _('You cannot change the company of the warehouse, as it is '
                  'already assigned to stock request orders that belong to '
                  'another company.'))
