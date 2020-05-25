from .dslVisitor import dslVisitor
from .dslParser import dslParser
from core.bot_scripts import FavRetweetListener
from core.bot_scripts import followFollowers
from core.bot_scripts import replyMentions
import tweepy


class DSLVisitorWalker(dslVisitor):

    def __init__(self, tweepy_api):
        super().__init__()
        self.tweepy_api = tweepy_api

    def visitTweet(self, ctx: dslParser.TweetContext):
        kwargs = {ctx.tweet_required_parameter().STATUS().getText(): ctx.tweet_required_parameter().stringValue().getText()}
        if ctx.tweet_optional_parameters():
            kwargs.update(self.getTweetOptionalParameters(ctx=ctx, kwargs=kwargs))
        self.tweepy_api.update_status(**kwargs)

    def visitReply(self, ctx: dslParser.ReplyContext):
        kwargs = {ctx.reply_required_parameters().getChild(0).getText(): ctx.reply_required_parameters().getChild(2).getText(),
                  ctx.reply_required_parameters().getChild(4).getText(): ctx.reply_required_parameters().getChild(6).getText()}
        if ctx.tweet_optional_parameters():
            kwargs.update(self.getTweetOptionalParameters(ctx=ctx, kwargs=kwargs))
        self.tweepy_api.update_status(**kwargs)

    def visitRetweet(self, ctx: dslParser.RetweetContext):
        kwargs = {ctx.retweet_required_parameter().ID().getText(): ctx.retweet_required_parameter().number().getText()}
        self.tweepy_api.retweet(**kwargs)

    def visitFavourite(self, ctx: dslParser.FavouriteContext):
        kwargs = {ctx.favourite_required_parameter().ID().getText(): ctx.favourite_required_parameter().number().getText()}
        self.tweepy_api.create_favorite(**kwargs)

    def visitSchedule(self, ctx: dslParser.ScheduleTweetContext):
        pass

    def visitDirectMessage(self, ctx: dslParser.DirectMessageContext):
        kwargs = {ctx.direct_message_required_parameters().getChild(0).getText(): ctx.direct_message_required_parameters().getChild(2).getText(),
                  ctx.direct_message_required_parameters().getChild(4).getText(): ctx.direct_message_required_parameters().getChild(6).getText()}
        self.tweepy_api.send_direct_message(**kwargs)

    def visitAutoFavouriteRetweet(self, ctx:dslParser.AutoFavouriteRetweetContext):
        keywords_list = []
        for keyword in ctx.keyword():
            keywords_list.append(keyword.getChild(2))
        tweets_listener = FavRetweetListener.FavRetweetListener(self.tweepy_api)
        stream = tweepy.Stream(self.tweepy_api.auth, tweets_listener)
        stream.filter(track=keywords_list, languages=["en"])

    def visitAutoFollowFollowers(self, ctx:dslParser.AutoFollowFollowersContext):
        follow_followers = followFollowers.FollowFollowers(tweepy_api=self.tweepy_api)
        follow_followers.follow_followers()

    def visitAutoReplyMentions(self, ctx:dslParser.AutoReplyMentionsContext):
        automate_loop_time = int(ctx.automateReplyParameter().getChild(2).getText())
        response = ctx.automateReplyParameter().getChild(6).getText()
        keywords_list = []
        for keyword in ctx.keyword():
            keywords_list.append(keyword.getChild(2))
        reply_to_mentions = replyMentions.ReplyMentions(tweepy_api=self.tweepy_api, keywords=keywords_list,
                                                        response=response, loop_time=automate_loop_time)
        reply_to_mentions.execute()

    def getTweetOptionalParameters(self, ctx, kwargs):
        for optional_parameter in ctx.tweet_optional_parameters():
            kwargs[optional_parameter.getChild(0).getText()] = optional_parameter.getChild(2).getText()
        return kwargs




