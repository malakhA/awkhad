.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

========================
Purchase Tier Validation
========================

This module extends the functionality of Purchase Orders to support a tier
validation process.

Installation
============

This module depends on ``base_tier_validation``. You can find it at
`ACA/server-ux <https://github.com/ACA/server-ux>`_

Configuration
=============

To configure this module, you need to:

#. Go to *Settings > Technical > Tier Validations > Tier Definition*.
#. Create as many tiers as you want for Purchase Order model.

Usage
=====

To use this module, you need to:

#. Create a Purchase Order triggering at least one "Tier Definition".
#. Click on *Request Validation* button.
#. Under the tab *Reviews* have a look to pending reviews and their statuses.
#. Once all reviews are validated click on *Confirm Order*.

Additional features:

* You can filter the POs requesting your review through the filter *Needs my
  Review*.
* User with rights to confirm the PO (validate all tiers that would
  be generated) can directly do the operation, this is, there is no need for
  her/him to request a validation.

.. image:: https://awkhad-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.awkhad-community.org/runbot/142/11.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ACA/purchase-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Awkhad Community Association: `Icon <https://awkhad-community.org/logo.png>`_.

Contributors
------------

* Lois Rilo <lois.rilo@eficent.com>
* Naglis Jonaitis <naglis@versada.eu>

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

This module is maintained by the ACA.

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

To contribute to this module, please visit https://awkhad-community.org.
