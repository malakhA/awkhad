# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests


@awkhad.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(awkhad.tests.HttpCase):

    def test_01_click_everywhere_as_admin(self):
        self.browser_js("/web", "awkhad.__DEBUG__.services['web.clickEverywhere']();", "awkhad.isReady === true", login="admin", timeout=45*60)


@awkhad.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(awkhad.tests.HttpCase):

    def test_01_click_everywhere_as_demo(self):
        self.browser_js("/web", "awkhad.__DEBUG__.services['web.clickEverywhere']();", "awkhad.isReady === true", login="demo", timeout=1800)
