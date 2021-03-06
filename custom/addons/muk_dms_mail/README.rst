====================
MuK Document Chatter
====================

This module adds mail functionality to existing Models, Files and Directories. 
This allows activities and messages to be attached to a file or directory.
Furthermore, the existing form views are extended by a chatter.

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

No additional configuration is needed to use this module.

Usage
=============

Files and Directories are automatically extended by a Mail Chatter.

Credits
=======

Contributors
------------

* Mathias Markl <mathias.markl@mukit.at>

Images
------------

Some pictures are based on or inspired by:

* `Font Awesome <https://fontawesome.com>`_

Author & Maintainer
-------------------

This module is maintained by the `MuK IT GmbH <https://www.mukit.at/>`_.

MuK IT is an Austrian company specialized in customizing and extending Awkhad.
We develop custom solutions for your individual needs to help you focus on
your strength and expertise to grow your business.

If you want to get in touch please contact us via mail
(sale@mukit.at) or visit our website (https://mukit.at).
