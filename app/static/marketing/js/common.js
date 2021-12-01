window.isBot = /bot|googlebot|crawler|spider|robot|crawling|chrome-lighthouse|Lighthouse|Speed Insights|Pingdom/i.test(window.navigator.userAgent);
if (window.isBot) {
  document.querySelector("body").classList.add('no-animate');
};


(function(fn) {
  if (window.isBot) return false;
  if (document.readyState != 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }

})(initJS);

function initJS() {
  if (!window.isBot) {
    // bot
  }
  calculate1vh();
  window.addEventListener('resize', calculate1vh);
  menu(jQuery);
  introPartnersSwiper(jQuery);
  introHexagon(jQuery);
  homeNewsSwiper(jQuery);
  servicesSwiper(jQuery);
  serviceClientsSwiper(jQuery);
  serviceProcessSwiper(jQuery);
  $('#trigger-service').length && onWheel(jQuery)
  aosInit(window.isBot)
}


var lastScrollTop = 0,
  scrollDirection = 'down';

document.addEventListener("scroll", function() {
  var st = window.pageYOffset || document.documentElement.scrollTop;
  if (st > lastScrollTop) {
    scrollDirection = 'down';
  } else {
    scrollDirection = 'up';
  }
  lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
}, false);

function calculate1vh() {
  var vh = window.innerHeight * 0.01;
  document.documentElement.style.setProperty('--vh', vh + 'px');
}

function menu($) {
  $('.header__bars').on('click', function(event) {
    event.preventDefault();
    pageDisableScroll();
    if (true) {}
      if($(this).hasClass('active')){
        pageEnableScroll();
      }else{
        pageDisableScroll();
      }
    $(this).toggleClass('active');
    $('.menu').toggleClass('active');
  });
}

function introPartnersSwiper($) {
  const inrtoProductSwiper = new Swiper('.intro__partners-slider', {
    slidesPerView: 'auto',
    slideClass: 'intro__partners-itm',
    wrapperClass: 'intro__partners-slider__list',
    spaceBetween: 24,
    breakpoints: {
      320: {
        spaceBetween: 24,
      },
      1024: {
        spaceBetween: 42,
      }
    },
  });
}

function introHexagon($) {
  let max = 22;
    // left = $('.intro__hexagon-bg path:nth-child(50)').offset().left;
  setTimeout(() => {
    $('.intro__hexagon-accent_itm').addClass('hexagon_blink');
  }, 5000);
  setInterval(function() {
    let nth = Math.floor(Math.random() * max);
    let introHexagon = $('.intro__hexagon-bg path:nth-child(' + nth + ')');
    if (introHexagon.length) {
      let left = introHexagon.offset().left;
      let top = introHexagon.offset().top;
      $('.intro__hexagon-accent_itm').css({
        left: left + 'px',
        top: top + 'px'
      });
    }
  }, 5000)
}


function homeNewsSwiper($) {
  const homeNewsSwiper = new Swiper('.home_news__slider', {
    slideClass: 'home_news__itm',
    wrapperClass: 'home_news__slider-list',
    spaceBetween: 12,
    breakpoints: {
      320: {
        spaceBetween: 12,
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      }
    },
  });
}


function servicesSwiper($){

  const servicesSliderSwiper = new Swiper('.service_slider__slider', {
    slidesPerView: 1,
    slideClass: 'service_slider__itm',
    wrapperClass: 'service_slider__slider-list',
    loop: true,
    effect: 'fade',
    fadeEffect: {
      crossFade: true
    },
    pagination: {
      el: ".service_slider__slider-pagination",
      type: "fraction",
    },
    navigation: {
      nextEl: ".service_slider__slider-next",
      prevEl: ".service_slider__slider-prev",
    },
  })

}


function serviceClientsSwiper($) {
  const serviceClientsSliderSwiper = new Swiper('.service_clients-slider', {
    slidesPerView: 'auto',
    slideClass: 'service_clients-itm',
    wrapperClass: 'service_clients-slider__list',
    spaceBetween: 48,
    breakpoints: {
      320: {
        spaceBetween: 48,
      },
      1200: {
        spaceBetween: 110,
      }
    },
  });
}



function serviceProcessSwiper($) {
  const serviceProcessSliderSwiper = new Swiper('.service_process__slider', {
    slidesPerView: 1,
    slideClass: 'service_process__itm',
    wrapperClass: 'service_process__slider-list',
    breakpoints: {
      320: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
      1400: {
        slidesPerView: 4,
      }
    },
    navigation: {
      nextEl: ".service_process__slider-next",
      prevEl: ".service_process__slider-prev",
    },
  });
}

function pageDisableScroll(){
  var html = $("html"), scrollbar = window.innerWidth - document.body.clientWidth;
  scrollbar && html.css('paddingRight', scrollbar + "px");
  html.css("overflow", "hidden")
}

function pageEnableScroll(){
  var html = $("html");
  html.css({"overflow": "visible", paddingRight: 0});
}


function aosInit(bot) {
  var disable = 'mobile';
  if ( bot || /^((?!chrome).)*safari/i.test(navigator.userAgent) ) {
    // document.querySelector("body").classList.add('no-animate');
    disable = true;
  };

  AOS.init({
    // Global settings:
    disable: disable, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
    startEvent: 'DOMContentLoaded', // name of the event dispatched on the document, that AOS should initialize on
    initClassName: 'aos-init', // class applied after initialization
    animatedClassName: 'aos-animate', // class applied on animation
    useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
    disableMutationObserver: false, // disables automatic mutations' detections (advanced)
    debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
    throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)
    // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
    // offset: aosOffset, // offset (in px) from the original trigger point
    delay: 100, // values from 0 to 3000, with step 50ms
    duration: 600, // values from 0 to 3000, with step 50ms
    easing: 'ease-in-out', // default easing for AOS animations
    once: true, // whether animation should happen only once - while scrolling down
    mirror: false, // whether elements should animate out while scrolling past them
    anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
  });
}

function onWheel($) {
  var elem = document.getElementById('trigger-service');
  isInner = false;

  if (elem.addEventListener) {
    if ('onwheel' in document) {
      // IE9+, FF17+
      elem.addEventListener("wheel", onWheelService);
    } else if ('onmousewheel' in document) {
      // устаревший вариант события
      elem.addEventListener("mousewheel", onWheelService);
    } else {
      // Firefox < 17
      elem.addEventListener("MozMousePixelScroll", onWheelService);
    }
  } else { // IE8-
    elem.attachEvent("onmousewheel", onWheelService);
  }

  $("#stiky-img").stick_in_parent({offset_top: 0});


  // Это решение предусматривает поддержку IE8-
  function onWheelService(e) {
    if ($(window).innerWidth() >= 1024 && isInner) {
      e = e || window.event;
      // deltaY, detail содержат пиксели
      // wheelDelta не дает возможность узнать количество пикселей
      // onwheel || MozMousePixelScroll || onmousewheel
      var delta = e.deltaY || e.detail || e.wheelDelta;
      if (delta > 0) {
        if (slideService == 2) {
          $('html, body').stop().animate({
            scrollTop: $('#trigger-service').offset().top + $('#trigger-service').height()
          }, 500);
        } else {
          $('html, body').stop().animate({
            scrollTop: $('#trigger-service-section-' + (slideService + 1)).offset().top
          }, 500);
        }
      } else {
        if (slideService == 1) {
          $('html, body').stop().animate({
            scrollTop: $('#trigger-service').offset().top - vh
          }, 500);
        } else {
          $('html, body').stop().animate({
            scrollTop: $('#trigger-service-section-' + (slideService - 1)).offset().top
          }, 500);
        }
      }
      e.preventDefault ? e.preventDefault() : (e.returnValue = false);
    }
  }
}
