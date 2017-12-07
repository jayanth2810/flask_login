__author__ = 'jayanthvenkataraman'

from flask import Flask
import os

app = Flask(__name__)


@app.route('/login', methods = ['GET'])
def login_function():
    return "JWT"

@app.route('/users/<jwt>', methods = ['GET'])
def grab_id_function(jwt):
    return "1234"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) #for taking Heroku's PORT environment variable
    app.run(host='0.0.0.0', port=port)