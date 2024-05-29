from flask import render_template

def index():
    return render_template('index.html')

def about():
    return render_template('about.html')

def inbody():
    return render_template('inbody.html')

def page_not_found(e):
    return render_template('404.html'), 404
