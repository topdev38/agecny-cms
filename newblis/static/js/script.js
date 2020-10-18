(function($) {

	

	"use strict";

	

	//Hide Loading Box (Preloader)

	function handlePreloader() {

		if($('.preloader').length){

			$('.preloader').delay(200).fadeOut(500);

		}

	}

	

	

	//Update Header Style and Scroll to Top

	function headerStyle() {

		if($('.main-header').length){

			var windowpos = $(window).scrollTop();

			var siteHeader = $('.main-header');

			var sticky_header = $('.main-header .sticky-header, .header-style-two .outer-container, .header-style-four .header-lower, .header-style-six .outer-container');

			var scrollLink = $('.scroll-to-top');

			if (windowpos > 55) {

				siteHeader.addClass('fixed-header');

				sticky_header.addClass("animated slideInDown");

				scrollLink.fadeIn(300);

			} else {

				siteHeader.removeClass('fixed-header');

				sticky_header.removeClass("animated slideInDown");

				scrollLink.fadeOut(300);

			}

		}

	}

	

	headerStyle();



	//Submenu Dropdown Toggle

	if($('.main-header li.dropdown ul').length){

		$('.main-header li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');

		

		//Dropdown Button

		$('.main-header li.dropdown .dropdown-btn').on('click', function() {

			$(this).prev('ul').slideToggle(500);

		});



		//Megamenu Toggle

		$('.main-header .main-menu li.dropdown .dropdown-btn').on('click', function() {

			$(this).prev('.mega-menu').slideToggle(500);

		});

		

		//Disable dropdown parent link

		$('.main-header .navigation li.dropdown > a,.hidden-bar .side-menu li.dropdown > a').on('click', function(e) {

			e.preventDefault();

		});

	}





	//Sidenav Two Toggle

	if($('.sidenav-bar, .hidden-bar').length){

		

		//Dropdown Button

		$('.sidenav-bar .navigation li.dropdown > a').on('click', function(e) {

			e.preventDefault();

			var ParentBox = $(this).parent('li');

			if($(ParentBox).hasClass('active')===true){

				$(ParentBox).removeClass('active');

			}else{

				$('.sidenav-bar .navigation li.dropdown').removeClass('active');

				$(this).parent('li').addClass('active');

			}

		});

	

		$(".sidenav-bar .side-nav .navigation li.dropdown > ul").slideUp();



		//Dropdown Button

		$('.sidenav-bar .side-nav .navigation li.dropdown > a').on('click', function() {

			$(this).next('ul').slideToggle(400);

			$(this).parent().siblings().find("ul").slideUp(400);

		});



		//Show Sidebar Button

		$('.main-header .nav-toggler').on('click', function(e) {

			e.preventDefault();

			$('body').toggleClass('active-side-nav');

		});

		

		//Dropdown Button

		$('.sidenav-bar .cross-icon, .hidden-bar .cross-icon, .form-back-drop').on('click', function(e) {

			e.preventDefault();

			$('body').removeClass('active-side-nav');

		});

	}





	//Banner Carousel

	if ($('.banner-carousel').length) {

		$('.banner-carousel').owlCarousel({

			animateOut: 'fadeOut',

		    animateIn: 'fadeIn',

			loop:true,

			margin:0,

			nav:true,

			smartSpeed: 700,

			autoHeight: true,

			autoplay: true,

			autoplayTimeout:10000,

			navText: [ '<span class="fa fa-long-arrow-left"></span> prev', 'next<span class="fa fa-long-arrow-right"></span>' ],

			responsive:{

				0:{

					items:1

				},

				600:{

					items:1

				},

				1024:{

					items:1

				},

			}

		});    		

	}



	//Banner Carousel Two

	if ($('.banner-carousel-two').length) {

		$('.banner-carousel-two').owlCarousel({

			animateOut: 'fadeOut',

		    animateIn: 'fadeIn',

			loop:true,

			margin:30,

			nav:true,

			smartSpeed: 15000,

			mouseDrag:false,

			touchDrag:false,

			autoHeight: true,

			autoplay: true,

			autoplayTimeout:10000,

			navText: [ '<span class="fa fa-long-arrow-left"></span> prev', 'next<span class="fa fa-long-arrow-right"></span>' ],

			responsive:{

				0:{

					items:1

				},

				600:{

					items:1

				},

				1024:{

					items:1

				},

			}

		});    		

	}

	//Testimonial Carousel two

	if ($('.testimonial-carousel-two').length) {

		$('.testimonial-carousel-two').owlCarousel({

			loop:true,

			margin:70,

			nav:true,

			smartSpeed: 700,

			autoplay: true,

			navText: [ '<span class="fa fa-long-arrow-left"></span> prev', 'next<span class="fa fa-long-arrow-right"></span>' ],

			responsive:{

				0:{

					items:1

				},

				600:{

					items:1

				},

				768:{

					margin:30,

					items:2

				},

				1024:{

					items:2

				}

			}

		});    		

	}



	//Projects Carousel

	if ($('.projects-carousel').length) {

		$('.projects-carousel').owlCarousel({

			loop:true,

			margin:0,

			nav:true,

			smartSpeed: 700,

			autoplay: true,

			navText: [ '<span class="fa fa-long-arrow-left"></span> prev', 'next<span class="fa fa-long-arrow-right"></span>' ],

			responsive:{

				0:{

					items:1

				},

				600:{

					items:2

				},

				800:{

					items:3

				},

				1024:{

					items:4

				},

				1400:{

					items:5

				}

			}

		});    		

	}



	//Projects Carousel

	if ($('.projects-carousel-two').length) {

		$('.projects-carousel-two').owlCarousel({

			animateOut: 'slideOutDown',

		    animateIn: 'zoomIn',

			loop:true,

			margin:30,

			nav:true,

			smartSpeed: 15000,

			mouseDrag:false,

			touchDrag:false,

			autoHeight: true,

			autoplay: true,

			autoplayTimeout:10000,

			navText: [ '<span class="fa fa-chevron-left"></span>', '<span class="fa fa-chevron-right"></span>' ],

			responsive:{

				0:{

					items:1

				},

				600:{

					items:1

				},

				1024:{

					items:1

				}

			}

		});     		

	}


/* ==========================================================================

   When document is loading, do

   ========================================================================== */

	

	$(window).on('load', function() {

		handlePreloader();

	});	



})(window.jQuery);