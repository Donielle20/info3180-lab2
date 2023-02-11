from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile')
def profile():
    now = datetime.datetime.now()
    now = str(now)
    now = now.split()
    date = format_date_joined(now[0])

    if (date[0] == "01"):
        date = "January"
    elif (date[0] == "02"):
        date = "February"
    elif (date[0] == "03"):
        date = "March"
    elif (date[0] == "04"):
        date = "April"
    elif (date[0] == "05"):
        date = "May"
    elif (date[0] == "06"):
        date = "June"
    elif (date[0] == "07"):
        date = "July"
    elif (date[0] == "08"):
        date = "August"
    elif (date[0] == "09"):
        date = "September"
    elif (date[0] == "10"):
        date = "October"
    elif (date[0] == "11"):
        date = "November"
    elif (date[0] == "12"):
        date = "December"
    return render_template('profile.html', date = date + ", 2023")

def format_date_joined(date):
    # Data format Year-Month-Day
    date = str(date)

    date = date.split("-")

    return date[1], date[0]

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
