from .dslVisitor import dslVisitor
from .dslParser import dslParser


class DSLVisitorWalker(dslVisitor):

    def __init__(self, tweepy_api):
        super().__init__()
        self.tweepy_api = tweepy_api

    def visitTweet(self, ctx:dslParser.TweetContext):
        kwargs = {}
        kwargs[ctx.tweet_required_parameter().status().getText()] = ctx.tweet_required_parameter().value().getText()
        for optional_param in ctx.tweet_optional_parameter():
            kwargs[optional_param.tweet_parameter().getText()] = optional_param.value().getText()
        self.tweepy_api.update_status(**kwargs)
        return self.visitChildren(ctx)
