# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.
import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):
    def test_01_wishlist_tour(self):
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_wishlist')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_wishlist.ready")
