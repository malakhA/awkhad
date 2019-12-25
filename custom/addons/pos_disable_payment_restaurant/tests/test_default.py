import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_pos_dis_pay_rest(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_disable_payment_restaurant_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_disable_payment_restaurant_tour.ready",

            login="admin",
            timeout=5000,
        )
