from flask_restplus import Namespace, Resource, reqparse
from flask import jsonify
from src.service.bitbucket_service import BitbucketService

bitbucket_api = Namespace('BB', description='BB operations')

@bitbucket_api.route('/BBmigration')
class CreateProject(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('bitbucketserverurl', type=str, required=True, help='Bitbucket Server URL')
    parser.add_argument('bitbucketcloudurl', type=str, required=True, help='Bitbucket Cloud URL')
    parser.add_argument('username', type=str, required=True, help='Bitbucket Server username')
    parser.add_argument('password', type=str, required=True, help='Bitbucket Server password')
    parser.add_argument('cloudworkspace', type=str, required=True, help='Bitbucket Cloud workspace')
    parser.add_argument('cloudauthusername', type=str, required=True, help='Bitbucket Cloud username')
    parser.add_argument('cloudauthpassword', type=str, required=True, help='Bitbucket Cloud password')

    @bitbucket_api.doc('BBmigration')
    @bitbucket_api.expect(parser)
    def get(self):
        args = self.parser.parse_args()

        # payload for the service
        payload = {
            'bitbucketserverurl': args['bitbucketserverurl'],
            'bitbucketcloudurl': args['bitbucketcloudurl'],
            'username': args['username'],
            'password': args['password'],
            'cloudworkspace': args['cloudworkspace'],
            'cloudauthusername': args['cloudauthusername'],
            'cloudauthpassword': args['cloudauthpassword']
        }

        # Calling the service to handle the logic
        response = BitbucketService.bitbucket_migration(payload)

        # Return the response
        return jsonify(response)
