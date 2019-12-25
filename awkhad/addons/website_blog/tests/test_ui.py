# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests


@awkhad.tests.tagged('post_install', '-at_install')
class TestUi(awkhad.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('blog')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.blog.ready", login='admin')
