from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404