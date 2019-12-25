# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests

@awkhad.tests.tagged('post_install', '-at_install')
class TestUi(awkhad.tests.HttpCase):

    def test_01_admin_rte(self):
        self.phantom_js("/web", "awkhad.__DEBUG__.services['web_tour.tour'].run('rte')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.rte.ready", login='admin')

    def test_02_admin_rte_inline(self):
        self.phantom_js("/web", "awkhad.__DEBUG__.services['web_tour.tour'].run('rte_inline')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.rte_inline.ready", login='admin')
