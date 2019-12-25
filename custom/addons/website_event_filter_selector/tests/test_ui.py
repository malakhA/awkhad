# Copyright 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from awkhad.tests.common import HttpCase


class UICase(HttpCase):
    def test_ui_website(self):
        """Test frontend tour."""
        self.browser_js(
            url_path="/event",
            code="awkhad.__DEBUG__.services['web_tour.tour']"
                 ".run('website_event_filter_selector')",
            ready="awkhad.__DEBUG__.services['web_tour.tour']"
                  ".tours.website_event_filter_selector.ready",
        )
