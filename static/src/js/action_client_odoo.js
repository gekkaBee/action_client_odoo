odoo.define('action_client_odoo_module', function(require){
    'use strict';

    // First of all, import the things we need here.
    let core = require('web.core');
    var Widget = require('web.Widget');
    var FieldManagerMixin = require('web.FieldManagerMixin');
    let AbstractAction = require('web.AbstractAction');
    let basic_fields = require('web.basic_fields');
    let QWeb = core.qweb;
    let _t = core._t;
    let rpc = require("web.rpc");

    var action_client_odoo = AbstractAction.extend({
        title: core._t("New Dialog"),
        cssLibs: [
            //Include the css and scss files here
        ],
        jsLibs: [
            //Include other JS files and libraries here
        ],
        //This is where the widget is initialized
        init: function(parent, action, options) {
            this._super.apply(this, arguments);
            this.action = action;
            this.context = action.context;
            this.actionManager = parent;
            this.options = options || {};
        },
        events: {
            //Include events such as click, change, here
        },

        start: function () {
            this.get_html()
        },

        get_html: function() {
            var self = this;
            self.html = QWeb.render("CustomForm", {})
            self.footer = QWeb.render("FooterButtons", {})
            $(self.$el).ready(function(){
                $('.o_content').html(self.html);
            });
        },

    });

    //Add the custom defined abstract action to the registry
    core.action_registry.add('action_client_odoo', action_client_odoo)
    return action_client_odoo


})