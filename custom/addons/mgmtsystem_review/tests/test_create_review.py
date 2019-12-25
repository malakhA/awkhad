from awkhad.tests import common
from awkhad import fields


class TestModelReview(common.TransactionCase):
    """Test class for mgmtsystem_review."""

    def test_create_review(self):
        """Test object creation."""
        record = self.env['mgmtsystem.review'].create({
            "name": "SampleReview",
            "date": fields.Datetime.now()
        })

        self.assertEqual(record.name, "SampleReview")
        record.button_close()
        self.assertEqual(record.state, "done")
