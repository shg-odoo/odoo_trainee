$(document).ready(function() {
    $(".sale_tbody input").on('keyup', function() {
        var $mult = 0;
        $('tr.prdct_line').each(function() {
            var $val1 = $('.qty_accepted1', this).val();
            var $val2 = $('.price_accepted1', this).val();
            var $total = ($val1 * 1) * ($val2 * 1)
            $mult += $total;
        });
        $("span[data-id='total_amount_2'] .oe_currency_value").text($mult);
    });

    $(".send_data_btn").click(function() {
        lines_data = {};
        ind = 0
        tmp = [];
        flag = 0;
        $('.sale_tbody input').each(function(index, value) {
            if (ind == 1) {
                tmp[ind] = value.value;
                lines_data["value" + "_" + flag] = tmp;
                flag++;
                ind = 0;
                tmp = []
            } else {
                tmp[ind] = value.value;
                ind++;
            }
        });
        var final_price_accepted = 0;
        for (const property in lines_data) {
            rec = lines_data[property];
            rec[rec.length] = rec[0] * rec[1];
            final_price_accepted += rec[0] * rec[1];
            lines_data[property] = rec;
        }
        console.log(lines_data);
        var objectData = {
            'csrf_token': $("input[name='csrf_token']").val(),
            'lines_data': JSON.stringify(lines_data),
            'final_price_accepted': final_price_accepted
        };
        var tmp_url = $("form[id='accepting']").attr("action");
        $.ajax({
            type: "POST",
            url: tmp_url,
            data: objectData,
            success: function(data) {
                console.log('Success');
                location.reload(true);

            },
            error: function() {
                console.log('Error');
            }
        });
    });

});