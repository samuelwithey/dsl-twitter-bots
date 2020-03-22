# Generated from dsl.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4S\n\4\3\5\6\5V\n\5\r\5\16\5W\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\6\ta\n\t\r\t\16\tb\3\t\3\t\2\2\n\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\3\2\5\6\2\f\f\17\17$$^^\5")
        buf.write("\2\62;C\\c|\5\2\13\f\17\17\"\"\2o\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\26\3\2\2\2\7")
        buf.write("R\3\2\2\2\tU\3\2\2\2\13Y\3\2\2\2\r[\3\2\2\2\17]\3\2\2")
        buf.write("\2\21`\3\2\2\2\23\24\5\5\3\2\24\25\7$\2\2\25\4\3\2\2\2")
        buf.write("\26\37\7$\2\2\27\36\n\2\2\2\30\33\7^\2\2\31\34\13\2\2")
        buf.write("\2\32\34\7\2\2\3\33\31\3\2\2\2\33\32\3\2\2\2\34\36\3\2")
        buf.write("\2\2\35\27\3\2\2\2\35\30\3\2\2\2\36!\3\2\2\2\37\35\3\2")
        buf.write("\2\2\37 \3\2\2\2 \6\3\2\2\2!\37\3\2\2\2\"#\7v\2\2#$\7")
        buf.write("y\2\2$%\7g\2\2%&\7g\2\2&S\7v\2\2\'(\7t\2\2()\7g\2\2)*")
        buf.write("\7v\2\2*+\7y\2\2+,\7g\2\2,-\7g\2\2-S\7v\2\2./\7t\2\2/")
        buf.write("\60\7g\2\2\60\61\7r\2\2\61\62\7n\2\2\62S\7{\2\2\63\64")
        buf.write("\7h\2\2\64\65\7c\2\2\65\66\7x\2\2\66\67\7q\2\2\678\7w")
        buf.write("\2\289\7t\2\29:\7k\2\2:;\7v\2\2;S\7g\2\2<=\7u\2\2=>\7")
        buf.write("e\2\2>?\7j\2\2?@\7g\2\2@A\7f\2\2AB\7w\2\2BC\7n\2\2CS\7")
        buf.write("g\2\2DE\7f\2\2EF\7k\2\2FG\7t\2\2GH\7g\2\2HI\7e\2\2IJ\7")
        buf.write("v\2\2JK\7/\2\2KL\7o\2\2LM\7g\2\2MN\7u\2\2NO\7u\2\2OP\7")
        buf.write("c\2\2PQ\7i\2\2QS\7g\2\2R\"\3\2\2\2R\'\3\2\2\2R.\3\2\2")
        buf.write("\2R\63\3\2\2\2R<\3\2\2\2RD\3\2\2\2S\b\3\2\2\2TV\t\3\2")
        buf.write("\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\n\3\2\2\2")
        buf.write("YZ\7.\2\2Z\f\3\2\2\2[\\\7=\2\2\\\16\3\2\2\2]^\7<\2\2^")
        buf.write("\20\3\2\2\2_a\t\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc")
        buf.write("\3\2\2\2cd\3\2\2\2de\b\t\2\2e\22\3\2\2\2\t\2\33\35\37")
        buf.write("RWb\3\b\2\2")
        return buf.getvalue()


class dslLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    StringLiteral = 1
    UnterminatedStringLiteral = 2
    Action = 3
    Identifier = 4
    COMMA = 5
    SEMICOLON = 6
    COLON = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "StringLiteral", "UnterminatedStringLiteral", "Action", "Identifier", 
            "COMMA", "SEMICOLON", "COLON", "WS" ]

    ruleNames = [ "StringLiteral", "UnterminatedStringLiteral", "Action", 
                  "Identifier", "COMMA", "SEMICOLON", "COLON", "WS" ]

    grammarFileName = "dsl.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


