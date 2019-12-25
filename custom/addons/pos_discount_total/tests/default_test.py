import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded_and_set_discount(self):
        self.phantom_js(
            '/web?debug=assets',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_discount_total_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_discount_total_tour.ready",

            login="admin",
            timeout=240,
        )
