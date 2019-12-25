# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
# Copyright 2017 Kolushov Alexandr <https://github.com/KolushovAlexandr>

import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_sale_available(self):
        # delay is added to be sure that all elements have been rendered properly
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_sale_available', 1000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_sale_available.ready",
                        login='admin')
