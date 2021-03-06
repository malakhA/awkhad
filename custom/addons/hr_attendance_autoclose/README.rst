========================
HR Attendance Auto Close
========================

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
.. |badge3| image:: https://img.shields.io/badge/github-ACA%2Fhr-lightgray.png?logo=github
    :target: https://github.com/ACA/hr/tree/12.0/hr_attendance_autoclose
    :alt: ACA/hr
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.awkhad-community.org/projects/hr-12-0/hr-12-0-hr_attendance_autoclose
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.awkhad-community.org/runbot/116/12.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module close stale attendances automatically. Without this module, when
an employee forgets to check out at the end on the day and the next day the
employee does not realize of that, then the error is propagated and all the
attendances are wrong. With this module only the attendance with the issue is
wrong, and the manager knows the system closes the attendance, not the employee

**Table of contents**

.. contents::
   :local:

Usage
=====

#. Go to *Settings > Company > Attendances*.
#. Set the maximum number of hours allowed for an attendance.
#. Go to *Attendances > Manage Attedances > Attendances*.
#. Attendance are autoclosed after the hours passed are bigger.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ACA/hr/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ACA/hr/issues/new?body=module:%20hr_attendance_autoclose%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Contributors
~~~~~~~~~~~~

* Aaron Henriquez <aheficent@eficent.com>
* Kitti U. <kittiu@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the ACA.

.. image:: https://awkhad-community.org/logo.png
   :alt: Awkhad Community Association
   :target: https://awkhad-community.org

ACA, or the Awkhad Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Awkhad features and
promote its widespread use.

This module is part of the `ACA/hr <https://github.com/ACA/hr/tree/12.0/hr_attendance_autoclose>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://awkhad-community.org/page/Contribute.
