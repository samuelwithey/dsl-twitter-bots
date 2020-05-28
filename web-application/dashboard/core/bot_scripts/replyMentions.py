import tweepy
import logging
import time

from datetime import datetime
from datetime import timedelta

logging.basicConfig(level=logging.INFO)


class ReplyMentions:

    def __init__(self, tweepy_api, keywords, response, loop_time):
        self.tweepy_api = tweepy_api
        self.keywords = keywords
        self.response = response
        self.loop_time = loop_time
        self.logger = logging.getLogger()
        self.date_time_start = datetime.now()

    def execute(self):
        latest_mention = self.tweepy_api.mentions_timeline(count=1)
        since_id = latest_mention[0].id
        while datetime.now() < (self.date_time_start + timedelta(minutes=self.loop_time)):
            since_id = self.check_mentions(keywords=self.keywords, since_id=since_id)
            self.logger.info("Waiting...")
            time.sleep(30)

    def check_mentions(self, keywords, since_id):
        self.logger.info("Retrieving mentions")
        new_since_id = since_id
        for tweet in tweepy.Cursor(self.tweepy_api.mentions_timeline,
                                   since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            if any(keyword in tweet.text.lower() for keyword in keywords):
                self.logger.info(f"Answering to {tweet.user.name}")

                if not tweet.user.following:
                    tweet.user.follow()

                default_response = "Hello @%s, " % tweet.user.screen_name
                response = default_response + self.response

                self.tweepy_api.update_status(
                    status=response,
                    in_reply_to_status_id=tweet.id,
                )
        return new_since_id
