import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        env = self.env
        product = env.ref('point_of_sale.led_lamp')
        product.write({
            'pos_category_ids': [(4, category.id) for category in env['pos.category'].search([])]
        })

        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_category_multi_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_category_multi_tour.ready",

            login="admin",
            timeout=240,
        )
