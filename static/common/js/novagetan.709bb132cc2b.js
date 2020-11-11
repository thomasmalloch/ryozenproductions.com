//Parallax & fade on scroll

function scrollBanner() {
  $(document).on('scroll', function(){
    var scrollPos = $(this).scrollTop();
    $('.parallax-fade-top').css({
      'top' : (scrollPos/2)+'px',
      'opacity' : 1-(scrollPos/950)
    });

    $('.parallax').css({
      'top' : (scrollPos * 0.3)+'px',
    });
  });
}

scrollBanner();