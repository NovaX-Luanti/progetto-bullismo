"""Flask server per il progetto scolastico.
Ogni route restituisce un template HTML con contenuti
ispirati al PDF "Podcast bullismo e cyberbullismo".
I testi sono di esempio e possono essere sostituiti
con quelli forniti dagli studenti.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Pagina principale con presentazione del progetto."""
    return render_template('index.html', title='Home')

@app.route('/bullismo')
def bullismo():
    """Spiega cos'è il bullismo e come affrontarlo."""
    return render_template('bullismo.html', title='Bullismo')

@app.route('/cyberbullismo')
def cyberbullismo():
    """Pagina dedicata al bullismo digitale."""
    return render_template('cyberbullismo.html', title='Cyberbullismo')

@app.route('/podcast')
def podcast():
    """Elenco degli episodi del podcast."""
    return render_template('podcast.html', title='Podcast')

@app.route('/notizie')
def notizie():
    """Sezione con notizie e aggiornamenti."""
    return render_template('notizie.html', title='Notizie')

@app.route('/emergenza')
def emergenza():
    """Contatti e informazioni per le emergenze."""
    return render_template('emergenza.html', title='Emergenza')

@app.route('/forum')
def forum():
    """Area forum (placeholder)."""
    return render_template('forum.html', title='Forum')

@app.route('/consigliaci')
def consigliaci():
    """Modulo per inviare suggerimenti."""
    return render_template('consigliaci.html', title='Consigliaci')

@app.route('/su')
def su():
    """Informazioni sul progetto e crediti."""
    return render_template('su.html', title='Su di noi')

@app.route('/cerca')
def cerca():
    """Pagina di ricerca (non implementata)."""
    return render_template('cerca.html', title='Cerca')

@app.route('/riflessioni')
def riflessioni():
    """Domande per stimolare la riflessione."""
    return render_template('riflessioni.html', title='Riflessioni')

@app.route('/fonti')
def fonti():
    """Elenco delle fonti utilizzate."""
    return render_template('fonti.html', title='Fonti')

if __name__ == '__main__':
    app.run(debug=True)
