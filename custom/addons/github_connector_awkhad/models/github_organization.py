# Copyright (C) 2016-Today: Awkhad Community Association (ACA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from awkhad import fields, models


class GithubOrganization(models.Model):
    _inherit = 'github.organization'

    runbot_parse_url = fields.Char(
        string='URL For Runbot Ids', oldname='runbot_url')

    default_author_text = fields.Char(string='Default Author Text')

    runbot_url_pattern = fields.Char(string='Runbot URL Pattern')
