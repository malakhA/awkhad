import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_res_partner_skype(self):
        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        env = self.env
        env['ir.module.module'].search([('name', '=', 'res_partner_skype')], limit=1).state = 'installed'
        env['res.partner'].search(([('id', '=', 9)]), limit=1).write({
            'skype': 'skype_test',
        })

        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js("/web#id=9&view_type=form&model=res.partner",
                        "awkhad.__DEBUG__.services['web_tour.tour'].run('tour_res_partner_skype', 1000)",
                        "awkhad.__DEBUG__.services['web_tour.tour'].tours.tour_res_partner_skype.ready",
                        login="admin", timeout=300)
