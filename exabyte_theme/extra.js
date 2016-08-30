$( document ).ready(function() {
    $('ul.subnav').on("click", function() {
        console.log("Clicked");
        $(this).toggleClass("active");
        $(this).next('ul.subnav').slideToggle(200).toggleClass("active");
    })
});
