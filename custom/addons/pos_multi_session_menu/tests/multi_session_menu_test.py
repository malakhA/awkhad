import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def multi_session_menu_test(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_multi_session_menu_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_multi_session_menu_tour.ready",

            login="admin",
            timeout=240,
        )
