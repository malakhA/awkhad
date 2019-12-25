# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad.tests


@awkhad.tests.tagged('post_install', '-at_install')
class TestWebsiteCrm(awkhad.tests.HttpCase):

    def test_tour(self):
        self.phantom_js("/", "awkhad.__DEBUG__.services['web_tour.tour'].run('website_crm_tour')", "awkhad.__DEBUG__.services['web_tour.tour'].tours.website_crm_tour.ready")

        # check result
        record = self.env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        self.assertEqual(len(record), 1)
        self.assertEqual(record.contact_name, 'John Smith')
        self.assertEqual(record.email_from, 'john@smith.com')
        self.assertEqual(record.partner_name, 'Awkhad S.A.')
