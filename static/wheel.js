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
});

function wheel_start() {
    sound_wheel.pause();
    sound_wheel_j.animate({volume: 1.0}, 1000);
    sound_wheel.play();
    let winner = $('.winner').fadeOut(1000);
    setTimeout(function () {
        winner.removeClass('winner');
        images.addClass('wheel').fadeIn(1000);
    }, 1000);
}

function wheel_stop(id) {
    let winner = $("#winners #" + id).addClass('winner');
    sound_winner.play();
    sound_wheel_j.animate({volume: 0.0}, 3500);
    images.fadeOut(2000);
    setTimeout(function () {
        images.removeClass('wheel');
        winner.fadeIn(3000);
        setTimeout(function () {
            sound_cheer.play();
        }, 1000)
    }, 2000);
}