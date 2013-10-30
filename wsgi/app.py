# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 16:19:04 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flask import request
import csv

app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        message = None

        file = request.files.get('file', None)
        if not file:
            message = "Csv file not attached."
        else:
            csvReader = csv.reader(file, delimiter=",")
            message = ""
            for row in csvReader:
                message += " ".join(row)

        kwargs = {
            'message' : message
        }

        return render_template('result.html', **kwargs)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)