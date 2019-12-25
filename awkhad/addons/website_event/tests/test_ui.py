import awkhad.tests


@awkhad.tests.tagged('post_install', '-at_install')
class TestUi(awkhad.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('event')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.event.ready", login='admin')
