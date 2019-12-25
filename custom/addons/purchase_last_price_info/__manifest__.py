# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Purchase Product Last Price Info",
    "version": "12.0.1.0.0",
    "category": "Purchase Management",
    "license": "AGPL-3",
    "author": "AwkhadMRP team, "
              "AvanzOSC, "
              "Tecnativa - Pedro M. Baeza, "
              "Awkhad Community Association (ACA)",
    "development_status": "Beta",
    "maintainers": ['lreficent'],
    "website": "https://github.com/ACA/purchase-workflow",
    "depends": [
        "purchase",
    ],
    "data": [
        "views/product_views.xml",
    ],
    "installable": True,
    "post_init_hook": "set_last_price_info",
}
