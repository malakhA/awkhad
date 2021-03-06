# Copyright 2018 Camptocamp SA
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP BoM Current Stock",
    "summary": "Add a report that explodes the bill of materials and show the "
               "stock available in the source location.",
    "version": "12.0.1.0.0",
    "category": "Manufacture",
    "website": "https://github.com/ACA/manufacture-reporting",
    "author": "Eficent, Awkhad Community Association (ACA)",
    "license": "AGPL-3",
    "depends": [
        "mrp_bom_location",
        "report_xlsx",
    ],
    "data": [
        "reports/report_mrpcurrentstock.xml",
        "wizard/bom_route_current_stock_view.xml",
    ],
}
