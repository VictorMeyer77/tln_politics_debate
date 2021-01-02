import tweepy


class TweeterApi:

    def __init__(self, username, dataDir):

        self.consumer_key = "Q9PkzmmwZtqgddfmEitAn7ocz"
        self.consumer_secret = "SyqkVvR89sQpVknc9e2coyq4qbWcaa60DJvdFOnMvHMJVXwZBW"
        self.access_token = "332892034-ahTEwLC4EaIT7KfzzoR7w1M0dwLkNO2Z6SgSMomE"
        self.access_token_secret = "LS9Vyb9vYPCObwpnFTvSRHCyGf8e9gc6ugIUMRUrZZURG"
        self.username = username
        self.output = dataDir + "/" + self.username[1:] + ".txt"
        self.api = None

    def setApi(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def getTweetsList(self):

        tweets = []

        for status in tweepy.Cursor(self.api.user_timeline,
                                    screen_name=self.username,
                                    include_rts=True,
                                    tweet_mode="extended").items():
            if "…" not in status.full_text:
                tweets.append(status.full_text)

        return tweets

    def write(self, tweets):

        file = open(self.output, "w+")
        for tweet in tweets:
            try:
                file.write(tweet)
            except Exception as e:
                print("WARNING: Impossible de sauvegarder: " + tweet)

        file.close()

    def run(self):

        self.setApi()
        tweets = self.getTweetsList()
        self.write(tweets)
        print("INFO: Tweets de {} téléchargés avec succès.".format(self.username))
