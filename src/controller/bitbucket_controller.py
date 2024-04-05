from flask_restx import Namespace, Resource, reqparse
from flask import jsonify
from src.service.chatbot import ChatbotService

bitbucket_api = Namespace('BB', description='BB operations')
    
@bitbucket_api.route("/hello")
class bitbucketHealthCheck(Resource):
    
    def get(self):
        print("Hello Bitbucket!!!")
        return "Migration Successful!!!", 200

@bitbucket_api.route("/chatbot")
class bitbucketChatbot(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('text', type=str, required=False, help='User Input')
    @bitbucket_api.expect(parser)
    def post(self):
        print("Chatbot processing...")
        args = self.parser.parse_args()
        return ChatbotService().chatbot_conversation(args['text'])
        
        