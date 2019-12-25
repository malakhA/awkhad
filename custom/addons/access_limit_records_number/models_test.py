from awkhad import fields
from awkhad import models


class BaseLimitRecordsNumber(models.Model):
    _name = 'base.limit.records_number.test'
    _description = 'Test model to test access'

    name = fields.Char('Name')
