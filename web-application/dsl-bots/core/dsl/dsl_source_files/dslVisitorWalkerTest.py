from .dslVisitor import dslVisitor
from .dslParser import dslParser
from core.bot_scripts import FavRetweetListener
from core.bot_scripts import followFollowers
from core.bot_scripts import replyMentions
from core.schedule import Schedule

import tweepy


class DSLVisitorWalkerTest(dslVisitor):

    def __init__(self):
        super().__init__()
        self.kwargs = {}

    def visitTweet(self, ctx: dslParser.TweetContext):
        self.kwargs = {ctx.tweet_required_parameter().STATUS().getText(): ctx.tweet_required_parameter().stringValue().getText()}
        if ctx.tweet_optional_parameters():
            self.kwargs.update(self.getTweetOptionalParameters(ctx=ctx, kwargs=self.kwargs))

    def visitReply(self, ctx: dslParser.ReplyContext):
        self.kwargs = {ctx.reply_required_parameters().getChild(0).getText(): ctx.reply_required_parameters().getChild(2).getText(),
                  ctx.reply_required_parameters().getChild(4).getText(): ctx.reply_required_parameters().getChild(6).getText()}
        if ctx.tweet_optional_parameters():
            self.kwargs.update(self.getTweetOptionalParameters(ctx=ctx, kwargs=self.kwargs))

    def visitRetweet(self, ctx: dslParser.RetweetContext):
        self.kwargs = {ctx.retweet_required_parameter().ID().getText(): ctx.retweet_required_parameter().number().getText()}

    def visitFavourite(self, ctx: dslParser.FavouriteContext):
        self.kwargs = {ctx.favourite_required_parameter().ID().getText(): ctx.favourite_required_parameter().number().getText()}

    def visitScheduleTweet(self, ctx: dslParser.ScheduleTweetContext):
        schedule_date_time_parameters = {}
        for parameter in ctx.schedule_tweet_required_parameter().date_time_parameter().getChildren():
            if parameter.getChildCount() != 0:
                schedule_date_time_parameters[parameter.getChild(0).getText()] = parameter.getChild(2).getText()
        index_start = ctx.schedule_tweet_required_parameter().tweet().start.start
        index_end = ctx.start.getInputStream().size
        tweet_action_input = ctx.start.getInputStream().getText(start=index_start, stop=index_end)
        schedule_tweet = Schedule(schedule_date_time_parameters=schedule_date_time_parameters,
                                  action=tweet_action_input, account_id=1, campaign_id=1)

    def visitDirectMessage(self, ctx: dslParser.DirectMessageContext):
        self.kwargs = {ctx.direct_message_required_parameters().getChild(0).getText(): ctx.direct_message_required_parameters().getChild(2).getText(),
                  ctx.direct_message_required_parameters().getChild(4).getText(): ctx.direct_message_required_parameters().getChild(6).getText()}

    def visitAutoFavouriteRetweet(self, ctx:dslParser.AutoFavouriteRetweetContext):
        keywords_list = []
        for keyword in ctx.keyword():
            keywords_list.append(keyword.getChild(2).getText())
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
            keywords_list.append(keyword.getChild(2).getText())
        reply_to_mentions = replyMentions.ReplyMentions(tweepy_api=self.tweepy_api, keywords=keywords_list,
                                                        response=response, loop_time=automate_loop_time)
        reply_to_mentions.execute()

    def getTweetOptionalParameters(self, ctx, kwargs):
        for optional_parameter in ctx.tweet_optional_parameters():
            kwargs[optional_parameter.getChild(0).getText()] = optional_parameter.getChild(2).getText()
        return kwargs

    def getKwargs(self):
        return self.kwargs




