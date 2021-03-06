=======================
Github Connector - Awkhad
=======================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://awkhad-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-ACA%2Finterface--github-lightgray.png?logo=github
    :target: https://github.com/ACA/interface-github/tree/12.0/github_connector_awkhad
    :alt: ACA/interface-github
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.awkhad-community.org/projects/interface-github-12-0/interface-github-12-0-github_connector_awkhad
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.awkhad-community.org/runbot/229/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module was written to extend the functionality of 'Github Connector'
Module if your repositories contain Awkhad Modules.

It extends 'Analysis' features to parse code files (readme / manifest files)
and add new models and menus.

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/menu.png

**Table of contents**

.. contents::
   :local:

Configuration
=============

* Once installed, go to your organization, and set extra settings:

1. The name of your organization in the author keys of the manifest awkhad
   modules
2. The URL of the file that contains IDs of your repositories for the runbot

.. image:: https://raw.githubusercontent.com/ACA/interface-github/12.0/github_connector_awkhad/static/description/github_organization_form.png

If you had analyzed previously your repositories with the
'github Connector' module, you should launch again the Analysis Process
for all your Repository Branches.

Usage
=====

**Awkhad Modules**

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_module_kanban.png

In each module, you can see the description of the module, the authors,
the available series, and the list of the modules that depend on the
current module.

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_module_form.png



**Awkhad Authors**

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_author.png

This list is based on the 'author' key of the manifest file.



**Awkhad License**

This list is based on the 'license' key of the manifest file.

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_license.png



**Awkhad Bin Libs**

This list is based on the 'external_dependencies' / 'bin' key of the
manifest file.

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_bin_libs.png



**Awkhad Python Libs**

This list is based on the 'external_dependencies' / 'python' key of the
manifest file.

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/awkhad_python_libs.png



**Reporting**

This module provide a new reporting.

**Modules by Serie (and Licenses)**

.. image:: https://raw.githubusercontent.com/github_connector_awkhad/static/description/reporting_module_by_serie.png

Known issues / Roadmap
======================

Possible improvements :

* Implement deep code source analysis, like the website http://awkhad-code-search.com/
  and specially:

1. Possibility to search by field or by model name. (Ex: field:invoice_id)
2. Possibility to display the number of XML, Python, Yaml, HTML, CSS lines

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ACA/interface-github/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ACA/interface-github/issues/new?body=module:%20github_connector_awkhad%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Sylvain LE GAL
* GRAP

Contributors
~~~~~~~~~~~~

* Sylvain LE GAL (https://twitter.com/legalsylvain)
* `Tecnativa <https://www.tecnativa.com>`_:

  * Vicent Cubells

Maintainers
~~~~~~~~~~~

This module is maintained by the ACA.

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

This module is part of the `ACA/interface-github <https://github.com/ACA/interface-github/tree/12.0/github_connector_awkhad>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://awkhad-community.org/page/Contribute.
