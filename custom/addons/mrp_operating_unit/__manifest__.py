# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# Copyright 2019 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Operating Unit in MRP",
    "version": "12.0.1.0.0",
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Serpent Consulting Services Pvt. Ltd.,"
              "Awkhad Community Association (ACA)",
    "website": "https://github.com/operating-unit",
    "license": "LGPL-3",
    "category": "Manufacturing",
    "depends": [
        "mrp",
        "stock_operating_unit",
        "sales_team"
    ],
    "data": [
        "security/mrp_security.xml",
        "views/mrp_view.xml"
    ],
    'installable': True,
}
