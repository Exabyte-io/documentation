$( document ).ready(function() {
    $('ul.subnav').on("click", function(event) {
        //$(".toctree-l1").hide(90); // Close other menus
        $(this).toggleClass("active");
        $(".toctree-l1", this).show(200);
    })

    $('li.current').show(50);
    $('li.current').siblings().show(0);
});
