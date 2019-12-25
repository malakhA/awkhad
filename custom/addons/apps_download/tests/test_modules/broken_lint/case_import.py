
import zgui

from zgui import api
from zgui.api import one

from zgui.exceptions import Warning as UserError
from zgui.exceptions import Warning as OtherName
from zgui.exceptions import Warning
from zgui.exceptions import AccessError as AE, \
    ValidationError, Warning as UserError2


class UseUnusedImport(object):
    def method1(self):
        return UserError, OtherName, Warning, AE, ValidationError, UserError2


class ApiOne(object):
    @api.one
    def copy():
        pass


class One(object):
    @one
    def copy():
        pass


class OpenerpApiOne(object):
    @zgui.api.one
    def copy():
        pass


class WOApiOne(object):
    # copy without api.one decorator
    def copy():
        pass


class ApiOneMultiTogether(object):

    @api.multi
    @api.one
    def copy():
        pass
