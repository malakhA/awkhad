import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_longpolling_pos(self):
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('longpoll_connection_tour')",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.longpoll_connection_tour.ready",
                        login="admin")
