# Generated from dsl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dslParser import dslParser
else:
    from dslParser import dslParser

# This class defines a complete generic visitor for a parse tree produced by dslParser.

class dslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by dslParser#twitbot.
    def visitTwitbot(self, ctx:dslParser.TwitbotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#stat.
    def visitStat(self, ctx:dslParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#action.
    def visitAction(self, ctx:dslParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet.
    def visitTweet(self, ctx:dslParser.TweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet_required_parameter.
    def visitTweet_required_parameter(self, ctx:dslParser.Tweet_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet_optional_parameters.
    def visitTweet_optional_parameters(self, ctx:dslParser.Tweet_optional_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweetImage.
    def visitTweetImage(self, ctx:dslParser.TweetImageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet_image_required_parameter.
    def visitTweet_image_required_parameter(self, ctx:dslParser.Tweet_image_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#reply.
    def visitReply(self, ctx:dslParser.ReplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#reply_required_parameters.
    def visitReply_required_parameters(self, ctx:dslParser.Reply_required_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#retweet.
    def visitRetweet(self, ctx:dslParser.RetweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#retweet_required_parameter.
    def visitRetweet_required_parameter(self, ctx:dslParser.Retweet_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#favourite.
    def visitFavourite(self, ctx:dslParser.FavouriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#favourite_required_parameter.
    def visitFavourite_required_parameter(self, ctx:dslParser.Favourite_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#scheduleTweet.
    def visitScheduleTweet(self, ctx:dslParser.ScheduleTweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#schedule_tweet_required_parameter.
    def visitSchedule_tweet_required_parameter(self, ctx:dslParser.Schedule_tweet_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#date_time_parameter.
    def visitDate_time_parameter(self, ctx:dslParser.Date_time_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#minute.
    def visitMinute(self, ctx:dslParser.MinuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#hour.
    def visitHour(self, ctx:dslParser.HourContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#day_of_month.
    def visitDay_of_month(self, ctx:dslParser.Day_of_monthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#month.
    def visitMonth(self, ctx:dslParser.MonthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#numeric_month.
    def visitNumeric_month(self, ctx:dslParser.Numeric_monthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#numeric_day.
    def visitNumeric_day(self, ctx:dslParser.Numeric_dayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#numeric_hour.
    def visitNumeric_hour(self, ctx:dslParser.Numeric_hourContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#numeric_minute.
    def visitNumeric_minute(self, ctx:dslParser.Numeric_minuteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#directMessage.
    def visitDirectMessage(self, ctx:dslParser.DirectMessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#direct_message_required_parameters.
    def visitDirect_message_required_parameters(self, ctx:dslParser.Direct_message_required_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#autoFavouriteRetweet.
    def visitAutoFavouriteRetweet(self, ctx:dslParser.AutoFavouriteRetweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#autoFollowFollowers.
    def visitAutoFollowFollowers(self, ctx:dslParser.AutoFollowFollowersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#autoReplyMentions.
    def visitAutoReplyMentions(self, ctx:dslParser.AutoReplyMentionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#automateReplyParameter.
    def visitAutomateReplyParameter(self, ctx:dslParser.AutomateReplyParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#keyword.
    def visitKeyword(self, ctx:dslParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#stringValue.
    def visitStringValue(self, ctx:dslParser.StringValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#number.
    def visitNumber(self, ctx:dslParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#unary_operator.
    def visitUnary_operator(self, ctx:dslParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#unsigned_number.
    def visitUnsigned_number(self, ctx:dslParser.Unsigned_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#boolean.
    def visitBoolean(self, ctx:dslParser.BooleanContext):
        return self.visitChildren(ctx)



del dslParser