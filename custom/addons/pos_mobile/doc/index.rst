============
 POS Mobile
============

Installation
============

* `Install <https://awkhad-development.readthedocs.io/en/latest/awkhad/usage/install-module.html>`__ this module in a usual way


Fastclick issues
----------------

According to the library note: fastclick offers no benefit on newer browsers, and risks introducing bugs into your application

Possible error is:

[Violation] A non-passive event listener was added to a scroll lock event. Consider marking the event handler as 'passive' to make the page more responsive.

The following commit removes fastclick in Awkhad 12.0:
https://github.com/awkhad/awkhad/commit/d458ec953b179596330091b3efe729868fb56ca2

To apply the update on earlier awkhad version you can use git commands or use patch file ``remove_fastclick.patch``. The patch can be found at module source. Exact commands are as following:

If awkhad is a git folder: ::

 cd /path/to/awkhad/source
 git fetch
 git cherry-pick d458ec953b179596330091b3efe729868fb56ca2

If your installation does not have git: ::

 cd /path/to/awkhad/source
 patch -p1 < /path/to/remove_fastclick.patch


Usage
=====

With using mobile telephone:

* Open menu ``Point of Sale``
* Click ``New Session``
* RESULT: POS interface in mobile version
* Use ``/pos/web/?m=0`` to force default POS interface

Without using mobile telephone:

* Open menu ``Point of Sale``
* Click ``New Session``
* RESULT: POS interface with default version
* Use ``/pos/web/?m=1`` to force the mobile version


Adding POS icon to a phone homescreen
=====================================

* Chrome

  * Run Chrome for Android and open the POS web page
  * Tap the menu button and tap Add to homescreen
  * Specify a name for the shortcut
  * Tap the Ok button

* Firefox

  * Run Firefox for Android and open the POS web page
  * Tap the menu button
  * Tap the Page option
  * Tap Add to Home Screen

* Safari

  * Run the Safari browser on Apple’s iOS and open the POS web page
  * Tap the Share button on the browser’s toolbar
  * Tap the Add to Home Screen icon in the Share menu
