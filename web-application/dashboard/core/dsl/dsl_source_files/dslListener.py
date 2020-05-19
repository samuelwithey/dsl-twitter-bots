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


    # Enter a parse tree produced by dslParser#status.
    def enterStatus(self, ctx:dslParser.StatusContext):
        pass

    # Exit a parse tree produced by dslParser#status.
    def exitStatus(self, ctx:dslParser.StatusContext):
        pass


    # Enter a parse tree produced by dslParser#tweet_optional_parameter.
    def enterTweet_optional_parameter(self, ctx:dslParser.Tweet_optional_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#tweet_optional_parameter.
    def exitTweet_optional_parameter(self, ctx:dslParser.Tweet_optional_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#tweet_parameter.
    def enterTweet_parameter(self, ctx:dslParser.Tweet_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#tweet_parameter.
    def exitTweet_parameter(self, ctx:dslParser.Tweet_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#reply.
    def enterReply(self, ctx:dslParser.ReplyContext):
        pass

    # Exit a parse tree produced by dslParser#reply.
    def exitReply(self, ctx:dslParser.ReplyContext):
        pass


    # Enter a parse tree produced by dslParser#reply_required_parameter.
    def enterReply_required_parameter(self, ctx:dslParser.Reply_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#reply_required_parameter.
    def exitReply_required_parameter(self, ctx:dslParser.Reply_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#in_reply_to_status_id.
    def enterIn_reply_to_status_id(self, ctx:dslParser.In_reply_to_status_idContext):
        pass

    # Exit a parse tree produced by dslParser#in_reply_to_status_id.
    def exitIn_reply_to_status_id(self, ctx:dslParser.In_reply_to_status_idContext):
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


    # Enter a parse tree produced by dslParser#retweet_id.
    def enterRetweet_id(self, ctx:dslParser.Retweet_idContext):
        pass

    # Exit a parse tree produced by dslParser#retweet_id.
    def exitRetweet_id(self, ctx:dslParser.Retweet_idContext):
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


    # Enter a parse tree produced by dslParser#account_id.
    def enterAccount_id(self, ctx:dslParser.Account_idContext):
        pass

    # Exit a parse tree produced by dslParser#account_id.
    def exitAccount_id(self, ctx:dslParser.Account_idContext):
        pass


    # Enter a parse tree produced by dslParser#schedule.
    def enterSchedule(self, ctx:dslParser.ScheduleContext):
        pass

    # Exit a parse tree produced by dslParser#schedule.
    def exitSchedule(self, ctx:dslParser.ScheduleContext):
        pass


    # Enter a parse tree produced by dslParser#schedule_required_parameter.
    def enterSchedule_required_parameter(self, ctx:dslParser.Schedule_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#schedule_required_parameter.
    def exitSchedule_required_parameter(self, ctx:dslParser.Schedule_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#date_time.
    def enterDate_time(self, ctx:dslParser.Date_timeContext):
        pass

    # Exit a parse tree produced by dslParser#date_time.
    def exitDate_time(self, ctx:dslParser.Date_timeContext):
        pass


    # Enter a parse tree produced by dslParser#direct_message.
    def enterDirect_message(self, ctx:dslParser.Direct_messageContext):
        pass

    # Exit a parse tree produced by dslParser#direct_message.
    def exitDirect_message(self, ctx:dslParser.Direct_messageContext):
        pass


    # Enter a parse tree produced by dslParser#direct_message_required_parameter.
    def enterDirect_message_required_parameter(self, ctx:dslParser.Direct_message_required_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#direct_message_required_parameter.
    def exitDirect_message_required_parameter(self, ctx:dslParser.Direct_message_required_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#recipient_id.
    def enterRecipient_id(self, ctx:dslParser.Recipient_idContext):
        pass

    # Exit a parse tree produced by dslParser#recipient_id.
    def exitRecipient_id(self, ctx:dslParser.Recipient_idContext):
        pass


    # Enter a parse tree produced by dslParser#text.
    def enterText(self, ctx:dslParser.TextContext):
        pass

    # Exit a parse tree produced by dslParser#text.
    def exitText(self, ctx:dslParser.TextContext):
        pass


    # Enter a parse tree produced by dslParser#value.
    def enterValue(self, ctx:dslParser.ValueContext):
        pass

    # Exit a parse tree produced by dslParser#value.
    def exitValue(self, ctx:dslParser.ValueContext):
        pass



del dslParser