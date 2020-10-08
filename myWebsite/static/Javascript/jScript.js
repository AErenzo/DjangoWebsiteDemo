//alert('Welcome to Open Research')

var head1 = document.querySelector('h1')
var head2 = document.querySelector('h2')


//headings.style.color = 'green'

function getRanCol(){
    var letters = '0123456789ABCDEF';
    var colour = '#';
    for (i = 0; i < 6; i++){
        colour = colour + letters[Math.floor(Math.random()*16)];
    }
    return colour
}

function landingClassColour(){
    colInput = getRanCol()
    head1.style.color = colInput;
    head2.style.color = colInput;
}

setInterval('landingClassColour()', 500);




