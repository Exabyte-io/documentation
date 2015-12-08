$(document).ready(function() {

    /*
     * Sidebar open/close logic
     * Open sidebar on cliking to #menu-trigger and close on click outside sidebar
     */
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


        $('#header').toggleClass('sidebar-toggled');

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
    });

    /*
     * Text field (used in search)
     * Add blue animated border and remove with condition on focus and blur
     */
    if($('.fg-line')[0]) {
        $('body').on('focus', '.form-control', function(){
            $(this).closest('.fg-line').addClass('fg-toggled');
        })

        $('body').on('blur', '.form-control', function(){
            var p = $(this).closest('.form-group');
            var i = p.find('.form-control').val();

            if (p.hasClass('fg-float')) {
                if (i.length == 0) {
                    $(this).closest('.fg-line').removeClass('fg-toggled');
                }
            }
            else {
                $(this).closest('.fg-line').removeClass('fg-toggled');
            }
        });
    }
});


