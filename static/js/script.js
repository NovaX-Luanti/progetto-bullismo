// Small collection of functions used throughout the website.
// They are intentionally simple so that students can read and
// understand what is happening.

// Toggle answer visibility in the "riflessioni" page.
// When a question is clicked we show (or hide) the related answer.
function toggleAnswer(id) {
    const element = document.getElementById(id); // paragraph with the answer
    if (element.style.display === 'none') {
        // show the answer
        element.style.display = 'block';
    } else {
        // hide the answer
        element.style.display = 'none';
    }
}

// Play or pause an episode on the podcast page.
// Each episode has an <audio> tag with a matching id.
function playAudio(id) {
    const audio = document.getElementById(id); // the audio element
    if (audio.paused) {
        // start playback
        audio.play();
    } else {
        // pause the sound
        audio.pause();
    }
}

// Keep an input[type="range"] in sync with audio playback.
// This creates a simple progress bar for the audio element.
function syncProgress(audioId, range) {
    const audio = document.getElementById(audioId); // audio element to track
    if (!audio || !range) return; // safety check
    audio.addEventListener('timeupdate', () => {
        // "timeupdate" fires as the audio plays.
        if (audio.duration) {
            // Update the range 0-100 with the playback percentage
            range.value = (audio.currentTime / audio.duration) * 100;
        } else {
            range.value = 0;
        }
    });
}
