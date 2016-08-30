$( document ).ready(function() {
    $('ul.subnav').on("click", function() {
        $(this).toggleClass("active");
        $(".toctree-l1", this).slideToggle(200);
    })
});
