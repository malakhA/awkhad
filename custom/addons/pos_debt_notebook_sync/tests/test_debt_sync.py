# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_pos_debt(self):
        # without a delay there might be problems caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('tour_pos_debt_notebook', 1000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.tour_pos_debt_notebook.ready",
                        login="admin", timeout=1000)
