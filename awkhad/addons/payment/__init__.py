# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from awkhad import api, SUPERUSER_ID

from . import models
from . import controllers
from . import wizards

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['payment.transaction'].search([]).unlink()
