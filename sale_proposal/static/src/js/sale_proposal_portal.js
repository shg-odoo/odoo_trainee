odoo.define('sale_proposal.sale_proposal_portal', function (require) {
    'use strict';
    const minusButton = document.getElementById('minus');
    const plusButton = document.getElementById('plus');
    const inputField = document.getElementById('input');

    minusButton.addEventListener('click', event => {
        event.preventDefault();
        const currentValue = Number(inputField.value) || 0;
        inputField.value = currentValue - 1;
    });
    plusButton.addEventListener('click', event => {
        event.preventDefault();
        const currentValue = Number(inputField.value) || 0;
        inputField.value = currentValue + 1;
    });
});

odoo.define('sale_proposal.SaleProposalAcceptReject', function (require) {
    "use strict";

    var SaleProposalAcceptReject = require('web.public.widget');
    var ProposalPortal = require('portal.PortalSidebar');
    var ajax = require('web.ajax');

    SaleProposalAcceptReject.registry.SaleProposalAcceptReject = ProposalPortal.extend({
        selector: '.portal_accept_reject',
        events: {
            'click .accept_button': 'clicking_accept_btn',
            'click .reject_button': 'clicking_RejectBtn'

        },
        clicking_accept_btn: function () {
            const qty_accpt = document.getElementsByClassName('accept_qty')
            const price_accpt = document.getElementsByClassName('accept_price')
            let quantity
            let price
            let record_id
            let proposal_line_id
            const proposal_id = document.getElementsByClassName('proposal_id')
            const dict = [];
            const access_token = new URLSearchParams(window.location.search).get('access_token');

            for (var i = 0; i < qty_accpt.length; i++) {
                var qty_linebyline = qty_accpt[i];
                var price_linebyline = price_accpt[i]
                quantity = qty_linebyline.value
                price = price_linebyline.value
                record_id = proposal_id[0].value
                proposal_line_id = qty_linebyline.getAttribute('line_id')
                dict.push({
                    'qty_accepted': quantity,
                    'price_accepted': price,
                    'proposal_id': record_id,
                    'amount_total_accpt': quantity * price,
                    'line_id': proposal_line_id,
                });
            }
            ajax.jsonRpc('/proposal/accepted/', 'call', {
                'data': dict, 'access_token': access_token
            },
            location.reload())
            alert("Your Proposal Have Been Accepted!");
            location.reload();

        },
        clicking_RejectBtn: function () {
            const proposal_id = document.getElementsByClassName('proposal_id')[0].value

            ajax.jsonRpc('/proposal/rejected/', 'call', { 'proposal_id':proposal_id

            })
            alert("Your Proposal Have Been Rejected!");
        }
    })
});


