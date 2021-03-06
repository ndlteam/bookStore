$("a[name='checkout']").each(function () {
    var currentEle = $(this);
    currentEle.on('click', function () {
        var good_price = currentEle.prev().prev().children().children().text();
        var good_name = currentEle.parent().prev().html();
        window.location.href = "/checkout/?good_name=" + good_name + "&good_price=" + good_price;
    })
});


function savenewpassword() {
    var newpassword = document.getElementById('newpassword').value;
    layer.confirm('确定要更改密码吗？', {
        btn: ['确定', '不了'] //按钮
    }, function () {
        window.location.href = "/save_new_password/?newpassword=" + newpassword;
    }, function () {

    });
}


function save() {
    var studentid = document.getElementById("studentid").getAttribute("placeholder");
    var citynum = document.getElementById("city").selectedIndex;
    var city = document.getElementById("city").options[citynum].text;
    var address = document.getElementById("address").value;
    var zipcode = document.getElementById("zipcode").value;
    var telephone = document.getElementById("telephone").value;
    var qq = document.getElementById("qq").value;
    $.ajax({
            url: "/update_user/?studentid=" + studentid + "&city=" + city + "&address=" + address + "&zipcode=" + zipcode + "&telephone=" + telephone + "&qq=" + qq + "&citynum=" + citynum,
            type: 'GET',
            success: function (arg) {
                layer.msg("保存完毕");
            }
        }
    )
}

$("a[name='add_to_cart']").each(function () {
    var currentEle = $(this);
    currentEle.on('click', function () {
        var good_price = currentEle.prev().prev().prev().children().children().html();
        var good_name = currentEle.parent().prev().html();
        var good_pic = currentEle.parent().parent().children().next().children().children().attr("src");
        $.ajax({
                url: "/add_to_cart/?good_name=" + good_name + "&good_price=" + good_price + "&good_pic=" + good_pic,
                type: 'GET',
                success: function (arg) {
                    layer.msg("已添加到购物车");
                }
            }
        )
    })
});

