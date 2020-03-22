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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\3\3\3\7")
        buf.write("\3\33\n\3\f\3\16\3\36\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2%\2\23\3\2\2\2")
        buf.write("\4\26\3\2\2\2\6\37\3\2\2\2\b!\3\2\2\2\n%\3\2\2\2\f\'\3")
        buf.write("\2\2\2\16\17\5\4\3\2\17\20\7\b\2\2\20\22\3\2\2\2\21\16")
        buf.write("\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\3\3\2\2\2\25\23\3\2\2\2\26\27\5\6\4\2\27\34\5\b\5\2\30")
        buf.write("\31\7\7\2\2\31\33\5\f\7\2\32\30\3\2\2\2\33\36\3\2\2\2")
        buf.write("\34\32\3\2\2\2\34\35\3\2\2\2\35\5\3\2\2\2\36\34\3\2\2")
        buf.write("\2\37 \7\5\2\2 \7\3\2\2\2!\"\5\n\6\2\"#\7\t\2\2#$\5\f")
        buf.write("\7\2$\t\3\2\2\2%&\7\6\2\2&\13\3\2\2\2\'(\7\3\2\2(\r\3")
        buf.write("\2\2\2\4\23\34")
        return buf.getvalue()


class dslParser ( Parser ):

    grammarFileName = "dsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "StringLiteral", "UnterminatedStringLiteral", 
                      "Action", "Identifier", "COMMA", "SEMICOLON", "COLON", 
                      "WS" ]

    RULE_twitbot = 0
    RULE_stat = 1
    RULE_action = 2
    RULE_parameter = 3
    RULE_identifier = 4
    RULE_value = 5

    ruleNames =  [ "twitbot", "stat", "action", "parameter", "identifier", 
                   "value" ]

    EOF = Token.EOF
    StringLiteral=1
    UnterminatedStringLiteral=2
    Action=3
    Identifier=4
    COMMA=5
    SEMICOLON=6
    COLON=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.Action:
                self.state = 12
                self.stat()
                self.state = 13
                self.match(dslParser.SEMICOLON)
                self.state = 19
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


        def parameter(self):
            return self.getTypedRuleContext(dslParser.ParameterContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dslParser.COMMA)
            else:
                return self.getToken(dslParser.COMMA, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dslParser.ValueContext)
            else:
                return self.getTypedRuleContext(dslParser.ValueContext,i)


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
            self.state = 20
            self.action()
            self.state = 21
            self.parameter()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.COMMA:
                self.state = 22
                self.match(dslParser.COMMA)
                self.state = 23
                self.value()
                self.state = 28
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
        self.enterRule(localctx, 4, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
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
        self.enterRule(localctx, 6, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.identifier()
            self.state = 32
            self.match(dslParser.COLON)
            self.state = 33
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
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
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
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(dslParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





