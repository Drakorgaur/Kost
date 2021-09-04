$(document).ready(function () {
    $("#register").css("background-color", "#505680");
    $("#register").click(function () {
        $("div[name='register']").removeAttr('hidden');
        $("div[name='login']").attr("hidden", true);
        $("#login").css("background-color", "#505680");
        $("#register").css("background-color", "#383c57");
    });

    $("#login").click(function () {
        $("div[name='register']").attr("hidden", true);
        $("div[name='login']").removeAttr('hidden');
        $("#register").css("background-color", "#505680");
        $("#login").css("background-color", "#383c57");
    });

});