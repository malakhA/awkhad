# Copyright 2019 ACSONE SA/NV
# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import _, api, fields, models


class AccountMoveBudget(models.Model):
    _name = "account.move.budget"
    _description = "Account Move Budget"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def _default_company(self):
        return self.env['res.company']. \
            _company_default_get('mis.budget')

    name = fields.Char(
        required=True,
        track_visibility='onchange',
    )
    description = fields.Char(
        track_visibility='onchange',
    )
    date_range_id = fields.Many2one(
        comodel_name='date.range',
        string='Date range',
    )
    date_from = fields.Date(
        required=True,
        string='From Date',
        track_visibility='onchange',
    )
    date_to = fields.Date(
        required=True,
        string='To Date',
        track_visibility='onchange',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('cancelled', 'Cancelled')],
        required=True,
        default='draft',
        track_visibility='onchange',
    )
    line_ids = fields.One2many(
        comodel_name='account.move.budget.line',
        inverse_name='budget_id',
        copy=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=_default_company,
    )

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)") % self.name
        return super(AccountMoveBudget, self).copy(default=default)

    @api.onchange('date_range_id')
    def _onchange_date_range(self):
        for rec in self:
            if rec.date_range_id:
                rec.date_from = rec.date_range_id.date_start
                rec.date_to = rec.date_range_id.date_end

    @api.onchange('date_from', 'date_to')
    def _onchange_dates(self):
        for rec in self:
            if rec.date_range_id:
                if rec.date_from != rec.date_range_id.date_start or \
                        rec.date_to != rec.date_range_id.date_end:
                    rec.date_range_id = False

    @api.multi
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.multi
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    @api.multi
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
