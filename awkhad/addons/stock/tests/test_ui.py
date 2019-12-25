# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests

@awkhad.tests.tagged('post_install', '-at_install')
class TestUi(awkhad.tests.HttpCase):

    def test_01_admin_stock_route(self):
        self.phantom_js("/web", "awkhad.__DEBUG__.services['web_tour.tour'].run('stock')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.stock.ready", login='admin')
