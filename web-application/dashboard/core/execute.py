import tweepy
from core.dsl.dsl_source_files.dslLexer import dslLexer
from core.dsl.dsl_source_files.dslParser import dslParser
from core.dsl.dsl_source_files.dslListener import dslListener
from core.dsl.dsl_source_files.dslVisitorWalker import DSLVisitorWalker
import sys
import os
from antlr4 import *
from django.conf import settings


class Execute:

    def __init__(self, account, campaign):
        self.account = account
        self.campaign = campaign

    def get_consumer_key(self, account):
        return account.consumer_key

    def get_consumer_secret_key(self, account):
        return account.consumer_secret_key

    def get_access_token(self, account):
        return account.access_token

    def get_access_token_secret(self, account):
        return account.access_token_secret

    def tweepy_auth(self):
        auth = tweepy.OAuthHandler(self.get_consumer_key(self.account), self.get_consumer_secret_key(self.account))
        auth.set_access_token(self.get_access_token(account=self.account), self.get_access_token_secret(account=self.account))
        return tweepy.API(auth)

    def build_lexer_parser(self):
        input_stream = FileStream(self.get_user_filename())
        print(input_stream)
        lexer = dslLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = dslParser(token_stream)
        tree = parser.twitbot()
        visitor = DSLVisitorWalker(self.tweepy_auth())
        visitor.visit(tree)
        # self.build_tree(parser=parser)

    def build_tree(self, parser):
        tree = parser.twitbot()
        lisp_tree_str = tree.toStringTree(recog=parser)
        print(lisp_tree_str)

    def get_user_filename(self):
        return settings.MEDIA_ROOT + "/" + self.campaign.upload.name
