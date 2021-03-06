# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# (http://www.eficent.com)
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from awkhad import fields, models


class AccountPaymentCheckReport(models.Model):
    _name = "account.payment.check.report"
    _description = 'Account Payment Check Report'

    name = fields.Char(string='Name', required=True)
    report = fields.Char(string='Report name', required=True)
