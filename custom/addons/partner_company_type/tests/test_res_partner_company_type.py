# Copyright 2017-2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from awkhad import tools

from awkhad.tests import SavepointCase
from psycopg2 import IntegrityError


class TestResPartnerCompanyType(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestResPartnerCompanyType, cls).setUpClass()
        cls.company_type = cls.env.ref(
            'partner_company_type.res_partner_company_type_sa')

    def test_00_duplicate(self):
        # Test Duplicate Company type

        with self.assertRaises(IntegrityError), tools.mute_logger(
                "awkhad.sql_db"):
            self.company_type.create(dict(
                name=self.company_type.name,
            ))
