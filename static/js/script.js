// Mostra o nasconde la risposta nelle domande di riflessione
function toggleAnswer(id) {
    const element = document.getElementById(id);
    if (element.style.display === 'none') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }
}

// Gestione semplificata del player audio nella pagina podcast
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
