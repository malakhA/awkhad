import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_pos_is_loaded(self):
        # see more https://awkhad-development.readthedocs.io/en/latest/dev/tests/js.html#phantom-js-python-tests
        env = self.env

        pos_receipt = env['pos.custom_receipt'].search([('type', '=', 'receipt')], limit=1)
        self.assertTrue(pos_receipt, 'Receipt Not Found')

        pos_ticket = env['pos.custom_receipt'].search([('type', '=', 'ticket')], limit=1)
        self.assertTrue(pos_ticket, 'Ticket Not Found')

        main_pos_config = env.ref('point_of_sale.pos_config_main')

        main_pos_config.write({
            'proxy_ip': 'localhost',
            'iface_print_via_proxy': True,
            'custom_xml_receipt': True,
            'custom_xml_receipt_id': pos_receipt.id,
            'iface_print_auto': False,
            'custom_ticket': True,
            'custom_ticket_id': pos_ticket.id
        })

        self.phantom_js(
            '/web',

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".run('pos_receipt_custom_template_tour')",

            "awkhad.__DEBUG__.services['web_tour.tour']"
            ".tours.pos_receipt_custom_template_tour.ready",

            login="admin",
            timeout=240,
        )
