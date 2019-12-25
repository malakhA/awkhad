# Copyright (C) 2017-Today: Awkhad Community Association (ACA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from awkhad import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    awkhad_module_id = fields.Many2one(
        'awkhad.module',
        'Awkhad Module',
        readonly=True,
    )
    technical_name = fields.Char(
        "Technical Name",
        related="awkhad_module_id.technical_name",
        store=True,
    )
    image_module = fields.Binary(
        'Icon Image',
        readonly=True,
        related="awkhad_module_id.image",
    )
