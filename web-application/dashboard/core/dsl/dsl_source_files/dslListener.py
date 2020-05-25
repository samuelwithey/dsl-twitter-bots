# Generated from dsl.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dslParser import dslParser
else:
    from dslParser import dslParser

# This class defines a complete listener for a parse tree produced by dslParser.
class dslListener(ParseTreeListener):

    # Enter a parse tree produced by dslParser#twitbot.
    def enterTwitbot(self, ctx:dslParser.TwitbotContext):
        pass

    # Exit a parse tree produced by dslParser#twitbot.
    def exitTwitbot(self, ctx:dslParser.TwitbotContext):
        pass


    # Enter a parse tree produced by dslParser#stat.
    def enterStat(self, ctx:dslParser.StatContext):
        pass

    # Exit a parse tree produced by dslParser#stat.
    def exitStat(self, ctx:dslParser.StatContext):
        pass


    # Enter a parse tree produced by dslParser#action.
    def enterAction(self, ctx:dslParser.ActionContext):
        pass

    # Exit a parse tree produced by dslParser#action.
    def exitAction(self, ctx:dslParser.ActionContext):
        pass


    # Enter a parse tree produced by dslParser#tweet.
    def enterTweet(self, ctx:dslParser.TweetContext):
        pass

    # Exit a parse tree produced by dslParser#tweet.
    def exitTweet(self, ctx:dslParser.TweetContext):
        pass


    # Enter a parse tree produced by dslParser#tweet_required_parameter.
    def enterTweet_required_parameter(self, ctx:dslParser.Tweet_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#tweet_required_parameter.
    def exitTweet_required_parameter(self, ctx:dslParser.Tweet_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#tweet_optional_parameters.
    def enterTweet_optional_parameters(self, ctx:dslParser.Tweet_optional_parametersContext):
        pass

    # Exit a parse tree produced by dslParser#tweet_optional_parameters.
    def exitTweet_optional_parameters(self, ctx:dslParser.Tweet_optional_parametersContext):
        pass


    # Enter a parse tree produced by dslParser#reply.
    def enterReply(self, ctx:dslParser.ReplyContext):
        pass

    # Exit a parse tree produced by dslParser#reply.
    def exitReply(self, ctx:dslParser.ReplyContext):
        pass


    # Enter a parse tree produced by dslParser#reply_required_parameters.
    def enterReply_required_parameters(self, ctx:dslParser.Reply_required_parametersContext):
        pass

    # Exit a parse tree produced by dslParser#reply_required_parameters.
    def exitReply_required_parameters(self, ctx:dslParser.Reply_required_parametersContext):
        pass


    # Enter a parse tree produced by dslParser#retweet.
    def enterRetweet(self, ctx:dslParser.RetweetContext):
        pass

    # Exit a parse tree produced by dslParser#retweet.
    def exitRetweet(self, ctx:dslParser.RetweetContext):
        pass


    # Enter a parse tree produced by dslParser#retweet_required_parameter.
    def enterRetweet_required_parameter(self, ctx:dslParser.Retweet_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#retweet_required_parameter.
    def exitRetweet_required_parameter(self, ctx:dslParser.Retweet_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#favourite.
    def enterFavourite(self, ctx:dslParser.FavouriteContext):
        pass

    # Exit a parse tree produced by dslParser#favourite.
    def exitFavourite(self, ctx:dslParser.FavouriteContext):
        pass


    # Enter a parse tree produced by dslParser#favourite_required_parameter.
    def enterFavourite_required_parameter(self, ctx:dslParser.Favourite_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#favourite_required_parameter.
    def exitFavourite_required_parameter(self, ctx:dslParser.Favourite_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#scheduleTweet.
    def enterScheduleTweet(self, ctx:dslParser.ScheduleTweetContext):
        pass

    # Exit a parse tree produced by dslParser#scheduleTweet.
    def exitScheduleTweet(self, ctx:dslParser.ScheduleTweetContext):
        pass


    # Enter a parse tree produced by dslParser#schedule_tweet_required_parameter.
    def enterSchedule_tweet_required_parameter(self, ctx:dslParser.Schedule_tweet_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#schedule_tweet_required_parameter.
    def exitSchedule_tweet_required_parameter(self, ctx:dslParser.Schedule_tweet_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#date_time_parameter.
    def enterDate_time_parameter(self, ctx:dslParser.Date_time_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#date_time_parameter.
    def exitDate_time_parameter(self, ctx:dslParser.Date_time_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#date.
    def enterDate(self, ctx:dslParser.DateContext):
        pass

    # Exit a parse tree produced by dslParser#date.
    def exitDate(self, ctx:dslParser.DateContext):
        pass


    # Enter a parse tree produced by dslParser#day_month_year.
    def enterDay_month_year(self, ctx:dslParser.Day_month_yearContext):
        pass

    # Exit a parse tree produced by dslParser#day_month_year.
    def exitDay_month_year(self, ctx:dslParser.Day_month_yearContext):
        pass


    # Enter a parse tree produced by dslParser#day_month.
    def enterDay_month(self, ctx:dslParser.Day_monthContext):
        pass

    # Exit a parse tree produced by dslParser#day_month.
    def exitDay_month(self, ctx:dslParser.Day_monthContext):
        pass


    # Enter a parse tree produced by dslParser#month.
    def enterMonth(self, ctx:dslParser.MonthContext):
        pass

    # Exit a parse tree produced by dslParser#month.
    def exitMonth(self, ctx:dslParser.MonthContext):
        pass


    # Enter a parse tree produced by dslParser#numeric_month.
    def enterNumeric_month(self, ctx:dslParser.Numeric_monthContext):
        pass

    # Exit a parse tree produced by dslParser#numeric_month.
    def exitNumeric_month(self, ctx:dslParser.Numeric_monthContext):
        pass


    # Enter a parse tree produced by dslParser#numeric_day.
    def enterNumeric_day(self, ctx:dslParser.Numeric_dayContext):
        pass

    # Exit a parse tree produced by dslParser#numeric_day.
    def exitNumeric_day(self, ctx:dslParser.Numeric_dayContext):
        pass


    # Enter a parse tree produced by dslParser#year.
    def enterYear(self, ctx:dslParser.YearContext):
        pass

    # Exit a parse tree produced by dslParser#year.
    def exitYear(self, ctx:dslParser.YearContext):
        pass


    # Enter a parse tree produced by dslParser#date_separator.
    def enterDate_separator(self, ctx:dslParser.Date_separatorContext):
        pass

    # Exit a parse tree produced by dslParser#date_separator.
    def exitDate_separator(self, ctx:dslParser.Date_separatorContext):
        pass


    # Enter a parse tree produced by dslParser#time.
    def enterTime(self, ctx:dslParser.TimeContext):
        pass

    # Exit a parse tree produced by dslParser#time.
    def exitTime(self, ctx:dslParser.TimeContext):
        pass


    # Enter a parse tree produced by dslParser#hour_minute.
    def enterHour_minute(self, ctx:dslParser.Hour_minuteContext):
        pass

    # Exit a parse tree produced by dslParser#hour_minute.
    def exitHour_minute(self, ctx:dslParser.Hour_minuteContext):
        pass


    # Enter a parse tree produced by dslParser#time_separator.
    def enterTime_separator(self, ctx:dslParser.Time_separatorContext):
        pass

    # Exit a parse tree produced by dslParser#time_separator.
    def exitTime_separator(self, ctx:dslParser.Time_separatorContext):
        pass


    # Enter a parse tree produced by dslParser#numeric_hour.
    def enterNumeric_hour(self, ctx:dslParser.Numeric_hourContext):
        pass

    # Exit a parse tree produced by dslParser#numeric_hour.
    def exitNumeric_hour(self, ctx:dslParser.Numeric_hourContext):
        pass


    # Enter a parse tree produced by dslParser#numeric_minute.
    def enterNumeric_minute(self, ctx:dslParser.Numeric_minuteContext):
        pass

    # Exit a parse tree produced by dslParser#numeric_minute.
    def exitNumeric_minute(self, ctx:dslParser.Numeric_minuteContext):
        pass


    # Enter a parse tree produced by dslParser#directMessage.
    def enterDirectMessage(self, ctx:dslParser.DirectMessageContext):
        pass

    # Exit a parse tree produced by dslParser#directMessage.
    def exitDirectMessage(self, ctx:dslParser.DirectMessageContext):
        pass


    # Enter a parse tree produced by dslParser#direct_message_required_parameters.
    def enterDirect_message_required_parameters(self, ctx:dslParser.Direct_message_required_parametersContext):
        pass

    # Exit a parse tree produced by dslParser#direct_message_required_parameters.
    def exitDirect_message_required_parameters(self, ctx:dslParser.Direct_message_required_parametersContext):
        pass


    # Enter a parse tree produced by dslParser#autoFavouriteRetweet.
    def enterAutoFavouriteRetweet(self, ctx:dslParser.AutoFavouriteRetweetContext):
        pass

    # Exit a parse tree produced by dslParser#autoFavouriteRetweet.
    def exitAutoFavouriteRetweet(self, ctx:dslParser.AutoFavouriteRetweetContext):
        pass


    # Enter a parse tree produced by dslParser#autoFollowFollowers.
    def enterAutoFollowFollowers(self, ctx:dslParser.AutoFollowFollowersContext):
        pass

    # Exit a parse tree produced by dslParser#autoFollowFollowers.
    def exitAutoFollowFollowers(self, ctx:dslParser.AutoFollowFollowersContext):
        pass


    # Enter a parse tree produced by dslParser#autoReplyMentions.
    def enterAutoReplyMentions(self, ctx:dslParser.AutoReplyMentionsContext):
        pass

    # Exit a parse tree produced by dslParser#autoReplyMentions.
    def exitAutoReplyMentions(self, ctx:dslParser.AutoReplyMentionsContext):
        pass


    # Enter a parse tree produced by dslParser#keywords.
    def enterKeywords(self, ctx:dslParser.KeywordsContext):
        pass

    # Exit a parse tree produced by dslParser#keywords.
    def exitKeywords(self, ctx:dslParser.KeywordsContext):
        pass


    # Enter a parse tree produced by dslParser#stringValue.
    def enterStringValue(self, ctx:dslParser.StringValueContext):
        pass

    # Exit a parse tree produced by dslParser#stringValue.
    def exitStringValue(self, ctx:dslParser.StringValueContext):
        pass


    # Enter a parse tree produced by dslParser#number.
    def enterNumber(self, ctx:dslParser.NumberContext):
        pass

    # Exit a parse tree produced by dslParser#number.
    def exitNumber(self, ctx:dslParser.NumberContext):
        pass


    # Enter a parse tree produced by dslParser#unary_operator.
    def enterUnary_operator(self, ctx:dslParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by dslParser#unary_operator.
    def exitUnary_operator(self, ctx:dslParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by dslParser#unsigned_number.
    def enterUnsigned_number(self, ctx:dslParser.Unsigned_numberContext):
        pass

    # Exit a parse tree produced by dslParser#unsigned_number.
    def exitUnsigned_number(self, ctx:dslParser.Unsigned_numberContext):
        pass


    # Enter a parse tree produced by dslParser#boolean.
    def enterBoolean(self, ctx:dslParser.BooleanContext):
        pass

    # Exit a parse tree produced by dslParser#boolean.
    def exitBoolean(self, ctx:dslParser.BooleanContext):
        pass



del dslParser