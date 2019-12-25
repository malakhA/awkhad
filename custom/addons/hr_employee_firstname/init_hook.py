# Copyright 2016-2019 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from awkhad import SUPERUSER_ID
from awkhad.api import Environment


def post_init_hook(cr, _):
    with Environment.manage():
        env = Environment(cr, SUPERUSER_ID, {})
        env['hr.employee']._install_employee_firstname()
