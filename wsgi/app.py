# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 15:58:18 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flask import request

app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        #print 'yes', request.form
        email = request.form['email']
        return render_template('result.html', email=email)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)