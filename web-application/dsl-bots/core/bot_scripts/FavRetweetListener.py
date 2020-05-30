import tweepy
import logging
import json

logging.basicConfig(level=logging.INFO)


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.logger = logging.getLogger()

    def on_status(self, tweet):
        self.logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                self.logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                self.logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        self.logger.error(status)
