# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.
import awkhad.tests


@awkhad.tests.tagged('post_install', '-at_install')
class TestUi(awkhad.tests.HttpCase):
    def test_01_portal_load_tour(self):
        self.phantom_js(
            "/",
            "awkhad.__DEBUG__.services['web_tour.tour'].run('portal_load_homepage')",
            "awkhad.__DEBUG__.services['web_tour.tour'].tours.portal_load_homepage.ready",
            login="portal"
        )
