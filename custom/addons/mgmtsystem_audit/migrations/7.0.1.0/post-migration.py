# -*- coding: utf-8 -*-
##############################################################################
#
#    ZgUI, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

logger = logging.getLogger('upgrade')


def migrate(cr, version):
    if version is None:
        return
    logger.info("Migrating mgmtsystem_audit from version %s", version)
    logger.info("Updating state flags")
    cr.execute("update mgmtsystem_audit set state = 'open' where state = 'o'")
    cr.execute("update mgmtsystem_audit set state = 'done' where state = 'c'")
    logger.info("mgmtsystem_audit update... done!")
