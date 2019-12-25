from awkhad.http import request
from awkhad.addons.portal.controllers.portal import CustomerPortal


class MultiCompanyPortal(CustomerPortal):

    def _prepare_portal_layout_values(self):
        company = request.website.company_id
        user = request.env.user
        user.switch_multi_company(company)
        return super(MultiCompanyPortal, self)._prepare_portal_layout_values()
