# Copyright 2019 Tecnativa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from awkhad import api, fields, models


class PurchaseOrderRecommendation(models.TransientModel):
    _inherit = 'purchase.order.recommendation'

    product_brand_ids = fields.Many2many(
        comodel_name='product.brand',
        string="Brands",
    )

    def _get_products(self):
        """Filter products of the given brands"""
        products = super()._get_products()
        # Filter products by brand if set.
        # It will apply to show_all_partner_products as well
        if self.product_brand_ids:
            products = products.filtered(
                lambda x: x.product_brand_id in self.product_brand_ids)
        return products

    def _get_all_products_domain(self):
        """Filter products of the given brands"""
        domain = super()._get_all_products_domain()
        if self.product_brand_ids and not self.env.context.get(
                'no_brands_filter'):
            domain += [('product_brand_id', 'in', self.product_brand_ids.ids)]
        return domain

    @api.onchange(
        'order_id', 'date_begin', 'date_end', 'line_amount',
        'show_all_partner_products', 'show_all_products',
        'product_category_ids', 'warehouse_ids', 'product_brand_ids')
    def _generate_recommendations(self):
        """Just to add field to the onchange method"""
        return super()._generate_recommendations()

    @api.onchange('show_all_partner_products', 'show_all_products')
    def _onchange_products(self):
        """Restrict available brands domain"""
        products = self._get_supplier_products()
        # Gets all products avoiding to filter them by brand again
        if self.show_all_products:
            products += self.with_context(
                no_brands_filter=True).env['product.product'].search(
                    self._get_all_products_domain())
        brands = products.mapped('product_brand_id')
        return {'domain': {'product_brand_ids': [('id', 'in', brands.ids)]}}
