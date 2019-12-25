import awkhad.tests
from awkhad import api


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_add_to_cart(self):
        self.phantom_env = api.Environment(self.registry.test_cr, self.uid, {})
        settings = self.phantom_env['res.config.settings']
        # a reload is needed for the module to work correctly with multi themes
        if hasattr(settings, 'multi_theme_reload'):
            settings.multi_theme_reload()
        # delay is added to be sure that all elements have been rendered properly
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('shop_add_to_cart', 1500)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.shop_add_to_cart.ready",
                        login='admin')
