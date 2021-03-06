

from awkhad import http
from awkhad.addons.web.controllers.main import Home
from awkhad.http import request
from awkhad.addons.auth_signup.controllers.main import AuthSignupHome


class Background(Home):

    @http.route('/web/login', type='http', auth="public")
    def web_login(self, redirect=None, **kw):
        picture_url = request.env['ir.attachment'].get_background_pic()
        if picture_url:
            request.params['picture_url'] = picture_url

        return super(Background, self).web_login(redirect=redirect, **kw)


class BackgroundSignup(AuthSignupHome):

    @http.route('/web/signup', type='http', auth="public")
    def web_auth_signup(self, *args, **kw):
        picture_url = request.env['ir.attachment'].get_background_pic()
        if picture_url:
            request.params['picture_url'] = picture_url

        return super(BackgroundSignup, self).web_auth_signup(*args, **kw)
