"""Simple Flask server for the podcast project.
The content is placeholder; replace with text from 'Podcast bullismo e cyberbullismo.pdf'.
"""
from flask import Flask, render_template

# This application serves a very small website for a school project about
# bullying and cyberbullying.  Each route simply renders a template.

app = Flask(__name__)

# Home page of the site
@app.route('/')
def index():
    """Render the welcome page."""
    return render_template('index.html', title='Home')

# Page with basic information about bullying
@app.route('/bullismo')
def bullismo():
    """Display the bullying overview page."""
    return render_template('bullismo.html', title='Bullismo')

# Page dedicated to cyberbullying
@app.route('/cyberbullismo')
def cyberbullismo():
    """Show information about cyberbullying."""
    return render_template('cyberbullismo.html', title='Cyberbullismo')

# Podcast landing page where students can listen to episodes
@app.route('/podcast')
def podcast():
    """List the available podcast episodes."""
    return render_template('podcast.html', title='Podcast')

# Questions for students to reflect on the topic
@app.route('/riflessioni')
def riflessioni():
    """Present a page with reflection questions."""
    return render_template('riflessioni.html', title='Riflessioni')

# Sources and references used in the project
@app.route('/fonti')
def fonti():
    """Show the bibliography and other resources."""
    return render_template('fonti.html', title='Fonti')

if __name__ == '__main__':
    app.run(debug=True)
