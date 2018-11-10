var cate_toggle_tag = false;
var sort_toggle_tag = false;
$(function () {
//    给全部类型加点击事件
    $("#all_cate").click(cate_toggle);
    $("#cates").click(cate_toggle);

//    排序
    $("#all_sort").click(sort_toggle);
    $("#sorts").click(sort_toggle);
})

function sort_toggle() {
    $("#sorts").toggle();
    if (sort_toggle_tag == false){
        $("#all_sort").find("span").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        sort_toggle_tag = true;
    } else{
        $("#all_sort").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        sort_toggle_tag = false;
    }
}

function cate_toggle() {
    $("#cates").toggle();
    // console.log($(this))
    if (cate_toggle_tag == false){
        $("#all_cate").find("span").removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        cate_toggle_tag = true;
    } else{
        $("#all_cate").find("span").removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        cate_toggle_tag = false;
    }

}