# Copyright 2019 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_pos_print_check(self):

        env = self.env
        env['ir.module.module'].search([('name', '=', 'pos_order_print_check')], limit=1).state = 'installed'

        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_order_print_check_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_order_print_check_tour.ready",

            login="admin",
            timeout=1000,
        )
