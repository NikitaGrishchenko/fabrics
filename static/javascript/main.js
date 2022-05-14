$(function ($) {
  $("#phone").mask("+7 (999) 999-99-99", {
    autoclear: true,
  });

  $(".drawer").drawer();

  $(".rating").tooltip({
    delay: { show: 0, hide: 0 },
  });
});
