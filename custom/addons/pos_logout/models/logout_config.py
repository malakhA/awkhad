# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from awkhad import fields
from awkhad import models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    logout_interval = fields.Integer(string='Screen Autolock', default=0, help="The last activity interval to activate the automatic screen lock. Zero if autolocking is not needed")
