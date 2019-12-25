# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch

from awkhad.addons.test_mail.tests.common import BaseFunctionalTest, MockEmails, TestRecipients
from awkhad.tools import mute_logger
from awkhad.tests import tagged


@tagged("awkhadbot")
class TestAwkhadbot(BaseFunctionalTest, MockEmails, TestRecipients):

    def setUp(self):
        super(TestAwkhadbot, self).setUp()
        self.awkhadbot = self.env.ref("base.partner_root")
        self.message_post_default_kwargs = {
            'body': '',
            'attachment_ids': [],
            'message_type': 'comment',
            'partner_ids': [],
            'subtype': 'mail.mt_comment'
        }
        self.awkhadbot_ping_body = '<a href="http://awkhad.com/web#model=res.partner&amp;id=%s" class="o_mail_redirect" data-oe-id="%s" data-oe-model="res.partner" target="_blank">@AwkhadBot</a>' % (self.awkhadbot.id, self.awkhadbot.id)
        self.test_record_employe = self.test_record.sudo(self.user_employee)

    @mute_logger('awkhad.addons.mail.models.mail_mail')
    def test_fetch_listener(self):
        channel = self.env['mail.channel'].sudo(self.user_employee).init_awkhadbot()
        partners = self.env['mail.channel'].channel_fetch_listeners(channel.uuid)
        awkhadbot = self.env.ref("base.partner_root")
        awkhadbot_in_fetch_listeners = [partner for partner in partners if partner['id'] == awkhadbot.id]
        self.assertEqual(len(awkhadbot_in_fetch_listeners), 1, 'awkhadbot should appear only once in channel_fetch_listeners')

    @mute_logger('awkhad.addons.mail.models.mail_mail')
    def test_awkhadbot_ping(self):
        kwargs = self.message_post_default_kwargs.copy()
        kwargs.update({'body': self.awkhadbot_ping_body, 'partner_ids': [self.awkhadbot.id, self.user_admin.partner_id.id]})

        with patch('random.choice', lambda x: x[0]):
            self.assertNextMessage(
                self.test_record_employe.with_context({'mail_post_autofollow': True}).message_post(**kwargs),
                sender=self.awkhadbot,
                answer=["Yep, AwkhadBot is in the place!"]
            )
        # Awkhadbot should not be a follower but user_employee and user_admin should
        follower = self.test_record.message_follower_ids.mapped('partner_id')
        self.assertNotIn(self.awkhadbot, follower)
        self.assertIn(self.user_employee.partner_id, follower)
        self.assertIn(self.user_admin.partner_id, follower)

    @mute_logger('awkhad.addons.mail.models.mail_mail')
    def test_onboarding_flow(self):
        kwargs = self.message_post_default_kwargs.copy()
        channel = self.env['mail.channel'].sudo(self.user_employee).init_awkhadbot()

        kwargs['body'] = 'tagada 😊'
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.awkhadbot,
            answer=("attachment",)
        )
        kwargs['body'] = ''
        kwargs['attachment_ids'] = [1]
        last_message = self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.awkhadbot,
            answer=("help",)
        )
        kwargs['attachment_ids'] = []

        channel.execute_command(command="help")
        self.assertNextMessage(
            last_message,  # no message will be post with command help, use last awkhadbot message instead
            sender=self.awkhadbot,
            answer=("@AwkhadBot",)
        )
        # we dont test the end of the flow since it will depends of the installed apps (livechat)
        self.user_employee.awkhadbot_state = "idle"
        kwargs['partner_ids'] = []
        kwargs['body'] = "I love you"
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.awkhadbot,
            answer=("too human for me",)
        )
        kwargs['body'] = "Go fuck yourself"
        self.assertNextMessage(
            channel.message_post(**kwargs),
            sender=self.awkhadbot,
            answer=("I have feelings",)
        )

    @mute_logger('awkhad.addons.mail.models.mail_mail')
    def test_awkhadbot_no_default_answer(self):
        kwargs = self.message_post_default_kwargs.copy()
        kwargs.update({'body': "I'm not talking to @awkhadbot right now", 'partner_ids': []})
        self.assertNextMessage(
            self.test_record_employe.message_post(**kwargs),
            answer=False
        )

    def assertNextMessage(self, message, answer=None, sender=None):
        last_message = self.env['mail.message'].search([('id', '=', message.id + 1)])
        if last_message:
            body = last_message.body.replace('<p>', '').replace('</p>', '')
        else:
            self.assertFalse(answer, "No last message found when an answer was expect")
        if answer is not None:
            if answer and not last_message:
                self.assertTrue(False, "No last message found")
            if isinstance(answer, list):
                self.assertIn(body, answer)
            elif isinstance(answer, tuple):
                for elem in answer:
                    self.assertIn(elem, body)
            elif not answer:
                self.assertFalse(last_message, "No answer should have been post")
                return
            else:
                self.assertEqual(body, answer)
        if sender:
            self.assertEqual(sender, last_message.author_id)
        return last_message
