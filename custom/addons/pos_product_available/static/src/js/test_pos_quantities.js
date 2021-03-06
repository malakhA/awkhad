/*  Copyright 2018-2019 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html). */
awkhad.define('pos_product_available.tour', function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var core = require('web.core');
    var _t = core._t;

    function open_pos_neworder() {
        return [{
            trigger: ".o_pos_kanban button.oe_kanban_action_button",
            content: _t("<p>Click to start the point of sale interface. It <b>runs on tablets</b>, laptops, or industrial hardware.</p><p>Once the session launched, the system continues to run without an internet connection.</p>"),
            position: "bottom"
        }, {
            content: "Switch to table or make dummy action",
            trigger: '.table, .order-button.selected',
            position: "bottom",
            timeout: 30000,
        }, {
            content: 'waiting for loading to finish',
            trigger: '.order-button.neworder-button',
        }];
    }

    function add_product_to_order(product_name) {
        return [{
            content: 'buy ' + product_name,
            trigger: '.product-list .product-name:contains("' + product_name + '")',
        }, {
            content: 'the ' + product_name + ' have been added to the order',
            trigger: '.orderline:contains("' + product_name + '")',
            run: function () {
                // it's a check
            },
        }];
    }

    function payment(pay_method) {
        return [{
            trigger: '.button.pay',
            content: _t("Open the payment screen"),
        }, {
            content: "Choose Administrator like a cashier or make a dummy action",
            trigger: '.modal-dialog.cashier:not(.oe_hidden) .cashier .selection-item:contains("Mitchell Admin"), .payment-screen:not(.oe_hidden) h1:contains("Payment")',
        }, {
            trigger: '.button.paymentmethod:contains("' + pay_method +'")',
            content: _t("Click the payment method"),
        }, {
            trigger: '.payment-screen .input-button.number-char:contains("2")',
            content: 'Set payment amount',
        }, {
            trigger: '.button.next.highlight:contains("Validate")',
            content: 'Validate payment',
        }, {
            extra_trigger: '.pos-sale-ticket',
            trigger: '.button.next.highlight:contains("Next Order")',
            content: 'Check proceeded validation',
        }];
    }

    function close_pos() {
        return [{
            trigger: '.header-button:contains("Close")',
            content: _t("Close POS"),
        }, {
            trigger: '.header-button.confirm:contains("Confirm")',
            content: _t("Close POS"),
        }, {
            extra_trigger: ".o_pos_kanban button.oe_kanban_action_button",
            trigger: '.breadcrumb li.active',
            content: _t("<p>Click to start the point of sale interface. It <b>runs on tablets</b>, laptops, or industrial hardware.</p><p>Once the session launched, the system continues to run without an internet connection.</p>"),
            position: "bottom",
        }];
    }

    function check_quantity(qty) {
        return [{
            content: 'check quantity',
            extra_trigger: '.product-list .product:contains("LED Lamp") .qty-tag:contains(' + String(qty) + '):not(.not-available)',
            trigger: '.order-button.selected',
        }];
    }

    var steps = [tour.STEPS.SHOW_APPS_MENU_ITEM, {
        trigger: '.o_app[data-menu-xmlid="point_of_sale.menu_point_root"]',
        content: _t("Ready to launch your <b>point of sale</b>? <i>Click here</i>."),
        position: 'right',
        edition: 'community'
    }, {
        trigger: '.o_app[data-menu-xmlid="point_of_sale.menu_point_root"]',
        content: _t("Ready to launch your <b>point of sale</b>? <i>Click here</i>."),
        position: 'bottom',
        edition: 'enterprise'
    }];
    steps = steps.concat(
        open_pos_neworder(),
        add_product_to_order('LED Lamp'),
        payment('Cash (USD)'),
        close_pos(),
        open_pos_neworder(),
        check_quantity(2)
    );

    tour.register('tour_pos_product_available', { test: true, url: '/web' }, steps);

});
