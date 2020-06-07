from .dslVisitor import dslVisitor
from .dslParser import dslParser


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

    def visitDirectMessage(self, ctx: dslParser.DirectMessageContext):
        self.kwargs = {ctx.direct_message_required_parameters().getChild(0).getText(): ctx.direct_message_required_parameters().getChild(2).getText(),
                  ctx.direct_message_required_parameters().getChild(4).getText(): ctx.direct_message_required_parameters().getChild(6).getText()}

    def getTweetOptionalParameters(self, ctx, kwargs):
        for optional_parameter in ctx.tweet_optional_parameters():
            kwargs[optional_parameter.getChild(0).getText()] = optional_parameter.getChild(2).getText()
        return kwargs

    def getKwargs(self):
        return self.kwargs




