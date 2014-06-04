$( document ).ready( function ()
{
    populateReloadButton();

    $.ajax( {
        dataType: "json",
        url:      "scripts/generate.py",
        success:  function ( data )
        {
            $( "#synop" ).html( data.result ).fadeIn( "slow" );
        },
        error:    function ( resp, msg )
        {
            console.log( resp, msg );
            $.jnotify( resp.statusText, "error" );
            location.reload();
        }
    } );
} );

var reload_button_values = [
    'Eh, pitch me another one...',
    'NEXT!',
    'That\'s awful. Next?',
    'Awful.',
    'Try for another?',
    'Did a five year old write this? Next!',
    'Why do I even bother? Sigh. Another, please.',
    'Not bad, but let\'s see what else there is.',
    'Atrocious.',
    'Rotten.',
    'That might sell overseas. Sell this to someone else.',
    'How dare you!',
    'Zzz...',
    'Boring. Next.',
    'Why do you hate me?',
    'GET THIS TRASH OUT OF HERE.',
    'Noooop.',
    'There\'s already a bunch of movies like this out there.',
    'Too original. Audiences want something familiar.',
    'Not toyetic enough.',
    'Hot!',
    'This one isn\'t half bad. Or half good.',
    'I could write a better one with a pen between my toes. Here, watch...',
    'Go home. Get some rest. Come back with a fresh idea.',
    '1947 called. They want their movie pitch back.',
    '...',
    'Hey, this could spark a franchise...',
    'Decent. Come back next month and pitch it again.',
    'I love it! ...HA! I\'m kidding, it\'s terrible.',
    'People that pitch movies like this make me sick.'

];

function populateReloadButton()
{
    $( "#Reload" ).html( reload_button_values[Math.round( Math.random() * reload_button_values.length )] );
}