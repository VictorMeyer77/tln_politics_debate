import tweepy

class TweeterApi:

    def __init__(self):

        self.consumer_key = "Q9PkzmmwZtqgddfmEitAn7ocz"
        self.consumer_secret = "SyqkVvR89sQpVknc9e2coyq4qbWcaa60DJvdFOnMvHMJVXwZBW"
        self.access_token = "332892034-ahTEwLC4EaIT7KfzzoR7w1M0dwLkNO2Z6SgSMomE"
        self.access_token_secret = "LS9Vyb9vYPCObwpnFTvSRHCyGf8e9gc6ugIUMRUrZZURG"
        self.api = None

    def setApi(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def getApi(self):

        if self.api is None:
            self.setApi()
        return self.api