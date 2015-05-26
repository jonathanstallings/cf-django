/*************************
Event Listeners
**************************/

$("#navbar-toggle").on("click", function (e) {
  e.preventDefault();
  $("nav.navbar-collapse").toggleClass("collapse");
});
