
import awkhad.tests


@awkhad.tests.common.at_install(True)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):
    def test_open_url(self):
        # wait till page loaded
        code = """
            setTimeout(function () {
                console.log('ok');
            }, 3000);
        """
        link = '/web/login'
        self.phantom_js(link, code, "", login="admin")
