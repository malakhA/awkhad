import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_print_method_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_print_method_tour.ready",

            login="admin",
            timeout=240,
        )
