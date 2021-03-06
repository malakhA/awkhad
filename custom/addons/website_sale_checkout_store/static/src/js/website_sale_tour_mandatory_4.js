/* Copyright 2017 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
   Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
   License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html). */
awkhad.define('website_sale_checkout_store.tour.4', function (require) {
'use strict';

var tour = require("web_tour.tour");
var base = require("web_editor.base");

tour.register('shop_mandatory_fields_nobill_ship', {
    test: true,
    url: '/shop',
    wait_for: base.ready()
},
    [
        // for unsigned user
        {
            content: 'search customizable desk',
            trigger: 'form input[name="search"]',
            run: 'text customizable desk'
        },
        {
            content: 'search customizable desk',
            trigger: 'form:has(input[name="search"]) .oe_search_button',
        },
        {
            content: 'select desk customizable',
            extra_trigger: '.oe_product_cart a:contains("Customizable Desk")',
            trigger: '.oe_product_cart a:contains("Customizable Desk")',
        },
        {
            content: "click on add to cart",
            trigger: '#add_to_cart',
        },
        {
            content: "click on proceed to checkout",
            trigger: '.btn-primary span:contains("Proceed to Checkout")',
        },
        //--------------------------DEFAULT PART ENDS--------------------------------------
        {
            content: "select payment",
            trigger: 'a[id="nobill_ship"]',
        },
        {
            content: "filling in name",
            trigger: '.div_name input[name="name"]',
            run: "text name",
        },
        {
            content: "filling in email",
            trigger: '#div_email input[name="email"]',
            run: "text email@email.mn",
        },
        {
            content: "filling in phone",
            trigger: '#div_phone input[name="phone"]',
            run: "text 1234567890",
        },
        {
            content: "filling in street",
            trigger: '.div_street input[name="street"]',
            run: "text Street and Number",
        },
        {
            content: "filling in city",
            trigger: '.div_city input[name="city"]',
            run: "text city",
        },
        {
            content: "Confirm checkout",
            trigger: 'a:contains("Next")',
        },
        {
            content: "Confirm payment method",
            trigger: "td:contains('Pay on delivery')",
        },
    ]
);

});
