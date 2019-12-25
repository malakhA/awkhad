import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_check_timer(self):
        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('project_timelog_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.project_timelog_tour.ready",

            login="admin",
        )
