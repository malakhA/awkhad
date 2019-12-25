
from zgui import fields
from zgui import models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    oil_change_odometer = fields.Float("Last oil change (odometer)")
