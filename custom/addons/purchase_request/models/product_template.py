# Copyright 2018-2019 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

from awkhad import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    purchase_request = fields.Boolean(
        help="Check this box to generate Purchase Request instead of "
             "generating Requests For Quotation from procurement."
    )
