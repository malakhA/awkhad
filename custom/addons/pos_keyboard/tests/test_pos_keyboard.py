# Copyright 2019 Kolushov Alexandr <https://it-projects.info/team/kolushovalexandr>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_pos_keyboard(self):
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('pos_keyboard_tour', 500)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.pos_keyboard_tour.ready",
                        login="admin")
