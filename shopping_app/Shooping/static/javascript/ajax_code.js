$(function() {
    var $table_data = $('#items');
    function add_data(data){
        var list_data = '';
        $.each(data,function(i,items){
        list_data += '<tr>';
        list_data += '<td name="id" value=order.id>'+ items.id + '</td>';
        list_data += '<td name="name" value=order.name>'+ items.name + '</td>';
        list_data += '<td name="price" value=order.price>'+ items.price + '</td>';
        list_data += '</tr>';
        });
    $table_data.append(list_data);
    }
    $.ajax({
    type: 'GET',
    url: '/new_user_form',
    dataType : "json",
    success : function(data){
    add_data(data)
    },
    error: function(){
    alert("error");
    }
    });

    $(document).on('submit','#form1',function(e){
    e.preventDefault();
    var items = {
        id : $('#id').val(),
        name : $('#name').val(),
        price : $('#price').val()
    }
    $.ajax({
    type : 'POST',
    url : '/new_user_form',
    dataType : "json",
    data : items,
    success:function(data){
    const form = document.getElementById('form1');
    form.reset();
    var list_data = '';
    list_data += '<tr>';
    list_data += '<td name="id" value=items.id>'+ items.id + '</td>';
    list_data += '<td name="id" value=items.id>'+ items.name + '</td>';
    list_data += '<td name="id" value=items.id>'+ items.price + '</td>';
    list_data += '</tr>';
    $table_data.append(list_data);
    // alert("Item added")
    },
    error: function(){
    alert("error while saving data");
    }
});
});
});
