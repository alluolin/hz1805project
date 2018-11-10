// $(function () {
//     $("form").submit(function () {
//         var uname = $("#name_id").val();
//         var pwd = $("#pwd_id").val();
//
//         if (uname.length < 3){
//             alert("用户过短");
//             return false;
//         }
//         if (pwd.length < 3){
//             alert("密码过短");
//             return false;
//         }
//
//         var pwd_md5 = md5(pwd);
//         $("#pwd_id").val(pwd_md5);
//     })
// })

$(function () {
    $("#submit").click(login)
});

function login() {
//    拿到用户输入，校验格式，md5，ajax，
// 成功跳转到mine页面，失败提示alter()

    var name = $("#uid").val();
    var pwd = $("#u_pwd").val();
    if (name.length < 3) {
        alert('用户名过短');
        return;
    }
    if (pwd.length < 6) {
        alert("密码过短");
        return;
    }
    var enc_pwd = md5(pwd);
    $.ajax({
        url: "/axf/login",
        data: {
            "name": name,
            'pwd': enc_pwd

        },
        method: 'post',
        success: function (res) {
            if (res.code == 1) {
                window.open(res.data, target = "_self")

            } else {
                alert(res.msg);
            }

        },
        error: function () {

        },
        complete: function () {

        }
    });

}


