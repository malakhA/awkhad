# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad.addons.component.core import Component


class AlgoliaConnectorComponent(Component):
    _name = "algolia.se.connector"
    _inherit = "base.se.connector"
    _collection = "se.backend.algolia"
    _record_id_key = "objectID"
