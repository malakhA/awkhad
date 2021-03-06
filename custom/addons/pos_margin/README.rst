================
PoS Order Margin
================

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
.. |badge3| image:: https://img.shields.io/badge/github-ACA%2Fpos-lightgray.png?logo=github
    :target: https://github.com/ACA/pos/tree/12.0/pos_margin
    :alt: ACA/pos
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.awkhad-community.org/projects/pos-12-0/pos-12-0-pos_margin
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.awkhad-community.org/runbot/184/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module extends the functionality of point of sale to support margin on
pos orders.

This gives the profitability by calculating the difference between the Unit
Price and Cost Price.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

* Go to 'Point Of Sale' / 'Orders' / 'Orders'
* Open an order

.. figure:: https://raw.githubusercontent.com/ACA/pos/12.0/pos_margin/static/description/pos_order_form.png
   :width: 800px

Known issues / Roadmap
======================

This module depends on ``sale_margin`` module to reuse algorithm present in the
function ``_get_purchase_price`` of the model ``sale.order.line`` to
compute correctly purchase price, in a multicurrency context.

This dependency can be removed, when Awkhad Core will be correctly refactored,
moving this ``@api.model`` function in a more generic module (``account``
for exemple).

Changelog
=========

12.0.1.0.0
~~~~~~~~~~

* Migrate to V12.0
* Reuse ``sale_margin`` computation to handle multi currency context.
* Correct computation of margin, if a module that adds ``uom_id`` on
  ``pos.order.line`` is installed.
* Add test

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ACA/pos/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ACA/pos/issues/new?body=module:%20pos_margin%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* GRAP

Contributors
~~~~~~~~~~~~

* Sylvain LE GAL (https://twitter.com/legalsylvain)
* Wolfgang Pichler

Maintainers
~~~~~~~~~~~

This module is maintained by the ACA.

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

This module is part of the `ACA/pos <https://github.com/ACA/pos/tree/12.0/pos_margin>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://awkhad-community.org/page/Contribute.
