odoo.define('portal_proposal.ProposalPage', function (require) {
'use strict';

var Widget = require('web.Widget');
var core = require('web.core');
var _t = core._t;


var ProposalPage = Widget.extend({
    template: 'proposal_page_template',
    
    events: {        
        'click .accept_data': '_accept_data',       
    },

    init: function () {
        this._super.apply(this, arguments);
    },

    willStart: function () {
        var self = this;
        return this._super.apply(this, arguments);
    },

    _accept_data: function() {
    	console.log("JS CALLED...")
    	return this._rpc({
                model: 'portal.proposal',
                method: 'accept_qty_price',
                args: [],
            }).then(function (data) {
            	self.data = data;
            });
    }
});

});