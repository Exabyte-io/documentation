function getSearchTerm()
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == 'q')
        {
            return sParameterName[1];
        }
    }
}

$(document).ready(function() {

    var search_term = getSearchTerm(),
        $search_modal = $('#mkdocs_search_modal');

    if(search_term){
        $search_modal.modal();
    }

    // make sure search input gets autofocus everytime modal opens.
    $search_modal.on('shown.bs.modal', function () {
        $search_modal.find('#mkdocs-search-query').focus();
    });

    // Highlight.js
    hljs.initHighlightingOnLoad();
    $('table').addClass('table table-striped table-hover');

    // Sidebar
    $('body').on('click', '#menu-trigger', function(e){
        e.preventDefault();
        var x = '#sidebar';

        $(x).toggleClass('toggled');
        $(this).toggleClass('open');
        $('body').toggleClass('modal-open');

        //Close opened sub-menus
        $('.sub-menu.toggled').not('.active').each(function(){
            $(this).removeClass('toggled');
            $(this).find('ul').hide();
        });

        $elem = '#sidebar';
        $elem2 = '#menu-trigger';

        if (!$('#sidebar').hasClass('toggled')) {
            $('#header').toggleClass('sidebar-toggled');
        }

        //When clicking outside
        if ($('#header').hasClass('sidebar-toggled')) {
            $(document).on('click', function (e) {
                if (($(e.target).closest($elem).length === 0) && ($(e.target).closest($elem2).length === 0)) {
                    setTimeout(function(){
                        $('body').removeClass('modal-open');
                        $($elem).removeClass('toggled');
                        $('#header').removeClass('sidebar-toggled');
                        $($elem2).removeClass('open');
                    });
                }
            });
        }
    })
});


$('body').scrollspy({
    target: '#sidebar'
});

/* Prevent disabled links from causing a page reload */
$("li.disabled a").click(function() {
    event.preventDefault();
});
