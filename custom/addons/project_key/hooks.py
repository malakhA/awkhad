# Copyright 2017 - 2018 Mawkhadlar <info@mawkhadlar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).


def post_init_hook(cr, registry):
    from awkhad import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['project.project']._set_default_project_key()
