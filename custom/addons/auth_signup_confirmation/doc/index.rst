===============================
 Email confirmation on sign up
===============================

Usage
=====

* `Install <https://awkhad-development.readthedocs.io/en/latest/awkhad/usage/install-module.html>`__ this module
* `Enable technical features <https://awkhad-development.readthedocs.io/en/latest/awkhad/usage/technical-features.html>`__
* Update Confirmation page if needed

  * Open ``Settings / Technical / Parameters / System Parameters``
  * Update value for record ``auth_signup_confirmation.url_singup_thankyou``

* Update Email template if needed

  * Open ``Settings / Technical / Email / Templates``
  * Update Template ``email for registration``

* Sign up

  * Open new Incognito window or simly log out
  * Navigate to ``/web`` page
  * Click ``Sing up`` link
  * Fill out the form
  * Click ``[Sing up]`` button

* Try to login without confirmation - you will get error "Wrong login\password"

* Check email and follow the link - now you can log in
