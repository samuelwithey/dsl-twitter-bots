# Generated from dsl.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\7\2\16")
        buf.write("\n\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16")
        buf.write("\3\32\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2")
        buf.write("\3\3\2\3\t\2\37\2\17\3\2\2\2\4\22\3\2\2\2\6\33\3\2\2\2")
        buf.write("\b\35\3\2\2\2\n\13\5\4\3\2\13\f\7\r\2\2\f\16\3\2\2\2\r")
        buf.write("\n\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20")
        buf.write("\3\3\2\2\2\21\17\3\2\2\2\22\23\5\6\4\2\23\30\5\b\5\2\24")
        buf.write("\25\7\f\2\2\25\27\5\b\5\2\26\24\3\2\2\2\27\32\3\2\2\2")
        buf.write("\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\30\3\2\2")
        buf.write("\2\33\34\t\2\2\2\34\7\3\2\2\2\35\36\7\13\2\2\36\37\7\n")
        buf.write("\2\2\37 \7\13\2\2 \t\3\2\2\2\4\17\30")
        return buf.getvalue()


class dslParser ( Parser ):

    grammarFileName = "dsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tweet'", "'retweet'", "'reply'", "'login'", 
                     "'favourite'", "'schedule-tweet'", "'direct-message'", 
                     "':'", "<INVALID>", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "COMMA", "SEMICOLON", "WS" ]

    RULE_twitbot = 0
    RULE_stat = 1
    RULE_action = 2
    RULE_parameter = 3

    ruleNames =  [ "twitbot", "stat", "action", "parameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    STRING=9
    COMMA=10
    SEMICOLON=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TwitbotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.StatContext)
            else:
                return self.getTypedRuleContext(dslParser.StatContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.SEMICOLON)
            else:
                return self.getToken(dslParser.SEMICOLON, i)

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dslParser.T__0) | (1 << dslParser.T__1) | (1 << dslParser.T__2) | (1 << dslParser.T__3) | (1 << dslParser.T__4) | (1 << dslParser.T__5) | (1 << dslParser.T__6))) != 0):
                self.state = 8
                self.stat()
                self.state = 9
                self.match(dslParser.SEMICOLON)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.action()
            self.state = 17
            self.parameter()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.COMMA:
                self.state = 18
                self.match(dslParser.COMMA)
                self.state = 19
                self.parameter()
                self.state = 24
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
        self.enterRule(localctx, 4, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << dslParser.T__0) | (1 << dslParser.T__1) | (1 << dslParser.T__2) | (1 << dslParser.T__3) | (1 << dslParser.T__4) | (1 << dslParser.T__5) | (1 << dslParser.T__6))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.STRING)
            else:
                return self.getToken(dslParser.STRING, i)

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
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(dslParser.STRING)
            self.state = 28
            self.match(dslParser.T__7)
            self.state = 29
            self.match(dslParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





