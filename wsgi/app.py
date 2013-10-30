# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 14:51:52 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
    return "Hello from OpenShift"

if __name__ == '__main__':
    app.run()