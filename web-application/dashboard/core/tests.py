import random
import string

from django.test import TestCase

from core.execute import Execute


class DSLVisitorWalkerTest(TestCase):

    def setUp(self):
        with open('core/api_keys.txt', 'r') as file:
            self.data = file.read().splitlines()
        self.consumer_key, self.consumer_secret_key, self.access_token, self.access_token_secret = [i for i in self.data]

    def test_tweet(self):
        execute = Execute(consumer_key=self.consumer_key, consumer_secret_key=self.consumer_secret_key, access_token=self.access_token, access_token_secret=self.access_token_secret)
        api = execute.tweepy_auth()
        input_statement = 'tweet status : "This is a Unit Test with random string: %s " ;' % ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        parser = execute.build_lexer_parser(input_statement=input_statement)
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree, api=api)