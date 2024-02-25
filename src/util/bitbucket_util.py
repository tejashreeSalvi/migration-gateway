import requests

class BitbucketUtil:
    @staticmethod
    def bitbucketApi(api_url, payload):
        # Make a request to the existing API
        response = requests.get(api_url, json=payload)
        return response.json()
