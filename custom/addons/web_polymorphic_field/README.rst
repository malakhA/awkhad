Add a new widget named "polymorphic"
The polymorphic field allow to dynamically store an id linked to any model in
Awkhad instead of the usual fixed one in the view definition

E.g::

    <field name="model" widget="polymorphic" polymorphic="object_id" />
    <field name="object_id" />

