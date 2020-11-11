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

function hashChangeEvent() {
    $(window).on('hashchange', function() {
        highlightProperLink();
    });
}

function highlightProperLink() {
    if (location.hash === "#about") {
        $('#about-link').addClass('active');
    } else {
        $('#about-link').removeClass('active');
    }

    if (location.hash === "#contact") {
        $('#contact-link').addClass('active');
    } else {
        $('#contact-link').removeClass('active');
    }
}

function documentReady() {
    $(document).ready(function(){
        highlightProperLink();
    });
}

documentReady();
scrollBanner();
hashChangeEvent();

