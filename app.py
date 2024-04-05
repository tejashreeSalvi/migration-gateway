from flask import Flask
from flask_restx import Api
from src.controller.bitbucket_controller import bitbucket_api
from flask_cors import CORS
app = Flask(__name__)

api = Api(app, version='1.0', title='MA API GATE-WAY', description='MA operations')
cors = CORS(app, resources={r"*": {"origins": ["http://localhost:3000"]}})  # Replace with your React app's origin

# Add the bitbucket API to the app
api.add_namespace(bitbucket_api, path='/BB')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5100, debug=True)
