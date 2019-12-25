# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Oscar Alcala (https://twitter.com/oscarolar)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import fields, models


class AwkhadCategory(models.Model):
    _name = 'awkhad.category'
    _description = 'Awkhad Category'

    name = fields.Char()
