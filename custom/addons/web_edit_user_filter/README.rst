=================
Edit User Filters
=================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://awkhad-community.org/page/development-status
    :alt: Production/Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-ACA%2Fweb-lightgray.png?logo=github
    :target: https://github.com/ACA/web/tree/12.0/web_edit_user_filter
    :alt: ACA/web
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.awkhad-community.org/projects/web-12-0/web-12-0-web_edit_user_filter
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.awkhad-community.org/runbot/162/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

In standard Awkhad you can edit user filters via the debug module.
The problem is that normal users often don't have access to this menu therefore can't adjust filters once they're saved.
This module makes this feature available for normal users with a user friendly interface.
It also adds the ability to adjust facets (a single part of the filter).

**Table of contents**

.. contents::
   :local:

Usage
=====

Edit a favourite filter:

#. Go to a list or kanban view;
#. open the advanced search options;
#. open the 'Favorites' menu;
#. click on the pencil icon to start editing the filter.

Edit a facet:

#. Click on the facet;
#. a menu is now shown which allows you to remove values from the facet;
#. to cancel removal you can click outside the popover.

.. image:: https://raw.githubusercontent.com/web_edit_user_filter/static/description/edit_facet.png
   :alt: Edit Facet

Known issues / Roadmap
======================

* Make individual values in facets editable.
* Make saved filters easy overwritable.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ACA/web/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ACA/web/issues/new?body=module:%20web_edit_user_filter%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Onestein

Contributors
~~~~~~~~~~~~

* Dennis Sluijk <d.sluijk@onestein.nl>

Maintainers
~~~~~~~~~~~

This module is maintained by the ACA.

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

This module is part of the `ACA/web <https://github.com/ACA/web/tree/12.0/web_edit_user_filter>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://awkhad-community.org/page/Contribute.
