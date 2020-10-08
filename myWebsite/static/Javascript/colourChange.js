var landing = document.querySelectorAll('#js')

// function which randomly generates a hexcode - random colour selection
function getRanCol(){
    var letters = '0123456789ABCDEF';
    var colour = '#';
    for (i = 0; i < 6; i++){
        colour = colour + letters[Math.floor(Math.random()*16)];
    }
    return colour
}

// for loop applying the random colour to each element selected
function setColour(){
    colInput = getRanCol()
    for (i = 0; i < landing.length; i++){
        landing[i].style.color = colInput;
    }
}

//built in method to call the setColour method every 500 mili secs
setInterval('setColour()', 500);