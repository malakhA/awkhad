# Copyright 2019 Tecnativa - Pedro M. Baeza
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Free Text Answers on Events Questions",
    "version": "12.0.1.0.0",
    "category": "Website",
    "website": "https://github.com/ACA/event",
    "author": "Tecnativa, "
              "Awkhad Community Association (ACA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "website_event_questions",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/event_event_views.xml",
        "views/event_templates.xml",
    ],
}
