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


    # Visit a parse tree produced by dslParser#status.
    def visitStatus(self, ctx:dslParser.StatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet_optional_parameter.
    def visitTweet_optional_parameter(self, ctx:dslParser.Tweet_optional_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#tweet_parameter.
    def visitTweet_parameter(self, ctx:dslParser.Tweet_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#reply.
    def visitReply(self, ctx:dslParser.ReplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#reply_required_parameter.
    def visitReply_required_parameter(self, ctx:dslParser.Reply_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#account_id.
    def visitAccount_id(self, ctx:dslParser.Account_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#retweet.
    def visitRetweet(self, ctx:dslParser.RetweetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#retweet_required_parameter.
    def visitRetweet_required_parameter(self, ctx:dslParser.Retweet_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#retweet_id.
    def visitRetweet_id(self, ctx:dslParser.Retweet_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#favourite.
    def visitFavourite(self, ctx:dslParser.FavouriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#favourite_required_parameter.
    def visitFavourite_required_parameter(self, ctx:dslParser.Favourite_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#schedule.
    def visitSchedule(self, ctx:dslParser.ScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#schedule_required_parameter.
    def visitSchedule_required_parameter(self, ctx:dslParser.Schedule_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#date_time.
    def visitDate_time(self, ctx:dslParser.Date_timeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#direct_message.
    def visitDirect_message(self, ctx:dslParser.Direct_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#direct_message_required_parameter.
    def visitDirect_message_required_parameter(self, ctx:dslParser.Direct_message_required_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#recipient_id.
    def visitRecipient_id(self, ctx:dslParser.Recipient_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#text.
    def visitText(self, ctx:dslParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dslParser#value.
    def visitValue(self, ctx:dslParser.ValueContext):
        return self.visitChildren(ctx)



del dslParser