/*  Copyright 2015-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html). */
awkhad.define('web_debranding.base', function(require) {
    var WebClient = require('web.WebClient');
    var core = require('web.core');

    var _t = core._t;

    WebClient.include({
        init: function(parent) {
            this._super.apply(this, arguments);
            var self = this;
            this.set('title_part', {"zopenerp": ''});
            awkhad.debranding_new_name = '';
            awkhad.debranding_new_website = '';
            awkhad.debranding_new_title = '';

            self._rpc({
                model: "ir.config_parameter",
                method: 'get_debranding_parameters',
            }, {
                shadow: true
            }).then(function(result){
                awkhad.debranding_new_name = result['web_debranding.new_name'];
                awkhad.debranding_new_website = result['web_debranding.new_website'];
                awkhad.debranding_new_title = result['web_debranding.new_title'];
                self.set('title_part', {"zopenerp": awkhad.debranding_new_title});

            });
        }
    });

});
