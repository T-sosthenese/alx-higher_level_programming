$(function () {
  // Start by selecting the element to be clicked using jQuery
  $('#red_header').bind('click', function () {
    $('header').css('color', '#FF0000');
  });
});
