# Copyright 2014-2015 Akretion <http://www.akretion.com>
# Copyright 2014-2016 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import api, fields, models
import awkhad.addons.decimal_precision as dp


class StockQuantPackage(models.Model):
    _inherit = 'stock.quant.package'

    parcel_tracking = fields.Char(string='Parcel Tracking')
    parcel_tracking_uri = fields.Char(
        help="Link to the carrier's tracking page for this package.",
    )
    total_weight = fields.Float(
        digits=dp.get_precision('Stock Weight'),
        help="Total weight of the package in kg, including the "
             "weight of the logistic unit."
    )

    @api.depends('total_weight')
    def _compute_weight(self):
        """ Use total_weight if defined
        otherwise fallback on the computed weight
        """
        to_do = self.browse()
        for pack in self:
            if pack.total_weight:
                pack.weight = pack.total_weight
            elif not pack.quant_ids:
                # package.pack_operations would be too easy
                operations = self.env['stock.move.line'].search([
                    ('result_package_id', '=', pack.id),
                    ('product_id', '!=', False),
                ])

                # we make use get_weight with  @api.multi instead of
                # sum([op.get_weight for op in operations])

                # sum of the pack_operation
                payload_weight = operations.get_weight()

                # sum and save in package
                pack.weight = payload_weight

            else:
                to_do |= pack
        if to_do:
            super(StockQuantPackage, to_do)._compute_weight()

    @api.multi
    def _complete_name(self, name, args):
        res = super()._complete_name(name, args)
        for pack in self:
            if pack.parcel_tracking:
                res[pack.id] += ' [%s]' % pack.parcel_tracking
            if pack.weight:
                res[pack.id] += ' %s kg' % pack.weight
        return res
