odoo.define('portal_proposal.proposal_tests', function (require) {
"use strict";

var Widget = require('web.Widget');
const publicWidget = require('web.public.widget');
/*const testUtils = require('web.test_utils');*/
const tour = require('web_tour.tour');
var FormView = require('web.FormView');
var testUtils = require('web.test_utils');

var createView = testUtils.createView;

QUnit.module('Portal Proposal', {
	beforeEach: function () {
		this.data = {};
	},
}, function() {
	QUnit.module('Proposal');
        QUnit.test('Proposal form', function (assert) {
            assert.expect(0);
            var parent = new WIdget.publicWidget();
            parent.appendTo($('#qunit-fixture'));

            var $form = $(
                '<form>' +
                    '<input name="qty_accepted" type="text"/>' +
                    '<input name="price_accepted" type="text"/>' +                  
                '</form>');
            $('#qunit-fixture').append($form);
            let button = document.querySelector('button');
            testUtils.dom.click(button);
            console.log("TEST...");
            parent.unmount();
            parent.destroy();
        });
});
});