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


    # Enter a parse tree produced by dslParser#parameter.
    def enterParameter(self, ctx:dslParser.ParameterContext):
        pass

    # Exit a parse tree produced by dslParser#parameter.
    def exitParameter(self, ctx:dslParser.ParameterContext):
        pass


    # Enter a parse tree produced by dslParser#identifier.
    def enterIdentifier(self, ctx:dslParser.IdentifierContext):
        pass

    # Exit a parse tree produced by dslParser#identifier.
    def exitIdentifier(self, ctx:dslParser.IdentifierContext):
        pass


    # Enter a parse tree produced by dslParser#value.
    def enterValue(self, ctx:dslParser.ValueContext):
        pass

    # Exit a parse tree produced by dslParser#value.
    def exitValue(self, ctx:dslParser.ValueContext):
        pass



del dslParser