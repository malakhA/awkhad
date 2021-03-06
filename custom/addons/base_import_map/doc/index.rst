=================
 Import Settings
=================

Installation
============

* `Install <https://awkhad-development.readthedocs.io/en/latest/awkhad/usage/install-module.html>`__ this module in a usual way

Usage
=====

Open built-in import tool. Then

* Load File
* click *+ Options...*
* To save settings:

  * Specify Settings name in *Save settings* field
  * Specify *File read hook* if needed (see below for explanation)
  * Specify Columns Map manually
  * Click ``[Import]``

* To use existed settings:

  * choose settings you want to use in *Settings:* field
  * Click ``[Import]``

To manage existed settings do as follows:

* `Enable technical features <https://awkhad-development.readthedocs.io/en/latest/awkhad/usage/technical-features.html>`__
* Open menu ``Settings >> Technical >> Import Settings``

File read hook
--------------

This field allows to update data on importing. Use variable ``row`` to update values in a row. For example::

    row[0] = 'prefix_' + row[0]

-- adds prefix to the first column.
