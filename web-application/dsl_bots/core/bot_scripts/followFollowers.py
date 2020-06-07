import tweepy
import logging

logging.basicConfig(level=logging.INFO)


class FollowFollowers:

    def __init__(self, tweepy_api):
        self.tweepy_api = tweepy_api
        self.logger = logging.getLogger()

    def follow_followers(self):
        self.logger.info("Retrieving and following followers")
        for follower in tweepy.Cursor(self.tweepy_api.followers).items():
            if not follower.following:
                self.logger.info(f"Following {follower.name}")
                follower.follow()
