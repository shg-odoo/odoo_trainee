odoo.define('odoo_trainee.tree_view_dashbord', function(require) {
    "use strict";

    var core = require('web.core');
    var QWeb = core.qweb;
    var KanbanController = require("web.KanbanController");
    var ListController = require("web.ListController");

    var includeDict_proposal = {
        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.modelName === "sale.proposal") {
            	var proposal_dashboard = QWeb.render('odoo_trainee.ProposalDashboard');
            	console.log("proposal_dashboard :",proposal_dashboard)
                console.log(">>>>>>.yeahhh",this.modelName)
                console.log(this.$el)
                this.$el.prepend(proposal_dashboard);
            }
        }
    };

    KanbanController.include(includeDict_proposal);
    ListController.include(includeDict_proposal);
});