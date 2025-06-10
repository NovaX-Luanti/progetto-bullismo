// Toggle answer visibility in the "riflessioni" page
function toggleAnswer(id) {
    const element = document.getElementById(id);
    if (element.style.display === 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }
}

// Fake audio player for podcast page
function playAudio(id) {
    const audio = document.getElementById(id);
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
    }
}
