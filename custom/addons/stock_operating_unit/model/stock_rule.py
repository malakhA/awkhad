# © 2019 Eficent Business and IT Consulting Services S.L.
# © 2019 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from awkhad import fields, models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    operating_unit_id = fields.Many2one(
        'operating.unit',
        related='warehouse_id.operating_unit_id',
        domain="[('user_ids', '=', uid)]")
