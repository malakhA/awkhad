import logging

import awkhad
from awkhad.tools.func import lazy_property

from .sessionstore import PostgresSessionStore

_logger = logging.getLogger(__name__)


class RootTkobr(awkhad.http.Root):

    @lazy_property
    def session_store(self):
        # Setup http sessions
        _logger.debug('HTTP sessions stored in Postgres')
        return PostgresSessionStore(session_class=awkhad.http.ZgUISession)


root = RootTkobr()
awkhad.http.root.session_store = root.session_store
