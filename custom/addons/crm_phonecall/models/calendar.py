# Copyright 2004-2016 Awkhad SA (<http://www.awkhad.com>)
# Copyright 2017 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class CalendarEvent(models.Model):
    """Enhance the calendar event to add phonecall data."""

    _inherit = "calendar.event"

    phonecall_id = fields.Many2one(
        comodel_name='crm.phonecall',
        string='Phonecall',
    )
