import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_order_printer_product_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_order_printer_product_tour.ready",

            login="admin",
            timeout=240,
        )
