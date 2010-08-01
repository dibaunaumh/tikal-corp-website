
$(function () {
    $("div.topMenu>ul>li").click(function () {
        $("div.topMenu>ul>li").removeClass("selected");
        $(".subMenu_level_2").fadeOut(100)
        $("div.nav-1").hide();
        $("div.nav-2").hide();
        $(this).attr("id") != "home"?$(this).addClass("selected"):$(this).removeClass("selected");
        if ($(this).attr("id") == "Solutions") { $(".subMenu_level_1").fadeIn(200); $("div.nav-1").fadeIn(500); } else { $(".subMenu_level_1").fadeOut(300); $("div.nav-1").fadeOut(300); };
    })

    $("div.subMenu_level_1>ul>li").click(function () {
        $("div.subMenu_level_1>ul>li").removeClass("selected");
        $(this).addClass("selected");
        $("div.nav-1").fadeOut(100);
        $("div.nav-2").fadeIn(500);
        $(".subMenu_level_2").fadeIn(200)
        $("div.nav-2").fadeIn(500)

    })

    $(".searchExplore").click(function () {
        $(".searchDropDown").slideToggle('fast', function () { });
    })

})
