"""Simple Flask server for the podcast project.
The content is placeholder; replace with text from 'Podcast bullismo e cyberbullismo.pdf'.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/bullismo')
def bullismo():
    return render_template('bullismo.html', title='Bullismo')

@app.route('/cyberbullismo')
def cyberbullismo():
    return render_template('cyberbullismo.html', title='Cyberbullismo')

@app.route('/podcast')
def podcast():
    return render_template('podcast.html', title='Podcast')

@app.route('/riflessioni')
def riflessioni():
    return render_template('riflessioni.html', title='Riflessioni')

@app.route('/fonti')
def fonti():
    return render_template('fonti.html', title='Fonti')

if __name__ == '__main__':
    app.run(debug=True)
