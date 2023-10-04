$(function () {
  // Selecting the element to be clicked and binding it to the click listener
  $('#red_header').bind('click', function () {
    // Adds a 'red' class element to the header after clicking
    $('header').addClass('red');
  });
});
