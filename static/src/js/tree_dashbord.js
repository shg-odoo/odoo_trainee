odoo.define('odoo_trainee.tree_view_dashbord', function(require) {
    "use strict";

    var core = require('web.core');
    var QWeb = core.qweb;
    var ListRenderer = require("web.ListRenderer");

    const includeDict_proposal = {
        _render: async function () {
            this._super.apply(this, arguments);
            if (this.state.model === "sale.proposal") {
            	await this._super(...arguments);
	            const result = await this._rpc({
	                model: 'sale.proposal',
	                method: 'get_record_counter',
	                context: self.context,
	            });
	            const elem = QWeb.render('odoo_trainee.ProposalDashboard', {
	                value: result,
	            });
	            this.$el.find('.table-responsive').prepend(elem);
            }
        }
    };
    ListRenderer.include(includeDict_proposal);
});