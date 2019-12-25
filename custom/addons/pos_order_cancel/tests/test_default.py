# Copyright 2017-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017 gaelTorrecillas <https://github.com/gaelTorrecillas>
# Copyright 2017 Gabbasov Dinar <https://it-projects.info/team/GabbasovDinar>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_order_cancel_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_order_cancel_tour.ready",

            login="admin",
            timeout=240,
        )
