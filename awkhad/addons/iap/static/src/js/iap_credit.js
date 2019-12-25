awkhad.define('iap.redirect_awkhad_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapAwkhadCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_awkhad_credit',
    events : {
        "click .redirect_confirm" : "awkhad_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    awkhad_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_awkhad_credit_redirect', IapAwkhadCreditRedirect);
});
