# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from awkhad import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    crossovered_budget_line_ids = fields.One2many(
        comodel_name='crossovered.budget.lines',
        inverse_name='analytic_account_id', string='Budget Lines')
