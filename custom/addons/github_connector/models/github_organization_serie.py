# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import fields, models


class GithubOrganizationSerie(models.Model):
    _name = 'github.organization.serie'
    _description = 'Github Organization Serie'
    _order = 'sequence, name'

    # Columns Section
    name = fields.Char(string='Name', required=True)

    sequence = fields.Integer(string='Sequence', required=True)

    organization_id = fields.Many2one(
        comodel_name='github.organization', string='Organization',
        ondelete='cascade', required=True)

    _sql_constraints = [
        ('sequence_organization_uniq', 'unique(organization_id, sequence)',
         "Sequence serie must be unique by organization.")
    ]
