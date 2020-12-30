odoo.define('prop.tour', function(require) {
"use strict";

var core = require('web.core');
var tour = require('web_tour.tour');

var _t = core._t;

 tour.register("sale_proposal_tour", {
        url: "/web#action=portal_sales_proposal.portal_sales_proposal_action",
    }, [{
        trigger: '.o_list_button_add',
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("<p>Create your first<b> Sales Proposal</b>.</p>"),
        position: "bottom",
    },{
        trigger: ".o_form_editable .o_field_many2one[name='partner_id']",
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("Write a customer name to create one, or see suggestions."),
        position: "bottom",
    }, {
        trigger: ".o_field_x2many_list_row_add > a",
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("Click here to add some products or services to your quotation."),
        position: "bottom",
    }, {
        trigger: ".o_field_widget[name='product_id'], .o_field_widget[name='product_template_id']",
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("Select a product, or create a new one on the fly."),
        position: "right",
        run: function (actions) {
            var $input = this.$anchor.find("input");
            actions.text("DESK0001", $input.length === 0 ? this.$anchor : $input);
            // fake keydown to trigger search
            var keyDownEvent = jQuery.Event("keydown");
            keyDownEvent.which = 42;
            this.$anchor.trigger(keyDownEvent);
            var $descriptionElement = $(".o_form_editable textarea[name='name']");
            // when description changes, we know the product has been created
            $descriptionElement.change(function () {
                $descriptionElement.addClass("product_creation_success");
            });
        },
        id: "product_selection_step"
        },{
        trigger: '.o_form_button_save',
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("<p>Once your proposal is ready, you can <b>save</b> it.</p>"),
        position: 'bottom',
        },{
        trigger: "button[name='action_send_mail']",
        extra_trigger: '.o_portal_sales_proposal',
        content: _t("<p>Now you can click here to<b> Send Proposal </b>Mail</p>"),
        position: 'bottom',
    }]);
 });
