let slider;
let sound;
let sound_winner;

function startWheel() {
    sound.pause();
    sound.currentTime = 0;
    sound.play();
    slider.startAuto()
}

function stopWheel(id = 0) {
    slider.stopAuto();
    setTimeout(function () {
        sound.pause();
        sound_winner.currentTime = 0;
        sound_winner.play();
        if (slider.getCurrentSlide() !== id) {
            slider.goToSlide(id)
        }
    }, 220)
}

$(document).ready(function () {
    sound = document.getElementById("sound");
    sound_winner = document.getElementById("sound_winner");
    slider = $('.slider').bxSlider({
        autoControls: !1,
        stopAutoOnClick: !0,
        pager: !1,
        controls: !1,
        randomStart: !0,
        touchEnabled: !1,
        slideWidth: 750,
        mode: 'vertical',
        preloadImages: 'all',
        speed: 100,
        pause: 110
    })
});