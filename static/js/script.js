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

function updateProgress(id, range) {
    const audio = document.getElementById(id);
    audio.currentTime = (range.value / 100) * audio.duration;
}

function syncProgress(id, range) {
    const audio = document.getElementById(id);
    const percent = (audio.currentTime / audio.duration) * 100;
    range.value = percent;
}
