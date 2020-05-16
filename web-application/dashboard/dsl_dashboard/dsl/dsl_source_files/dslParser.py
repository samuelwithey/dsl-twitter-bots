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
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\3")
        buf.write("\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\'\2\16")
        buf.write("\3\2\2\2\4\30\3\2\2\2\6!\3\2\2\2\b#\3\2\2\2\n\'\3\2\2")
        buf.write("\2\f)\3\2\2\2\16\17\5\4\3\2\17\25\7\b\2\2\20\21\5\4\3")
        buf.write("\2\21\22\7\b\2\2\22\24\3\2\2\2\23\20\3\2\2\2\24\27\3\2")
        buf.write("\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\25\3")
        buf.write("\2\2\2\30\31\5\6\4\2\31\36\5\b\5\2\32\33\7\7\2\2\33\35")
        buf.write("\5\b\5\2\34\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37\5\3\2\2\2 \36\3\2\2\2!\"\7\5\2\2\"\7\3\2\2")
        buf.write("\2#$\5\n\6\2$%\7\t\2\2%&\5\f\7\2&\t\3\2\2\2\'(\7\6\2\2")
        buf.write("(\13\3\2\2\2)*\7\3\2\2*\r\3\2\2\2\4\25\36")
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
            self.state = 12
            self.stat()
            self.state = 13
            self.match(dslParser.SEMICOLON)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.Action:
                self.state = 14
                self.stat()
                self.state = 15
                self.match(dslParser.SEMICOLON)
                self.state = 21
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
            self.state = 22
            self.action()
            self.state = 23
            self.parameter()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==dslParser.COMMA:
                self.state = 24
                self.match(dslParser.COMMA)
                self.state = 25
                self.parameter()
                self.state = 30
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
            self.state = 31
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
            self.state = 33
            self.identifier()
            self.state = 34
            self.match(dslParser.COLON)
            self.state = 35
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
            self.state = 37
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
            self.state = 39
            self.match(dslParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





