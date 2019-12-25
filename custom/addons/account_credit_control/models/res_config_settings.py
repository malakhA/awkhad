# Copyright 2012-2017 Camptocamp SA
# Copyright 2017 Okia SPRL (https://okia.be)
# Copyright 2018 Access Bookings Ltd (https://accessbookings.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    credit_control_tolerance = fields.Float(
        related="company_id.credit_control_tolerance",
        readonly=False,
    )
    credit_policy_id = fields.Many2one(
        comodel_name='credit.control.policy',
        related="company_id.credit_policy_id",
        readonly=False,
        string='Credit Control Policy',
        help="The Credit Control Policy used "
             "on partners by default. "
             "This setting can be overridden"
             " on partners or invoices.",
    )
