# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests


@awkhad.tests.tagged('post_install','-at_install')
class TestUi(awkhad.tests.HttpCase):

    def test_01_crm_tour(self):
        self.phantom_js("/web", "awkhad.__DEBUG__.services['web_tour.tour'].run('crm_tour')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.crm_tour.ready", login="admin")
