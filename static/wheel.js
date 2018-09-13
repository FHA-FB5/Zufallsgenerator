let sound_wheel;
let sound_winner;
let sound_wheel_j;
let sound_winner_j;
let sound_cheer;
let images;

$(document).ready(function () {
    sound_wheel = document.getElementById('sound_wheel');
    sound_winner = document.getElementById('sound_winner');
    sound_cheer = document.getElementById('sound_cheer');
    sound_wheel_j = $('#sound_wheel');
    sound_winner_j = $('#sound_winner');
    images = $('#images');

    $('#wheel .wheelImages').on('click', function () {
        wheel_start();
    });
});

function wheel_start() {
    sound_wheel.pause();
    sound_wheel_j.animate({volume: 1.0}, 1000);
    sound_wheel.play();
    images.addClass('spin').fadeIn(1000);
    $('.winner_image.winner').removeClass('winner').fadeOut('slow');
}

function wheel_stop(id) {
    sound_winner.play();
    sound_wheel_j.animate({volume: 0.0}, 3500);
    images.fadeOut(2000);
    setTimeout(function () {
        images.removeClass('spin');
    }, 2000);
    let winner = $("img#" + id + ".winner_image").addClass('winner');
    setTimeout(function () {
        winner.fadeIn(2500)
    }, 2500);
    setTimeout(function () {
        sound_cheer.play();
    }, 4000)
}