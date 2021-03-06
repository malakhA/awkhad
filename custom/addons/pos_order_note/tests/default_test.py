import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded_and_added_note_to_order(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_order_note_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_order_note_tour.ready",

            login="admin",
            timeout=240,
        )
