function hadleSubnavClick() {
    // show/hide the content of second-level navigation on click
    $('li.toctree-l1').on("click", function (event) {
        // initiate show/hide only when clicking at the top level
        $(this).hasClass("open")
        && $(event.target).parent().hasClass("toctree-l1")
        && $(event.target).is("span")
            ? $(".toctree-l2", this).hide(200) : $(".toctree-l2", this).show(200);
        $(this).toggleClass("open");
    });

    $('li.current').show(50);
    $('li.current').siblings().show(0);
}

$(document).ready(hadleSubnavClick);
