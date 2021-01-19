odoo.define('portal_proposal.proposal_tests', function (require) {
"use strict";


var FormView = require('web.FormView');
var testUtils = require('web.test_utils');
const { afterEach, beforeEach, start } = require('mail/static/src/utils/test_utils.js');

var createView = testUtils.createView;

QUnit.module('portal_proposal', {}, function () {
QUnit.module('static', {}, function () {
QUnit.module('tests', {}, function () {
QUnit.module('proposal_tests.js', {
	beforeEach() {
		beforeEach(this);
		this.data = {
            'portal.proposal': {
                fields: {},
                records: []
            }
        };
	},
	afterEach() {
        afterEach(this);
    },
});
QUnit.test('Proposal form', async function (assert) {
    assert.expect(2);
    assert.ok(1,1,'Qunit test executed!!!');
   
    var form = await createView({
        View: FormView,
        model: 'portal.proposal',
        data: this.data,
        arch:'<form>' +
                '<sheet>' +
                    '<group>' +
                        '<button type="button" class="btn btn-primary accept_data" id="acc_btn">Accept</button>' +
                        '<div id="success_div">' + 
                        	'<p><strong>The proposal has been accepted.</strong></p>' +
                        '</div>' +
                    '</group>' +
                '</sheet>' +
            '</form>',
        res_id: 1,
        mockRPC: function (route, args) {        	
        	if (args.model) {
        		assert.strictEqual(args.model, "portal.proposal", "Model should be proposal");
        		return Promise.resolve();
        	}
            return this._super.apply(this, arguments);
        },
    });	

    await testUtils.form.clickEdit(form);

    form.$('.accept_data').trigger('focus');
	form.$('.popover .accept_data').trigger('click');
	
	form.destroy();

    });
});
});
});

QUnit.testStart(prop_js_tests);
});