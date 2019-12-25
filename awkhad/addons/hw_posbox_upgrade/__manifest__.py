# -*- coding: utf-8 -*-
# Part of Awkhad. See LICENSE file for full copyright and licensing details.

{
    'name': 'IoTBox Software Upgrader',
    'category': 'Point of Sale',
    'website': 'https://www.awkhad.com/page/point-of-sale-hardware',
    'sequence': 6,
    'summary': 'Allows to remotely upgrade the IoTBox software',
    'description': """
IoTBox Software Upgrader
========================

This module allows to remotely upgrade the IoTBox software to a
new version. This module is specific to the IoTBox setup and environment
and should not be installed on regular Awkhad servers.

""",
    'depends': ['hw_proxy'],
    'installable':  False,
}
