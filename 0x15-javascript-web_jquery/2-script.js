#!/usr/bin/node
// updates the text color of the <header> element to red (#FF0000)

$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
