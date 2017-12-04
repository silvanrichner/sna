import twitter
import json
import time

class MultiUserAPI:
    def getAPI(self):
        if (self.current_request_count >= 15):
            self.current_token += 1

            if (self.current_token >= len(self.tokens)):
                time.sleep(15 * 60)
                self.current_token = 0

            self.switchUser(self.current_token)
            self.current_request_count = 0

        self.current_request_count += 1

        return self.api

    def switchUser(self, new_token):
        self.api = twitter.Api(consumer_key=self.tokens[new_token]['consumer_key'],
                               consumer_secret=self.tokens[new_token]['consumer_secret'],
                               access_token_key=self.tokens[new_token]['access_token_key'],
                               access_token_secret=self.tokens[new_token]['access_token_secret'])

    def __init__(self):
        self.tokens = json.load(open('api_tokens.json'))
        self.current_token = 0
        self.current_request_count = 0
        self.switchUser(self.current_token)
