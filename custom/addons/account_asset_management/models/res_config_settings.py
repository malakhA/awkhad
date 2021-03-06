# Copyright (c) 2014 ACSONE SA/NV (http://acsone.eu).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import fields, models


class Config(models.TransientModel):
    _inherit = 'res.config.settings'

    module_account_asset_management = fields.Boolean(
        string='Assets management (ACA)',
        help="""This allows you to manage the assets owned by a company
                or a person. It keeps track of the depreciation occurred
                on those assets, and creates account move for those
                depreciation lines.
                This installs the module account_asset_management.""")
