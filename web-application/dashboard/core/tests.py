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
        self.api = self.get_tweepy_api()

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

    def get_most_recent_user_timeline_tweet(self):
        return self.api.user_timeline(count=1)

    def get_most_recent_user_mention(self):
        return self.api.mentions_timeline(count=1)

    def get_most_recent_direct_message(self):
        return self.api.list_direct_messages(count=1)


class DSLVisitorWalkerTest(ConfigureTests):

    def test_tweet(self):
        status = 'This is a Unit Test with random string: %s' % self.generate_random_string()
        input_statement = 'tweet status : "%s" ;' % status
        self.execute(input_statement=input_statement)
        tweet = self.get_most_recent_user_timeline_tweet()[0]
        self.assertEqual(tweet.text, status)

    def test_retweet(self):
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertFalse(timeline_tweet[0].retweeted)
        input_statement = 'retweet id : %s ;' % timeline_tweet[0].id
        self.execute(input_statement=input_statement)
        updated_timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertTrue(updated_timeline_tweet[0].retweeted)

    def test_favourite(self):
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertFalse(timeline_tweet[0].favorited)
        input_statement = 'favourite id : %s ;' % timeline_tweet[0].id
        self.execute(input_statement=input_statement)
        updated_timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertTrue(updated_timeline_tweet[0].favorited)

    def test_reply_to_tweet(self):
        api = self.get_tweepy_api()
        latest_mention = api.mentions_timeline(count=1)
        reply_id = latest_mention[0].id
        username = latest_mention[0].user.screen_name
        input_statement = 'reply in_reply_to_status_id : %s, status : "Hello @%s, Random Reply %s";' % (reply_id, username,
                                                                                             self.generate_random_string())
        self.execute(input_statement=input_statement)
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertEqual(reply_id, timeline_tweet[0].in_reply_to_status_id)

    def test_tweet_optional_parameters(self):
        input_statement = """
        tweet 
            status : "This is a Unit Test with random string: %s",
            possibly_sensitive : True,
            lat: 50.834400,
            long: -0.130240;""" % self.generate_random_string()
        self.execute(input_statement=input_statement)
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertTrue(timeline_tweet[0].place.name, "Brighton")

    def test_schedule_tweet(self):
        pass

    def test_direct_message(self):
        recipient_id = '1050149543029948416'
        text = 'Hello Friend! % s' % self.generate_random_string()
        input_statement = 'direct_message recipient_id : %s, text : "%s" ;' % (recipient_id, text)
        self.execute(input_statement=input_statement)
        direct_message = self.get_most_recent_direct_message()
        self.assertTrue(recipient_id, direct_message[0].message_create.get('target').get('recipient_id'))
        self.assertTrue(text, direct_message[0].message_create.get("message_data").get("text"))


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
