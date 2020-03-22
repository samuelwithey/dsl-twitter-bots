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


    # Enter a parse tree produced by dslParser#login_stat.
    def enterLogin_stat(self, ctx:dslParser.Login_statContext):
        pass

    # Exit a parse tree produced by dslParser#login_stat.
    def exitLogin_stat(self, ctx:dslParser.Login_statContext):
        pass


    # Enter a parse tree produced by dslParser#login.
    def enterLogin(self, ctx:dslParser.LoginContext):
        pass

    # Exit a parse tree produced by dslParser#login.
    def exitLogin(self, ctx:dslParser.LoginContext):
        pass


    # Enter a parse tree produced by dslParser#login_parameter.
    def enterLogin_parameter(self, ctx:dslParser.Login_parameterContext):
        pass

    # Exit a parse tree produced by dslParser#login_parameter.
    def exitLogin_parameter(self, ctx:dslParser.Login_parameterContext):
        pass


    # Enter a parse tree produced by dslParser#login_identifier.
    def enterLogin_identifier(self, ctx:dslParser.Login_identifierContext):
        pass

    # Exit a parse tree produced by dslParser#login_identifier.
    def exitLogin_identifier(self, ctx:dslParser.Login_identifierContext):
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