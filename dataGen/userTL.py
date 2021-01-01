import tweepy

class UserTL:

    def __init__(self, username, api, dataDir):
        self.username = username
        self.api = api
        self.output = dataDir + "/" + self.username[1:] + ".txt"

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
            file.write(tweet)
        file.close()

    def run(self):

        tweets = self.getTweetsList()
        self.write(tweets)