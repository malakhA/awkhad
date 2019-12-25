import awkhad.tests


@awkhad.tests.common.at_install(False)
@awkhad.tests.common.post_install(True)
class TestUi(awkhad.tests.HttpCase):

    def test_01_mail_base(self):
        # wait till page loaded
        code = """
            setTimeout(function () {
                console.log('ok');
            }, 1000);
        """
        link = '/web#action=%s' % self.ref('mail.mail_channel_action_client_chat')
        self.phantom_js(link, code, "awkhad.__DEBUG__.services['mail_base.base']", login="admin")
