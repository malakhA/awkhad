# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class MediaType(models.Model):
    _name = "storage.media.type"
    _description = "Storage Media Type"

    name = fields.Char(translated=True, required=True)
    code = fields.Char()
