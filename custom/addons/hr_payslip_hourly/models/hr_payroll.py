# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from awkhad import fields, models, api, _
from datetime import datetime, timedelta


class hr_contract(models.Model):
    _inherit = 'hr.contract'

    is_hourly_pay = fields.Boolean(string='Hourly Pay')


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    total_hours = fields.Char(string="Total Hours", compute='_compute_employee_total_hours')

    @api.multi
    @api.depends('date_to', 'date_from', 'employee_id')
    def _compute_employee_total_hours(self):
        for payslip in self:
            att_ids = self.env['hr.attendance'].search([('employee_id', '=', payslip.employee_id.id),
                                                        ('check_out', '>=', datetime.strptime(str(payslip.date_from), '%Y-%m-%d').strftime('%Y-%m-%d 00:00:00')),
                                                        ('check_out', '<=', datetime.strptime(str(payslip.date_to), '%Y-%m-%d').strftime('%Y-%m-%d 23:59:59'))
                                                        ])
            if att_ids:
                total_seconds = 0
                for att in att_ids:
                    record_time = str(timedelta(hours=att.worked_hours)).split(':')
                    if record_time and len(record_time) >= 2:
                        conv_time = datetime.strptime(record_time[0] + ':' + record_time[1], '%H:%M')
                        if conv_time:
                            total_seconds += conv_time.minute * 60 + conv_time.hour * 3600
                day = total_seconds // 86400
                hour = (total_seconds - (day * 86400)) // 3600
                minute = (total_seconds - ((day * 86400) + (hour * 3600))) // 60
                payslip.total_hours = str(hour + (24 * day)) + ':' + str(minute)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
