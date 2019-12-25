# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

import awkhad
import awkhad.exceptions

def login(db, login, password):
    res_users = awkhad.registry(db)['res.users']
    try:
        return res_users._login(db, login, password)
    except awkhad.exceptions.AccessDenied:
        return False

def check(db, uid, passwd):
    res_users = awkhad.registry(db)['res.users']
    return res_users.check(db, uid, passwd)

def compute_session_token(session, env):
    self = env['res.users'].browse(session.uid)
    return self._compute_session_token(session.sid)

def check_session(session, env):
    self = env['res.users'].browse(session.uid)
    expected = self._compute_session_token(session.sid)
    if expected and awkhad.tools.misc.consteq(expected, session.session_token):
        return True
    self._invalidate_session_cache()
    return False
