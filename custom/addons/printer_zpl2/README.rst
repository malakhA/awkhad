.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
ZPL II Label printing
=====================

This module extends the **Report to printer** (``base_report_to_printer``)
module to add a ZPL II label printing feature.

This module is meant to be used as a base for module development, and does not provide a GUI on its own.
See below for more details.

Installation
============

Nothing special, just install the module.

Configuration
=============

To configure this module, you need to:

#. Go to *Settings > Printing > Labels > ZPL II*
#. Create new labels
#. Import ZPL2 code
#. Use the Test Mode tab during the creation

It's also possible to add a label printing wizard on any model by creating a new *ir.actions.act_window* record.
For example, to add the printing wizard on the *product.product* model ::

    <act_window id="action_wizard_purchase"
      name="Print Label"
      src_model="product.product"
      res_model="wizard.print.record.label"
      view_mode="form"
      target="new"
      key2="client_action_multi"/>

Usage
=====

To print a label, you need to call use the label printing method from anywhere (other modules, server actions, etc.).

Example : Print the label of a product ::

    self.env['printing.label.zpl2'].browse(label_id).print_label(
        self.env['printing.printer'].browse(printer_id),
        self.env['product.product'].browse(product_id))

You can also use the generic label printing wizard, if added on some models.

.. image:: https://awkhad-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.awkhad-community.org/runbot/144/12.0

Known issues / Roadmap
======================

* Develop a "Designer" view in a separate module, to allow drawing labels with simple mouse clicks/drags

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ACA/report-print-send/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Awkhad Community Association: `Icon <https://github.com/ACA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Sylvain Garancher <sylvain.garancher@syleam.fr>
* Florent de Labarre
* Jos De Graeve <Jos.DeGraeve@apertoso.be>

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
