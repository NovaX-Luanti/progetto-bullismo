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

// Keep an input[type="range"] in sync with audio playback
function syncProgress(audioId, range) {
    const audio = document.getElementById(audioId);
    if (!audio || !range) return;
    audio.addEventListener('timeupdate', () => {
        if (audio.duration) {
            range.value = (audio.currentTime / audio.duration) * 100;
        } else {
            range.value = 0;
        }
    });
}
