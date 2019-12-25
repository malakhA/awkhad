# Copyright 2016-2017 Versada <https://versada.eu/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from awkhad.service import wsgi_server
from awkhad.tools import config as awkhad_config

from . import const
from .logutils import LoggerNameFilter, AwkhadSentryHandler

import collections

_logger = logging.getLogger(__name__)
HAS_RAVEN = True
try:
    import raven
    from raven.middleware import Sentry
except ImportError:
    HAS_RAVEN = False
    _logger.debug('Cannot import "raven". Please make sure it is installed.')


def get_awkhad_commit(awkhad_dir):
    '''Attempts to get Awkhad git commit from :param:`awkhad_dir`.'''
    if not awkhad_dir:
        return
    try:
        return raven.fetch_git_sha(awkhad_dir)
    except raven.exceptions.InvalidGitRepository:
        _logger.debug(
            'Awkhad directory: "%s" not a valid git repository', awkhad_dir)


def initialize_raven(config, client_cls=None):
    '''
    Setup an instance of :class:`raven.Client`.

    :param config: Sentry configuration
    :param client: class used to instantiate the raven client.
    '''
    enabled = config.get('sentry_enabled', False)
    if not (HAS_RAVEN and enabled):
        return

    if config.get('sentry_awkhad_dir') and config.get('sentry_release'):
        _logger.debug('Both sentry_awkhad_dir and sentry_release defined, choosing sentry_release')
    options = {
        'release': config.get('sentry_release', get_awkhad_commit(config.get('sentry_awkhad_dir'))),
    }
    for option in const.get_sentry_options():
        value = config.get('sentry_%s' % option.key, option.default)
        if isinstance(option.converter, collections.Callable):
            value = option.converter(value)
        options[option.key] = value

    level = config.get('sentry_logging_level', const.DEFAULT_LOG_LEVEL)
    exclude_loggers = const.split_multiple(
        config.get('sentry_exclude_loggers', const.DEFAULT_EXCLUDE_LOGGERS)
    )
    if level not in const.LOG_LEVEL_MAP:
        level = const.DEFAULT_LOG_LEVEL

    client_cls = client_cls or raven.Client
    client = client_cls(**options)
    handler = AwkhadSentryHandler(
        config.get('sentry_include_context', True),
        client=client,
        level=const.LOG_LEVEL_MAP[level],
    )
    if exclude_loggers:
        handler.addFilter(LoggerNameFilter(
            exclude_loggers, name='sentry.logger.filter'))
    raven.conf.setup_logging(handler)
    wsgi_server.application = Sentry(
        wsgi_server.application, client=client)

    client.captureMessage('Starting Awkhad Server')
    return client


sentry_client = initialize_raven(awkhad_config)
