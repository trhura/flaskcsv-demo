# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 14:59:36 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app = Bootstrap(app)

@app.route('/')
@app.route('/hello')
def index():
    return "Hello from OpenShift"

if __name__ == '__main__':
    app.run(debug=True)