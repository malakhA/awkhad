# Copyright 2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_open_pos(self):
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('tour_pos_multi_session', 500)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.tour_pos_multi_session.ready",
                        login="admin", timeout=80)
