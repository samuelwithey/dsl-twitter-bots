import time
import datetime
import tweepy
import logging
from datetime import timedelta
from antlr4 import *
from django.test import TestCase
from core.dsl.dsl_source_files.dslLexer import dslLexer
from core.dsl.dsl_source_files.dslParser import dslParser
from core.dsl.dsl_source_files.dslVisitorWalkerTest import DSLVisitorWalkerTest
from core.execute import Execute
from dsl_bots.test_utils import generate_random_string


class ConfigureTests(TestCase):

    def setUp(self):
        with open('core/api_keys.txt', 'r') as file:
            self.data = file.read().splitlines()
        self.consumer_key, self.consumer_secret_key, self.access_token, self.access_token_secret = [i for i in self.data]
        self.logger = logging.getLogger()
        self.api = self.get_tweepy_api()

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


class DSLExecuteTests(ConfigureTests):

    def execute(self, input_statement):
        execute = Execute(consumer_key=self.consumer_key, consumer_secret_key=self.consumer_secret_key,
                          access_token=self.access_token, access_token_secret=self.access_token_secret)
        api = execute.tweepy_auth()
        parser = execute.build_lexer_parser(input_statement=input_statement)
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree, api=api)

    def get_most_recent_user_timeline_tweet(self):
        return self.api.user_timeline(count=1)

    def get_most_recent_user_mention(self):
        return self.api.mentions_timeline(count=1)

    def get_most_recent_direct_message(self):
        return self.api.list_direct_messages(count=1)


class DSLTest(TestCase):

    def execute(self, input_statement):
        input_stream = InputStream(input_statement)
        lexer = dslLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = dslParser(token_stream)
        tree = parser.twitbot()
        visitor = DSLVisitorWalkerTest()
        visitor.visit(tree)
        return visitor.getKwargs()

    def test_tweet(self):
        tweet_dict = {'status': 'hello test'}
        input_statement = 'tweet status : "%s";' % tweet_dict.get('status')
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(tweet_dict, kwargs)

    def test_tweet_optional_parameters(self):
        tweet_dict = {'status': 'hello test', 'possibly_sensitive': 'True', 'lat': '50.834400',
                      'long': '-0.130240'}
        input_statement = """
        tweet 
            status : "%s",
            possibly_sensitive : %s,
            lat : %s,
            long : %s
            ;        
        """ % (tweet_dict.get('status'), tweet_dict.get('possibly_sensitive'), tweet_dict.get('lat'),
               tweet_dict.get('long'))
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(tweet_dict, kwargs)

    def test_favourite(self):
        favourite_dict = {'id': '124123453324'}
        input_statement = "favourite id : %s ;" % favourite_dict.get('id')
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(favourite_dict, kwargs)

    def test_retweet(self):
        retweet_dict = {'id': '124123453324'}
        input_statement = "retweet id : %s ;" % retweet_dict.get('id')
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(retweet_dict, kwargs)

    def test_reply_to_tweet(self):
        reply_dict = {'in_reply_to_status_id': '231312513434', 'status': 'Replying to user'}
        input_statement = 'reply_to_tweet in_reply_to_status_id : %s, status : "%s";' % (reply_dict.get('in_reply_to_status_id'),
                                                                                reply_dict.get('status'))
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(reply_dict, kwargs)

    def test_direct_message(self):
        direct_message_dict = {'recipient_id': '231312513434', 'text': 'Hello Friend!'}
        input_statement = 'direct_message recipient_id : %s, text : "%s" ;' % (direct_message_dict.get('recipient_id')
                                                                               , direct_message_dict.get('text'))
        kwargs = self.execute(input_statement=input_statement)
        self.assertDictEqual(direct_message_dict, kwargs)


class DSLVisitorWalkerAPITests(DSLExecuteTests):

    def test_tweet(self):
        status = 'This is a Unit Test with random string: %s' % generate_random_string()
        input_statement = 'tweet status : "%s" ;' % status
        self.execute(input_statement=input_statement)
        tweet = self.get_most_recent_user_timeline_tweet()[0]
        self.assertEqual(tweet.text, status)

    def test_retweet(self):
        time.sleep(3)
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
        input_statement = 'reply_to_tweet in_reply_to_status_id : %s, status : "Hello @%s, Random Reply %s";' % (reply_id, username,
                                                                                             generate_random_string())
        self.execute(input_statement=input_statement)
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertEqual(reply_id, timeline_tweet[0].in_reply_to_status_id)

    def test_tweet_optional_parameters(self):
        input_statement = """
        tweet 
            status : "This is a Unit Test with random string: %s",
            possibly_sensitive : True,
            lat: 50.834400,
            long: -0.130240;""" % generate_random_string()
        self.execute(input_statement=input_statement)
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertTrue(timeline_tweet[0].place.name, "Brighton")

    def test_direct_message(self):
        recipient_id = '1050149543029948416'
        text = 'Hello Friend! % s' % generate_random_string()
        input_statement = 'direct_message recipient_id : %s, text : "%s" ;' % (recipient_id, text)
        self.execute(input_statement=input_statement)
        direct_message = self.get_most_recent_direct_message()
        self.assertTrue(recipient_id, direct_message[0].message_create.get('target').get('recipient_id'))
        self.assertTrue(text, direct_message[0].message_create.get("message_data").get("text"))

    def test_schedule_tweet(self):
        timeline_tweet = self.get_most_recent_user_timeline_tweet()
        schedule_time = datetime.datetime.now() + timedelta(minutes=1)
        tweet_status = 'hello world %s' % generate_random_string()
        input_statement = 'schedule minute : %s, hour : %s, day_of_month : %s, month : %s, tweet status : "%s" ;' \
                          % (schedule_time.minute, schedule_time.hour, schedule_time.day, schedule_time.month, tweet_status)
        self.execute(input_statement=input_statement)
        self.assertNotEqual(tweet_status, timeline_tweet[0].text)
        time.sleep(60)
        updated_timeline_tweet = self.get_most_recent_user_timeline_tweet()
        self.assertEqual(tweet_status, updated_timeline_tweet[0].text)


class BotScriptTest(DSLExecuteTests):
    def test_reply_mentions_bot(self):
        input_statement = 'automate_reply_to_mentions automate_time_minutes : 01, response : "Please Reach us via DM", keyword : "support";'
        self.execute(input_statement=input_statement)

    def test_follow_followers_bot(self):
        input_statement = 'follow_all_followers;'
        self.execute(input_statement=input_statement)

    def test_fav_retweet_listener(self):
        input_statement = 'automate_favourites_retweets keyword : "Python", keyword : "Computer Science", keyword : "Twitter API" ;'
        self.execute(input_statement=input_statement)
