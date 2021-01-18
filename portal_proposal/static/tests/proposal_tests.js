odoo.define('portal_proposal.proposal_tests', function (require) {
"use strict";

/*var Widget = require('web.Widget');*/
var publicWidget = require('web.public.widget');
/*const testUtils = require('web.test_utils');*/
const tour = require('web_tour.tour');
var FormView = require('web.FormView');
var testUtils = require('web.test_utils');

var createView = testUtils.createView;

/*QUnit.module('proposal_tests.js', {
	beforeEach: function () {
		this.data = {};
	},
},*/
 /*function prop_js_tests() {*/
QUnit.module('portal_proposal', {}, function () {
QUnit.module('static', {}, function () {
QUnit.module('tests', {}, function () {
QUnit.module('proposal_tests.js', {
	beforeEach() {
		beforeEach(this);
	},
});
QUnit.test('Proposal form', function (assert) {
    assert.expect(1);
    assert.ok(1,1,'Qunit test executed!!!');
    var parent = new publicWidget();
    parent.appendTo($('#qunit-fixture'));

    var $form = $(
        '<form>' +
            '<input name="qty_accepted" type="text"/>' +
            '<input name="price_accepted" type="text"/>' +                  
        '</form>');
    $('#qunit-fixture').append($form);

    assert.strictEqual(form.$('div .success_div').text(), 'The proposal has been accepted.', "The proposal has been accepted.");

    let button = document.querySelector('button');
    testUtils.dom.click(button);
    /*console.log("TEST...");*/
    form.$('.accept_data').trigger('focus');
	form.$('.popover .accept_data').trigger('click');

    parent.unmount();
    parent.destroy();
    });
});
});
});
/*};*//*
)*/
QUnit.testStart(prop_js_tests);
});