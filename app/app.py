__author__ = 'jayanthvenkataraman'

from flask import Flask
import os
import json

app = Flask(__name__)


@app.route('/login', methods = ['GET'])
def login_function():
    result = {"data": "JWT"}
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users/', methods = ['GET'])
def grab_id_function():
    result = {"data": "1234"}
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) #for taking Heroku's PORT environment variable
    app.run(host='0.0.0.0', port=port)