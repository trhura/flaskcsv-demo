# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-10-30 17:00:16 (trhura)>

__author__ = "Thura Hlaing <trhura@gmail.com>"

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flask import request
from flask import send_file

import csv
import tempfile
import random

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
            csvReader = csv.reader(file,delimiter=",")

            with tempfile.NamedTemporaryFile(mode="w") as oFile:
                csvWriter = csv.writer(oFile,delimiter=",")
                for row in csvReader:
                    csvWriter.writerow(row + ['09-731 558 ' + str(random.randint(111,999)) ])
                oFile.flush()
                oFile.seek(0,0)

                return send_file(oFile.name, mimetype='text/csv')

        kwargs = {
            'message' : message
        }

        return render_template('result.html', **kwargs)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)