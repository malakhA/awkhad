# Copyright 2015 Ainara Galdona - AvanzOSC
# Copyright 2017 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Production Lot Multi Company",
    "summary": "Make serial numbers multi-company aware",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": 'https://github.com/ACA/multi-company',
    "license": "AGPL-3",
    "author": "AwkhadMRP team, "
              "AvanzOSC, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Awkhad Community Association (ACA)",
    "installable": True,
    "depends": [
        "stock",
    ],
    "data": [
        "security/stock_production_lot_security.xml",
        "views/stock_production_lot_view.xml",
    ],
}
