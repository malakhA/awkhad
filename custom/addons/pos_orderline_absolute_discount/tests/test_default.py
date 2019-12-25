import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        self.phantom_js(
            '/web?debug=assets',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_orderline_absolute_discount_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_orderline_absolute_discount_tour.ready",

            login="admin",
            timeout=240,
        )
