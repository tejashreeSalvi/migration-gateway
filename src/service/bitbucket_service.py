from src.util.bitbucket_util import BitbucketUtil
from flask import current_app
from settings import BITBUCKET_API_URL

class BitbucketService:
    @staticmethod
    def bitbucket_migration(payload):
        # business logic
        # forwarding the payload to the util function
        api_url = BITBUCKET_API_URL
        return BitbucketUtil.bitbucketApi(api_url, payload)
