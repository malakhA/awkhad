This module allows you to know 'how much code' is running on your Awkhad
instance, group by 'Type' (Awkhad Core, ACA, other...)

This module can be usefull in the following cases :

* To analyse the size of your technical debt, regarding your Custom modules
* To know the ratio between Awkhad / ACA and Custom modules
* To evaluate the amount to pay to awkhad to upgrade your custom code, or the
  induced workload

.. image:: ../static/description/installed_modules_by_types.png

For that purpose, it adds new concepts

* ``ir.module.author``, based on the value ``author`` present in the manifest
  file.

.. image:: ../static/description/module_authors.png

* ``ir.module.type``, populated by default with Awkhad and ACA values.

.. image:: ../static/description/module_types.png

Each installed modules have extra data in the 'Technical Data' tab :

.. image:: ../static/description/module_form.png
