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

    def visitReply(self, ctx:dslParser.ReplyContext):
        kwargs = {}
        for required_param in ctx.reply_required_parameter():
            kwargs[required_param.reply_parameter().getText()] = required_param.reply_parameter.value().getText()
        for optional_param in ctx.tweet_optional_parameter():
            kwargs[optional_param.tweet_parameter().getText()] = optional_param.value().getText()
        self.tweepy_api.update_status(**kwargs)

    def visitRetweet(self, ctx:dslParser.RetweetContext):
        kwargs = {ctx.retweet_required_parameter().retweet_id().getText(): ctx.retweet_required_parameter().value().getText()}
        self.tweepy_api.retweet(**kwargs)

    def visitFavourite(self, ctx:dslParser.FavouriteContext):
        kwargs = {ctx.favourite_required_parameter().account_id().getText(): ctx.favourite_required_parameter().value().getText()}
        self.tweepy_api.create_favorite(**kwargs)

    def visitSchedule(self, ctx:dslParser.ScheduleContext):
        pass

    def visitDirect_message(self, ctx:dslParser.Direct_messageContext):
        kwargs = {}
        for required_param in ctx.direct_message_required_parameter():
            kwargs[required_param.direct_message_parameter().getText()] = required_param.direct_message_parameter.value().getText()
        self.tweepy_api.send_direct_message(**kwargs)



