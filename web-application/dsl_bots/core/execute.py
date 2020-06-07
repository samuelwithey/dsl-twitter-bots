import tweepy
import logging
from core.dsl.dsl_source_files.dslLexer import dslLexer
from core.dsl.dsl_source_files.dslParser import dslParser
from core.dsl.dsl_source_files.dslVisitorWalker import DSLVisitorWalker
from antlr4 import *
from django.conf import settings


class Execute:

    def __init__(self, account=None, campaign=None, consumer_key=None, consumer_secret_key=None, access_token=None,
                 access_token_secret=None):
        if (account and campaign) is not None:
            self.account = account
            self.campaign = campaign
        else:
            self.account = None
            self.campaign = None
        self.consumer_key = consumer_key
        self.consumer_secret_key = consumer_secret_key
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.logger = logging.getLogger()

    def get_consumer_key(self):
        if self.account is None:
            return self.consumer_key
        else:
            return self.account.consumer_key

    def get_consumer_secret_key(self):
        if self.account is None:
            return self.consumer_secret_key
        else:
            return self.account.consumer_secret_key

    def get_access_token(self):
        if self.account is None:
            return self.access_token
        else:
            return self.account.access_token

    def get_access_token_secret(self):
        if self.account is None:
            return self.access_token_secret
        else:
            return self.account.access_token_secret

    def tweepy_auth(self):
        auth = tweepy.OAuthHandler(self.get_consumer_key(), self.get_consumer_secret_key())
        auth.set_access_token(self.get_access_token(), self.get_access_token_secret())
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
        except Exception as e:
            self.logger.error("Error creating API", exc_info=True)
            raise e
        return api

    def build_lexer_parser(self, input_statement=""):
        if not input_statement:
            input_stream = FileStream(self.get_user_filename())
        else:
            input_stream = InputStream(input_statement)
        lexer = dslLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = dslParser(token_stream)
        return parser

    def build_tree(self, parser):
        return parser.twitbot()

    def traverse_tree(self, tree, api):
        if (self.account or self.campaign) is None:
            visitor = DSLVisitorWalker(tweepy_api=api)
        else:
            visitor = DSLVisitorWalker(tweepy_api=api, account=self.account, campaign=self.campaign)
        visitor.visit(tree)

    def get_user_filename(self):
        return settings.MEDIA_ROOT + "/" + self.campaign.dsl_program_upload.name
