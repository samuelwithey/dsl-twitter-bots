import random
import string
import tweepy
import time

from django.test import TestCase
import logging

from core.execute import Execute


class ConfigureTests(TestCase):

    def setUp(self):
        with open('core/api_keys.txt', 'r') as file:
            self.data = file.read().splitlines()
        self.consumer_key, self.consumer_secret_key, self.access_token, self.access_token_secret = [i for i in self.data]
        self.logger = logging.getLogger()

    def execute(self, input_statement):
        execute = Execute(consumer_key=self.consumer_key, consumer_secret_key=self.consumer_secret_key,
                          access_token=self.access_token, access_token_secret=self.access_token_secret)
        api = execute.tweepy_auth()
        parser = execute.build_lexer_parser(input_statement=input_statement)
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree, api=api)

    def get_tweepy_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret_key)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
        except Exception as e:
            self.logger.error("Error creating API", exc_info=True)
            raise e
        return api

    def generate_random_string(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))


class DSLVisitorWalkerTest(ConfigureTests):

    def test_tweet(self):
        input_statement = 'tweet status : "This is a Unit Test with random string: %s" ;' % self.generate_random_string()
        self.execute(input_statement=input_statement)

    def test_tweet_optional_parameters(self):
        input_statement = """
        tweet 
            status : "This is a Unit Test with random string: %s",
            possibly_sensitive : True,
            lat: 50.834400,
            long: -0.130240;""" % self.generate_random_string()
        self.execute(input_statement=input_statement)

    def test_reply_to_tweet(self):
        api = self.get_tweepy_api()
        latest_mention = api.mentions_timeline(count=1)
        reply_id = latest_mention[0].id
        username = latest_mention[0].user.screen_name
        input_statement = 'reply in_reply_to_status_id : %s, status : "Hello @%s, Random Reply %s";' % (reply_id, username,
                                                                                             self.generate_random_string())
        self.execute(input_statement=input_statement)

    def test_retweet(self):
        time.sleep(5)
        api = self.get_tweepy_api()
        timeline_tweet = api.user_timeline(count=1)
        print(timeline_tweet)
        tweet_id = timeline_tweet[0].id
        input_statement = 'retweet id : %s ;' % tweet_id
        self.execute(input_statement=input_statement)

    def test_favourite(self):
        time.sleep(5)
        api = self.get_tweepy_api()
        timeline_tweet = api.user_timeline(count=1)
        print(timeline_tweet)
        tweet_id = timeline_tweet[0].id
        input_statement = 'favourite id : %s ;' % tweet_id
        self.execute(input_statement=input_statement)

    def test_schedule_tweet(self):
        pass

    def test_direct_message(self):
        input_statement = 'direct_message recipient_id : %s, text : "Hello Friend!" ;' % '1050149543029948416'
        self.execute(input_statement=input_statement)


class BotScriptTest(ConfigureTests):
    def test_reply_mentions_bot(self):
        input_statement = 'automate_reply_to_mentions automate_time_minutes : 01, response : "Please Reach us via DM", keyword : "support";'
        self.execute(input_statement=input_statement)

    def test_follow_followers_bot(self):
        input_statement = 'follow_all_followers;'
        self.execute(input_statement=input_statement)

    def test_fav_retweet_listener(self):
        input_statement = 'automate_favourites_retweets keyword : "Python", keyword : "Computer Science", keyword : "Twitter API" ;'
        self.execute(input_statement=input_statement)
