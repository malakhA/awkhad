==============================
 Store sessions in postgresql
==============================

Installation
============

To use module, add it to ``--load`` parameter. E.g. ::

     ./awkhad.py --load=web,web_kanban,base_session_store_psql

In current implementation, you don't need to install module via awkhad interface.

It's recommended to `patch <https://github.com/it-projects-llc/install-awkhad/blob/11.0/install-awkhad-saas.sh#L392-L405>`_ awkhad to exclude database from loading list, otherwise it's treated as normal awkhad database (with base module installed, cron is running, etc.)

Configuration
=============

You can use ``session_store_db`` parameter in config file (default value is ``session_store``) to specify database where sessions are stored. 


Uninstallation
==============

To uninstall the module delete it from ``--load`` parameter.
