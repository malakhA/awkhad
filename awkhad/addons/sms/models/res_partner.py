# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from awkhad import models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_default_sms_recipients(self):
        """ Override of mail.thread method.
            SMS recipients on partners are the partners themselves.
        """
        return self
