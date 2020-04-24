(function ($) {
    $('.main-nav-li > li').on('click', function () {
        var now = $(this).text();
        var check = 0;
        if (text == 'HOME') {
            $('.main-nav-li + li').addClass('colorlib-active');
            check == 0;
        } else {
            $(this).addClass("colorlib-active");
            check == 1;

        }


    });
})(jQuery);



    
