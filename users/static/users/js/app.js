/*************************
Special User Behavior
**************************/

var FRODO_ID = 1;
var GANDALF_ID =4;

$users_ul = $("#current-users ul");

function selectByID (user_id) {
    //Selects a user list item by user_id
    return $users_ul.find('li[data-id="' + user_id + '"]');
}

function removeTransitions (user_id) {
    //Remove CSS transitions class
    var $thisID = selectByID(user_id);
    
    $thisID.removeClass('showTransitions');
}

function fadeByID (user_id) {
    //Fades a user list item.
    var $thisID = selectByID(user_id);
    
    $thisID.addClass('showTransitions');
    $thisID.addClass('faded');
    return $thisID;
}

function revealByID (user_id) {
    // Unfades and unhides a user list item.
    var $thisID = selectByID(user_id);
    
    $thisID.removeClass('faded hidden');
    setTimeout(removeTransitions, 1000, user_id);
    return $thisID;
}

function getDelButtonByID (user_id) {
    //Gets the delete anchor 'button' in the user list item.
    return selectByID(user_id).find('a.delete');
}

function changeDelButtonText (user_id, text) {
    //Changes the text of the delete anchor 'button' in user list item.
    getDelButtonByID(user_id).text(text);
}

function frodoVanish (user_id) {
    //Frodo puts on the rind and . . .
    fadeByID(user_id);
    changeDelButtonText(user_id, "Oh no! Mr. Frodo!");
}

function whiteRider (user_id) {
    //User list item is styled as Gandalf the White.
    var $thisID = selectByID(user_id).addClass('showTransitions');
    
    $thisID.addClass('whiteRider').removeClass('hover');
    $thisID.find('a.user-link').text("Gandalf the White");
}

function greyPilgrim (user_id) {
    //Remove list item styling from Gandalf the White.
    return selectByID(user_id).removeClass('whiteRider');
}

/*************************
Event Listeners
**************************/

$("#navbar-toggle").on("click", function (e) {
  e.preventDefault();
  $("nav.navbar-collapse").toggleClass("collapse");
});

getDelButtonByID(FRODO_ID).on("click", function (e) {
    var $delButton = getDelButtonByID(FRODO_ID);
    
    e.preventDefault();
    frodoVanish(FRODO_ID);
    $delButton.off("click");
    setTimeout(changeDelButtonText, 2000, FRODO_ID, "Come Back!");
});

getDelButtonByID(GANDALF_ID).on("click", function (e) {
    var $delButton = getDelButtonByID(GANDALF_ID);
    
    e.preventDefault();
    whiteRider(GANDALF_ID);
    $delButton.off("click");
    setTimeout(changeDelButtonText, 2000, GANDALF_ID, "Return?");
});
