odoo.define('sale_proposal.sale_proposal_portal', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');
    var PortalSidebar = require('portal.PortalSidebar');

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

odoo.define('sale_proposal.sale_proposal_accept', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');
    var Portalaccept = require('portal.PortalSidebar');
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');

    publicWidget.registry.sale_proposal_accept = Portalaccept.extend({
        selector: '.portal_accept_reject',
        events: {
            'click .accept_btn': '_onClick_accept_btn',
            'click .reject_btn': '_onClick_reject_btn',
        },
        _onClick_accept_btn: function () {
            var qty_accept = document.getElementById('input')
            console.log(qty_accept);
            console.log('qty_accept');
            var access_token = new URLSearchParams(window.location.search).get('access_token');

            var price_accept = document.getElementsByClassName('accept_price')
            document.write(price_accept);
            ajax.jsonRpc('/proposal/accepted/', 'call', {
                'data': qty_accept,
                'access_token': access_token
            }).then(function (url) {
            })
        },


    });


});
