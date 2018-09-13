let sound_wheel;
let sound_winner;
let sound_wheel_j;
let sound_winner_j;

$( document ).ready( function() {
    sound_wheel = document.getElementById('sound_wheel');
    sound_winner = document.getElementById('sound_winner');
    sound_wheel_j = $('#sound_wheel');
    sound_winner_j = $('#sound_winner');

    $('#wheel .wheelImages').on( 'click', function() {
        wheel_start();
     });
});
function wheel_start(){
    sound_wheel_j.animate({volume: 1.0}, 1000);
    sound_wheel.play();
    const selector = $('#wheel .wheelImages div, #images > div');
    selector.addClass('spinning');
    $('.winner_image.winner').removeClass('winner').fadeOut('slow');
}
function wheel_stop(id){
    sound_winner.play();
    sound_wheel_j.animate({volume: 0.1}, 1500);
    setTimeout(function(){
        sound_wheel.pause();

        const selector = $('#wheel .wheelImages div, #images > div');

        $("img#" + id + ".winner_image").addClass('winner').fadeIn(1500, function(){
            selector.removeClass( 'spinning' );
        });
    }, 2000);
}