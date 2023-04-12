from app import app
from flask import render_template

@app.route('/')
@app.route('/sneakers')
def hello_world():
    return 'Hello World!'
    return render_template('sneakers.html')
