# Copyright 2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import awkhad.tests
from awkhad.api import Environment


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_postponed_invoice(self):

        self.phantom_js('/pos/web?m=1',
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('pos_invoice_postponed_tour', 1000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.pos_invoice_postponed_tour.ready",
                        login="admin", timeout=240)

        cr = self.registry.cursor()
        cr.execute('select "id" from "pos_order" order by "id" desc limit 1')
        res = cr.fetchall()
        env = Environment(cr, self.uid, {})
        order = env['pos.order'].browse(res[0])

        self.assertEqual(len(order.statement_ids), 0, 'Number of statements are %s expected %s' % (len(order.statement_ids), 0))
        self.assertEqual(order.amount_paid, 0, 'Amount paid is %s expected %s' % (order.amount_paid, 0))
        cr.release()
