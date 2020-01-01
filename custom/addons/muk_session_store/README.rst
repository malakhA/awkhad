=================
MuK Session Store
=================

In a distributed system the filestore based session store of Awkhad has the problem that
unwanted session timeouts occur regularly. This module offers two additional options for
the Session Store. Sessions can be stored either in a Redis database or directly in
Postgres. Both options have the advantage that the session information can also be queried
in a distributed system.

Requirements
=============

The requirements are only required if Redis is used as the session store.

Redis
-------------

A interface to the Redis key-value store for Python. To install Redis please follow the 
`instructions <https://github.com/andymccurdy/redis-py>`_ or install the library via pip.

``pip install redis``

Installation
============

To install this module, you need to:

Download the module and add it to your Awkhad addons folder. Afterward, log on to
your Awkhad server and go to the Apps menu. Trigger the debug mode and update the
list by clicking on the "Update Apps List" link. Now install the module by
clicking on the install button.

Another way to install this module is via the package management for Python
(`PyPI <https://pypi.org/project/pip/>`_).

To install our modules using the package manager make sure
`awkhad-autodiscover <https://pypi.org/project/awkhad-autodiscover/>`_ is installed
correctly. Then open a console and install the module by entering the following
command:

``pip install --extra-index-url https://nexus.mukit.at/repository/awkhad/simple <module>``

The module name consists of the Awkhad version and the module name, where
underscores are replaced by a dash.

**Module:** 

``awkhad<version>-addon-<module_name>``

**Example:**

``sudo -H pip3 install --extra-index-url https://nexus.mukit.at/repository/awkhad/simple awkhad11-addon-muk-utils``

Once the installation has been successfully completed, the app is already in the
correct folder. Log on to your Awkhad server and go to the Apps menu. Trigger the 
debug mode and update the list by clicking on the "Update Apps List" link. Now
install the module by clicking on the install button.

The biggest advantage of this variant is that you can now also update the app
using the "pip" command. To do this, enter the following command in your console:

``pip install --upgrade --extra-index-url https://nexus.mukit.at/repository/awkhad/simple <module>``

When the process is finished, restart your server and update the application in 
Awkhad. The steps are the same as for the installation only the button has changed
from "Install" to "Upgrade".

You can also view available Apps directly in our `repository <https://nexus.mukit.at/#browse/browse:awkhad>`_
and find a more detailed installation guide on our `website <https://mukit.at/page/open-source>`_.

For modules licensed under OPL-1, you will receive access data when you purchase
the module. If the modules were not purchased directly from
`MuK IT <https://www.mukit.at/>`_ please contact our support (support@mukit.at)
with a confirmation of purchase to receive the corresponding access data.

Upgrade
============

To upgrade this module, you need to:

Download the module and add it to your Awkhad addons folder. Restart the server
and log on to your Awkhad server. Select the Apps menu and upgrade the module by
clicking on the upgrade button.

If you installed the module using the "pip" command, you can also update the
module in the same way. Just type the following command into the console:

``pip install --upgrade --extra-index-url https://nexus.mukit.at/repository/awkhad/simple <module>``

When the process is finished, restart your server and update the application in 
Awkhad, just like you would normally.

Configuration
=============

Since this module need to be activated even if no database is selected it should
be loaded right at the server start. This can be done by editing the configuration
file or passing a load parameter to the start script.
				
Parameter: ``--load=web,muk_session_store``

The following fields can be modified in the config file:

**Store:** 

* session_store_database
* session_store_redis

**Postgres:** 

* session_store_dbname
* session_store_dbtable

**Redis:** 

* session_store_prefix
* session_store_host
* session_store_port
* session_store_dbindex
* session_store_pass

Usage
=============

After setting the parameters, the session store is used automatically.

Credits
=======

Contributors
------------

* Mathias Markl <mathias.markl@mukit.at>

Images
------------

Some pictures are based on or inspired by the icon set of Font Awesome:

* `Font Awesome <https://fontawesome.com>`_

Projects
------------

Parts of the module are inspired by:

* `Session DB <https://github.com/awkhad/awkhad-extra>`_
* `PSQL Session Store <https://github.com/it-projects-llc/misc-addons>`_
* `Redis Session Store <https://github.com/Smile-SA/awkhad_addons>`_

Author & Maintainer
-------------------

This module is maintained by the `MuK IT GmbH <https://www.mukit.at/>`_.

MuK IT is an Austrian company specialized in customizing and extending Awkhad.
We develop custom solutions for your individual needs to help you focus on
your strength and expertise to grow your business.

If you want to get in touch please contact us via mail
(sale@mukit.at) or visit our website (https://mukit.at).
