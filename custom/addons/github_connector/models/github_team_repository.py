# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from awkhad import fields, models


class GithubTeamRepository(models.Model):
    _name = 'github.team.repository'
    _description = 'Github Team Repository'
    _order = 'team_id, repository_id'

    _PERMISSION_SELECTION = [
        ('undefined', 'Undefined'),
        ('read', 'Read'),
        ('write', 'Write'),
        ('admin', 'Admin'),
    ]

    # Column Section
    team_id = fields.Many2one(
        comodel_name='github.team', string='Team',
        required=True, index=True, readonly=True, ondelete='cascade')

    repository_id = fields.Many2one(
        comodel_name='github.repository', string='Repository',
        required=True, index=True, readonly=True, ondelete='cascade')

    permission = fields.Selection(
        selection=_PERMISSION_SELECTION, string='Permission', required=True,
        readonly=True)
