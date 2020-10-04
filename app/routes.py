from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    #TODO make a temp template for pages
    return render_template('index.html', title="home")

#login
#menu
#stock