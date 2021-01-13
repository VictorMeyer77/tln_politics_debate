import tweepy
import os

class TweeterApi:

    def __init__(self, username, dataDir, tweeterToken, side):

        self.consumerKey = tweeterToken["consumer_key"]
        self.consumerSecret = tweeterToken["consumer_secret"]
        self.accessToken = tweeterToken["access_token"]
        self.accessTokenSecret = tweeterToken["access_token_secret"]
        self.username = username
        self.output = os.path.join(dataDir, side, self.username[1:] + ".txt")
        self.api = None

    def setApi(self):
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
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
