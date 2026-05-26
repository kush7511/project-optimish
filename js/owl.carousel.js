/* Local compatibility shim for pages that reference owl.carousel.js. */
(function ($) {
  if (!$ || $.fn.owlCarousel) {
    return;
  }

  $.fn.owlCarousel = function () {
    return this;
  };
})(window.jQuery);
