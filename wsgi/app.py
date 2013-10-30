# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 15:03:42 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)