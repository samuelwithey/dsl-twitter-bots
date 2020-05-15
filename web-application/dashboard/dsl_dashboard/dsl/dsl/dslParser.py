# Generated from dsl.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\7\7\66\n\7\f\7\16\79\13\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2")
        buf.write("\2<\2\26\3\2\2\2\4 \3\2\2\2\6)\3\2\2\2\b+\3\2\2\2\n/\3")
        buf.write("\2\2\2\f\61\3\2\2\2\16:\3\2\2\2\20<\3\2\2\2\22@\3\2\2")
        buf.write("\2\24B\3\2\2\2\26\27\5\4\3\2\27\35\7\n\2\2\30\31\5\f\7")
        buf.write("\2\31\32\7\n\2\2\32\34\3\2\2\2\33\30\3\2\2\2\34\37\3\2")
        buf.write("\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37\35\3")
        buf.write("\2\2\2 !\5\6\4\2!\"\5\b\5\2\"#\7\t\2\2#$\5\b\5\2$%\7\t")
        buf.write("\2\2%&\5\b\5\2&\'\7\t\2\2\'(\5\b\5\2(\5\3\2\2\2)*\7\3")
        buf.write("\2\2*\7\3\2\2\2+,\5\n\6\2,-\7\13\2\2-.\5\24\13\2.\t\3")
        buf.write("\2\2\2/\60\7\4\2\2\60\13\3\2\2\2\61\62\5\16\b\2\62\67")
        buf.write("\5\20\t\2\63\64\7\t\2\2\64\66\5\20\t\2\65\63\3\2\2\2\66")
        buf.write("9\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\r\3\2\2\29\67\3\2")
        buf.write("\2\2:;\7\7\2\2;\17\3\2\2\2<=\5\22\n\2=>\7\13\2\2>?\5\24")
        buf.write("\13\2?\21\3\2\2\2@A\7\b\2\2A\23\3\2\2\2BC\7\5\2\2C\25")
        buf.write("\3\2\2\2\4\35\67")
        return buf.getvalue()


class dslParser ( Parser ):

    grammarFileName = "dsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'login'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "Login", "LoginIdentifier", "StringLiteral", 
                      "UnterminatedStringLiteral", "Action", "Identifier", 
                      "COMMA", "SEMICOLON", "COLON", "WS" ]

    RULE_twitbot = 0
    RULE_login_stat = 1
    RULE_login = 2
    RULE_login_parameter = 3
    RULE_login_identifier = 4
    RULE_stat = 5
    RULE_action = 6
    RULE_parameter = 7
    RULE_identifier = 8
    RULE_value = 9

    ruleNames =  [ "twitbot", "login_stat", "login", "login_parameter", 
                   "login_identifier", "stat", "action", "parameter", "identifier", 
                   "value" ]

    EOF = Token.EOF
    Login=1
    LoginIdentifier=2
    StringLiteral=3
    UnterminatedStringLiteral=4
    Action=5
    Identifier=6
    COMMA=7
    SEMICOLON=8
    COLON=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TwitbotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def login_stat(self):
            return self.getTypedRuleContext(dslParser.Login_statContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.SEMICOLON)
            else:
                return self.getToken(dslParser.SEMICOLON, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.StatContext)
            else:
                return self.getTypedRuleContext(dslParser.StatContext,i)


        def getRuleIndex(self):
            return dslParser.RULE_twitbot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTwitbot" ):
                listener.enterTwitbot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTwitbot" ):
                listener.exitTwitbot(self)




    def twitbot(self):

        localctx = dslParser.TwitbotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_twitbot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.login_stat()
            self.state = 21
            self.match(dslParser.SEMICOLON)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.Action:
                self.state = 22
                self.stat()
                self.state = 23
                self.match(dslParser.SEMICOLON)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Login_statContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def login(self):
            return self.getTypedRuleContext(dslParser.LoginContext,0)


        def login_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.Login_parameterContext)
            else:
                return self.getTypedRuleContext(dslParser.Login_parameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.COMMA)
            else:
                return self.getToken(dslParser.COMMA, i)

        def getRuleIndex(self):
            return dslParser.RULE_login_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin_stat" ):
                listener.enterLogin_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin_stat" ):
                listener.exitLogin_stat(self)




    def login_stat(self):

        localctx = dslParser.Login_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_login_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.login()
            self.state = 31
            self.login_parameter()
            self.state = 32
            self.match(dslParser.COMMA)
            self.state = 33
            self.login_parameter()
            self.state = 34
            self.match(dslParser.COMMA)
            self.state = 35
            self.login_parameter()
            self.state = 36
            self.match(dslParser.COMMA)
            self.state = 37
            self.login_parameter()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoginContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Login(self):
            return self.getToken(dslParser.Login, 0)

        def getRuleIndex(self):
            return dslParser.RULE_login

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin" ):
                listener.enterLogin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin" ):
                listener.exitLogin(self)




    def login(self):

        localctx = dslParser.LoginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_login)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(dslParser.Login)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Login_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def login_identifier(self):
            return self.getTypedRuleContext(dslParser.Login_identifierContext,0)


        def COLON(self):
            return self.getToken(dslParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(dslParser.ValueContext,0)


        def getRuleIndex(self):
            return dslParser.RULE_login_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin_parameter" ):
                listener.enterLogin_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin_parameter" ):
                listener.exitLogin_parameter(self)




    def login_parameter(self):

        localctx = dslParser.Login_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_login_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.login_identifier()
            self.state = 42
            self.match(dslParser.COLON)
            self.state = 43
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Login_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LoginIdentifier(self):
            return self.getToken(dslParser.LoginIdentifier, 0)

        def getRuleIndex(self):
            return dslParser.RULE_login_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogin_identifier" ):
                listener.enterLogin_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogin_identifier" ):
                listener.exitLogin_identifier(self)




    def login_identifier(self):

        localctx = dslParser.Login_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_login_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(dslParser.LoginIdentifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(dslParser.ActionContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.ParameterContext)
            else:
                return self.getTypedRuleContext(dslParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.COMMA)
            else:
                return self.getToken(dslParser.COMMA, i)

        def getRuleIndex(self):
            return dslParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = dslParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.action()
            self.state = 48
            self.parameter()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.COMMA:
                self.state = 49
                self.match(dslParser.COMMA)
                self.state = 50
                self.parameter()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Action(self):
            return self.getToken(dslParser.Action, 0)

        def getRuleIndex(self):
            return dslParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = dslParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(dslParser.Action)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dslParser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(dslParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(dslParser.ValueContext,0)


        def getRuleIndex(self):
            return dslParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = dslParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.identifier()
            self.state = 59
            self.match(dslParser.COLON)
            self.state = 60
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(dslParser.Identifier, 0)

        def getRuleIndex(self):
            return dslParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = dslParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(dslParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(dslParser.StringLiteral, 0)

        def getRuleIndex(self):
            return dslParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = dslParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(dslParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





