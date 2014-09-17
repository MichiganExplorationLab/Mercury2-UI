/*
Contains the Javascript that is used to power the various parts of the Mercury2 User Interface.
*/

/***** Global interface elements *****/
$(function(){
  // Event boxes
  $(".alert").on('click', 'span', function(){
    $(this).parent().hide(300);
  });
});