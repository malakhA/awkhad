# Copyright (C) 2017-Today: Awkhad Community Association (ACA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    download_count = fields.Integer()
