from flask import Flask
from flask_restplus import Api
from src.controller.bitbucket_controller import bitbucket_api

app = Flask(__name__)

api = Api(app, version='1.0', title='Bitbucket API', description='Bitbucket operations')

# Add the bitbucket API to the app
api.add_namespace(bitbucket_api, path='/bitbucket')


if __name__ == '__main__':
    app.run(debug=True,port=5100)
