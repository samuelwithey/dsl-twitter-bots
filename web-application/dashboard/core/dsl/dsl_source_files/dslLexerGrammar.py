# Generated from dslLexerGrammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2l")
        buf.write("\u02dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u00e0\n\3\7\3\u00e2\n\3\f\3\16\3\u00e5\13\3")
        buf.write("\3\4\3\4\3\4\7\4\u00ea\n\4\f\4\16\4\u00ed\13\4\5\4\u00ef")
        buf.write("\n\4\3\5\6\5\u00f2\n\5\r\5\16\5\u00f3\3\5\3\5\7\5\u00f8")
        buf.write("\n\5\f\5\16\5\u00fb\13\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\6!\u0204\n!\r!\16")
        buf.write("!\u0205\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3")
        buf.write("<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3")
        buf.write("H\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3M\3M\3M\3")
        buf.write("N\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3")
        buf.write("T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3")
        buf.write("Z\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\3]\3]\3]\3^\3^\3^\3_\3_\3")
        buf.write("_\3`\3`\3`\3a\3a\3a\3b\3b\3b\3c\3c\3c\3d\3d\3d\3e\3e\3")
        buf.write("e\3f\3f\3f\3g\3g\3g\3h\3h\3h\3i\3i\3i\3j\3j\3j\3k\3k\3")
        buf.write("k\2\2l\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9")
        buf.write("V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9")
        buf.write("^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7e\u00c9")
        buf.write("f\u00cbg\u00cdh\u00cfi\u00d1j\u00d3k\u00d5l\3\2\5\6\2")
        buf.write("\f\f\17\17$$^^\5\2\13\f\17\17\"\"\3\2\62;\2\u02e3\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\3\u00d7")
        buf.write("\3\2\2\2\5\u00da\3\2\2\2\7\u00ee\3\2\2\2\t\u00f1\3\2\2")
        buf.write("\2\13\u00fc\3\2\2\2\r\u0100\3\2\2\2\17\u0105\3\2\2\2\21")
        buf.write("\u010b\3\2\2\2\23\u010e\3\2\2\2\25\u0114\3\2\2\2\27\u012a")
        buf.write("\3\2\2\2\31\u0131\3\2\2\2\33\u0144\3\2\2\2\35\u0149\3")
        buf.write("\2\2\2\37\u0152\3\2\2\2!\u0166\3\2\2\2#\u016c\3\2\2\2")
        buf.write("%\u0174\3\2\2\2\'\u0183\3\2\2\2)\u018d\3\2\2\2+\u0196")
        buf.write("\3\2\2\2-\u019b\3\2\2\2/\u01a0\3\2\2\2\61\u01a5\3\2\2")
        buf.write("\2\63\u01a7\3\2\2\2\65\u01a9\3\2\2\2\67\u01ab\3\2\2\2")
        buf.write("9\u01b3\3\2\2\2;\u01c8\3\2\2\2=\u01de\3\2\2\2?\u01e7\3")
        buf.write("\2\2\2A\u0203\3\2\2\2C\u0209\3\2\2\2E\u020b\3\2\2\2G\u020d")
        buf.write("\3\2\2\2I\u0212\3\2\2\2K\u0214\3\2\2\2M\u0216\3\2\2\2")
        buf.write("O\u0218\3\2\2\2Q\u021a\3\2\2\2S\u021c\3\2\2\2U\u021e\3")
        buf.write("\2\2\2W\u0220\3\2\2\2Y\u0222\3\2\2\2[\u0224\3\2\2\2]\u0226")
        buf.write("\3\2\2\2_\u0228\3\2\2\2a\u022b\3\2\2\2c\u022e\3\2\2\2")
        buf.write("e\u0231\3\2\2\2g\u0234\3\2\2\2i\u0237\3\2\2\2k\u023a\3")
        buf.write("\2\2\2m\u023d\3\2\2\2o\u0240\3\2\2\2q\u0243\3\2\2\2s\u0246")
        buf.write("\3\2\2\2u\u0249\3\2\2\2w\u024c\3\2\2\2y\u024f\3\2\2\2")
        buf.write("{\u0252\3\2\2\2}\u0255\3\2\2\2\177\u0258\3\2\2\2\u0081")
        buf.write("\u025b\3\2\2\2\u0083\u025e\3\2\2\2\u0085\u0261\3\2\2\2")
        buf.write("\u0087\u0264\3\2\2\2\u0089\u0267\3\2\2\2\u008b\u026a\3")
        buf.write("\2\2\2\u008d\u026d\3\2\2\2\u008f\u0270\3\2\2\2\u0091\u0273")
        buf.write("\3\2\2\2\u0093\u0276\3\2\2\2\u0095\u0279\3\2\2\2\u0097")
        buf.write("\u027c\3\2\2\2\u0099\u027f\3\2\2\2\u009b\u0282\3\2\2\2")
        buf.write("\u009d\u0285\3\2\2\2\u009f\u0288\3\2\2\2\u00a1\u028b\3")
        buf.write("\2\2\2\u00a3\u028e\3\2\2\2\u00a5\u0291\3\2\2\2\u00a7\u0294")
        buf.write("\3\2\2\2\u00a9\u0297\3\2\2\2\u00ab\u029a\3\2\2\2\u00ad")
        buf.write("\u029d\3\2\2\2\u00af\u02a0\3\2\2\2\u00b1\u02a3\3\2\2\2")
        buf.write("\u00b3\u02a6\3\2\2\2\u00b5\u02a9\3\2\2\2\u00b7\u02ac\3")
        buf.write("\2\2\2\u00b9\u02af\3\2\2\2\u00bb\u02b2\3\2\2\2\u00bd\u02b5")
        buf.write("\3\2\2\2\u00bf\u02b8\3\2\2\2\u00c1\u02bb\3\2\2\2\u00c3")
        buf.write("\u02be\3\2\2\2\u00c5\u02c1\3\2\2\2\u00c7\u02c4\3\2\2\2")
        buf.write("\u00c9\u02c7\3\2\2\2\u00cb\u02ca\3\2\2\2\u00cd\u02cd\3")
        buf.write("\2\2\2\u00cf\u02d0\3\2\2\2\u00d1\u02d3\3\2\2\2\u00d3\u02d6")
        buf.write("\3\2\2\2\u00d5\u02d9\3\2\2\2\u00d7\u00d8\5\5\3\2\u00d8")
        buf.write("\u00d9\7$\2\2\u00d9\4\3\2\2\2\u00da\u00e3\7$\2\2\u00db")
        buf.write("\u00e2\n\2\2\2\u00dc\u00df\7^\2\2\u00dd\u00e0\13\2\2\2")
        buf.write("\u00de\u00e0\7\2\2\3\u00df\u00dd\3\2\2\2\u00df\u00de\3")
        buf.write("\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00db\3\2\2\2\u00e1\u00dc")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00ef\7\62\2\2\u00e7\u00eb\4\63;\2\u00e8\u00ea\4\62;")
        buf.write("\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ee\u00e6\3\2\2\2\u00ee\u00e7\3\2\2\2")
        buf.write("\u00ef\b\3\2\2\2\u00f0\u00f2\4\62;\2\u00f1\u00f0\3\2\2")
        buf.write("\2\u00f2\u00f3\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f9\7\60\2\2\u00f6")
        buf.write("\u00f8\4\62;\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\n\3\2\2")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe")
        buf.write("\7c\2\2\u00fe\u00ff\7v\2\2\u00ff\f\3\2\2\2\u0100\u0101")
        buf.write("\7V\2\2\u0101\u0102\7t\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\16\3\2\2\2\u0105\u0106\7H\2\2\u0106\u0107")
        buf.write("\7c\2\2\u0107\u0108\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\20\3\2\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7f\2\2\u010d\22\3\2\2\2\u010e\u010f\7v\2\2\u010f\u0110")
        buf.write("\7y\2\2\u0110\u0111\7g\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\24\3\2\2\2\u0114\u0115\7k\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7a\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\u011a\7r\2\2\u011a\u011b\7n\2\2\u011b\u011c")
        buf.write("\7{\2\2\u011c\u011d\7a\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7a\2\2\u0120\u0121\7u\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122\u0123\7c\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7w\2\2\u0125\u0126\7u\2\2\u0126\u0127\7a\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7f\2\2\u0129\26\3\2\2\2\u012a\u012b")
        buf.write("\7u\2\2\u012b\u012c\7v\2\2\u012c\u012d\7c\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e\u012f\7w\2\2\u012f\u0130\7u\2\2\u0130\30")
        buf.write("\3\2\2\2\u0131\u0132\7r\2\2\u0132\u0133\7q\2\2\u0133\u0134")
        buf.write("\7u\2\2\u0134\u0135\7u\2\2\u0135\u0136\7k\2\2\u0136\u0137")
        buf.write("\7d\2\2\u0137\u0138\7n\2\2\u0138\u0139\7{\2\2\u0139\u013a")
        buf.write("\7a\2\2\u013a\u013b\7u\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\7u\2\2\u013e\u013f\7k\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7k\2\2\u0141\u0142\7x\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143\32\3\2\2\2\u0144\u0145\7n\2\2\u0145\u0146")
        buf.write("\7q\2\2\u0146\u0147\7p\2\2\u0147\u0148\7i\2\2\u0148\34")
        buf.write("\3\2\2\2\u0149\u014a\7r\2\2\u014a\u014b\7n\2\2\u014b\u014c")
        buf.write("\7c\2\2\u014c\u014d\7e\2\2\u014d\u014e\7g\2\2\u014e\u014f")
        buf.write("\7a\2\2\u014f\u0150\7k\2\2\u0150\u0151\7f\2\2\u0151\36")
        buf.write("\3\2\2\2\u0152\u0153\7f\2\2\u0153\u0154\7k\2\2\u0154\u0155")
        buf.write("\7u\2\2\u0155\u0156\7r\2\2\u0156\u0157\7n\2\2\u0157\u0158")
        buf.write("\7c\2\2\u0158\u0159\7{\2\2\u0159\u015a\7a\2\2\u015a\u015b")
        buf.write("\7e\2\2\u015b\u015c\7q\2\2\u015c\u015d\7q\2\2\u015d\u015e")
        buf.write("\7t\2\2\u015e\u015f\7f\2\2\u015f\u0160\7k\2\2\u0160\u0161")
        buf.write("\7p\2\2\u0161\u0162\7c\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7g\2\2\u0164\u0165\7u\2\2\u0165 \3\2\2\2\u0166\u0167")
        buf.write("\7t\2\2\u0167\u0168\7g\2\2\u0168\u0169\7r\2\2\u0169\u016a")
        buf.write("\7n\2\2\u016a\u016b\7{\2\2\u016b\"\3\2\2\2\u016c\u016d")
        buf.write("\7t\2\2\u016d\u016e\7g\2\2\u016e\u016f\7v\2\2\u016f\u0170")
        buf.write("\7y\2\2\u0170\u0171\7g\2\2\u0171\u0172\7g\2\2\u0172\u0173")
        buf.write("\7v\2\2\u0173$\3\2\2\2\u0174\u0175\7f\2\2\u0175\u0176")
        buf.write("\7k\2\2\u0176\u0177\7t\2\2\u0177\u0178\7g\2\2\u0178\u0179")
        buf.write("\7e\2\2\u0179\u017a\7v\2\2\u017a\u017b\7a\2\2\u017b\u017c")
        buf.write("\7o\2\2\u017c\u017d\7g\2\2\u017d\u017e\7u\2\2\u017e\u017f")
        buf.write("\7u\2\2\u017f\u0180\7c\2\2\u0180\u0181\7i\2\2\u0181\u0182")
        buf.write("\7g\2\2\u0182&\3\2\2\2\u0183\u0184\7h\2\2\u0184\u0185")
        buf.write("\7c\2\2\u0185\u0186\7x\2\2\u0186\u0187\7q\2\2\u0187\u0188")
        buf.write("\7w\2\2\u0188\u0189\7t\2\2\u0189\u018a\7k\2\2\u018a\u018b")
        buf.write("\7v\2\2\u018b\u018c\7g\2\2\u018c(\3\2\2\2\u018d\u018e")
        buf.write("\7u\2\2\u018e\u018f\7e\2\2\u018f\u0190\7j\2\2\u0190\u0191")
        buf.write("\7g\2\2\u0191\u0192\7f\2\2\u0192\u0193\7w\2\2\u0193\u0194")
        buf.write("\7n\2\2\u0194\u0195\7g\2\2\u0195*\3\2\2\2\u0196\u0197")
        buf.write("\7f\2\2\u0197\u0198\7c\2\2\u0198\u0199\7v\2\2\u0199\u019a")
        buf.write("\7g\2\2\u019a,\3\2\2\2\u019b\u019c\7v\2\2\u019c\u019d")
        buf.write("\7k\2\2\u019d\u019e\7o\2\2\u019e\u019f\7g\2\2\u019f.\3")
        buf.write("\2\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2\7g\2\2\u01a2\u01a3")
        buf.write("\7z\2\2\u01a3\u01a4\7v\2\2\u01a4\60\3\2\2\2\u01a5\u01a6")
        buf.write("\7.\2\2\u01a6\62\3\2\2\2\u01a7\u01a8\7=\2\2\u01a8\64\3")
        buf.write("\2\2\2\u01a9\u01aa\7<\2\2\u01aa\66\3\2\2\2\u01ab\u01ac")
        buf.write("\7m\2\2\u01ac\u01ad\7g\2\2\u01ad\u01ae\7{\2\2\u01ae\u01af")
        buf.write("\7y\2\2\u01af\u01b0\7q\2\2\u01b0\u01b1\7t\2\2\u01b1\u01b2")
        buf.write("\7f\2\2\u01b28\3\2\2\2\u01b3\u01b4\7h\2\2\u01b4\u01b5")
        buf.write("\7q\2\2\u01b5\u01b6\7n\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8")
        buf.write("\7q\2\2\u01b8\u01b9\7y\2\2\u01b9\u01ba\7a\2\2\u01ba\u01bb")
        buf.write("\7c\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd\7n\2\2\u01bd\u01be")
        buf.write("\7a\2\2\u01be\u01bf\7h\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1")
        buf.write("\7n\2\2\u01c1\u01c2\7n\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4")
        buf.write("\7y\2\2\u01c4\u01c5\7g\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7")
        buf.write("\7u\2\2\u01c7:\3\2\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca")
        buf.write("\7w\2\2\u01ca\u01cb\7v\2\2\u01cb\u01cc\7q\2\2\u01cc\u01cd")
        buf.write("\7o\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf\7v\2\2\u01cf\u01d0")
        buf.write("\7g\2\2\u01d0\u01d1\7a\2\2\u01d1\u01d2\7v\2\2\u01d2\u01d3")
        buf.write("\7k\2\2\u01d3\u01d4\7o\2\2\u01d4\u01d5\7g\2\2\u01d5\u01d6")
        buf.write("\7a\2\2\u01d6\u01d7\7o\2\2\u01d7\u01d8\7k\2\2\u01d8\u01d9")
        buf.write("\7p\2\2\u01d9\u01da\7w\2\2\u01da\u01db\7v\2\2\u01db\u01dc")
        buf.write("\7g\2\2\u01dc\u01dd\7u\2\2\u01dd<\3\2\2\2\u01de\u01df")
        buf.write("\7t\2\2\u01df\u01e0\7g\2\2\u01e0\u01e1\7u\2\2\u01e1\u01e2")
        buf.write("\7r\2\2\u01e2\u01e3\7q\2\2\u01e3\u01e4\7p\2\2\u01e4\u01e5")
        buf.write("\7u\2\2\u01e5\u01e6\7g\2\2\u01e6>\3\2\2\2\u01e7\u01e8")
        buf.write("\7c\2\2\u01e8\u01e9\7w\2\2\u01e9\u01ea\7v\2\2\u01ea\u01eb")
        buf.write("\7q\2\2\u01eb\u01ec\7o\2\2\u01ec\u01ed\7c\2\2\u01ed\u01ee")
        buf.write("\7v\2\2\u01ee\u01ef\7g\2\2\u01ef\u01f0\7a\2\2\u01f0\u01f1")
        buf.write("\7t\2\2\u01f1\u01f2\7g\2\2\u01f2\u01f3\7r\2\2\u01f3\u01f4")
        buf.write("\7n\2\2\u01f4\u01f5\7{\2\2\u01f5\u01f6\7a\2\2\u01f6\u01f7")
        buf.write("\7v\2\2\u01f7\u01f8\7q\2\2\u01f8\u01f9\7a\2\2\u01f9\u01fa")
        buf.write("\7o\2\2\u01fa\u01fb\7g\2\2\u01fb\u01fc\7p\2\2\u01fc\u01fd")
        buf.write("\7v\2\2\u01fd\u01fe\7k\2\2\u01fe\u01ff\7q\2\2\u01ff\u0200")
        buf.write("\7p\2\2\u0200\u0201\7u\2\2\u0201@\3\2\2\2\u0202\u0204")
        buf.write("\t\3\2\2\u0203\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\3\2\2\2")
        buf.write("\u0207\u0208\b!\2\2\u0208B\3\2\2\2\u0209\u020a\7\61\2")
        buf.write("\2\u020aD\3\2\2\2\u020b\u020c\7\60\2\2\u020cF\3\2\2\2")
        buf.write("\u020d\u020e\5I%\2\u020e\u020f\5I%\2\u020f\u0210\5I%\2")
        buf.write("\u0210\u0211\5I%\2\u0211H\3\2\2\2\u0212\u0213\t\4\2\2")
        buf.write("\u0213J\3\2\2\2\u0214\u0215\7\62\2\2\u0215L\3\2\2\2\u0216")
        buf.write("\u0217\7\63\2\2\u0217N\3\2\2\2\u0218\u0219\7\64\2\2\u0219")
        buf.write("P\3\2\2\2\u021a\u021b\7\65\2\2\u021bR\3\2\2\2\u021c\u021d")
        buf.write("\7\66\2\2\u021dT\3\2\2\2\u021e\u021f\7\67\2\2\u021fV\3")
        buf.write("\2\2\2\u0220\u0221\78\2\2\u0221X\3\2\2\2\u0222\u0223\7")
        buf.write("9\2\2\u0223Z\3\2\2\2\u0224\u0225\7:\2\2\u0225\\\3\2\2")
        buf.write("\2\u0226\u0227\7;\2\2\u0227^\3\2\2\2\u0228\u0229\7\62")
        buf.write("\2\2\u0229\u022a\7\62\2\2\u022a`\3\2\2\2\u022b\u022c\7")
        buf.write("\62\2\2\u022c\u022d\7\63\2\2\u022db\3\2\2\2\u022e\u022f")
        buf.write("\7\62\2\2\u022f\u0230\7\64\2\2\u0230d\3\2\2\2\u0231\u0232")
        buf.write("\7\62\2\2\u0232\u0233\7\65\2\2\u0233f\3\2\2\2\u0234\u0235")
        buf.write("\7\62\2\2\u0235\u0236\7\66\2\2\u0236h\3\2\2\2\u0237\u0238")
        buf.write("\7\62\2\2\u0238\u0239\7\67\2\2\u0239j\3\2\2\2\u023a\u023b")
        buf.write("\7\62\2\2\u023b\u023c\78\2\2\u023cl\3\2\2\2\u023d\u023e")
        buf.write("\7\62\2\2\u023e\u023f\79\2\2\u023fn\3\2\2\2\u0240\u0241")
        buf.write("\7\62\2\2\u0241\u0242\7:\2\2\u0242p\3\2\2\2\u0243\u0244")
        buf.write("\7\62\2\2\u0244\u0245\7;\2\2\u0245r\3\2\2\2\u0246\u0247")
        buf.write("\7\63\2\2\u0247\u0248\7\62\2\2\u0248t\3\2\2\2\u0249\u024a")
        buf.write("\7\63\2\2\u024a\u024b\7\63\2\2\u024bv\3\2\2\2\u024c\u024d")
        buf.write("\7\63\2\2\u024d\u024e\7\64\2\2\u024ex\3\2\2\2\u024f\u0250")
        buf.write("\7\63\2\2\u0250\u0251\7\65\2\2\u0251z\3\2\2\2\u0252\u0253")
        buf.write("\7\63\2\2\u0253\u0254\7\66\2\2\u0254|\3\2\2\2\u0255\u0256")
        buf.write("\7\63\2\2\u0256\u0257\7\67\2\2\u0257~\3\2\2\2\u0258\u0259")
        buf.write("\7\63\2\2\u0259\u025a\78\2\2\u025a\u0080\3\2\2\2\u025b")
        buf.write("\u025c\7\63\2\2\u025c\u025d\79\2\2\u025d\u0082\3\2\2\2")
        buf.write("\u025e\u025f\7\63\2\2\u025f\u0260\7:\2\2\u0260\u0084\3")
        buf.write("\2\2\2\u0261\u0262\7\63\2\2\u0262\u0263\7;\2\2\u0263\u0086")
        buf.write("\3\2\2\2\u0264\u0265\7\64\2\2\u0265\u0266\7\62\2\2\u0266")
        buf.write("\u0088\3\2\2\2\u0267\u0268\7\64\2\2\u0268\u0269\7\63\2")
        buf.write("\2\u0269\u008a\3\2\2\2\u026a\u026b\7\64\2\2\u026b\u026c")
        buf.write("\7\64\2\2\u026c\u008c\3\2\2\2\u026d\u026e\7\64\2\2\u026e")
        buf.write("\u026f\7\65\2\2\u026f\u008e\3\2\2\2\u0270\u0271\7\64\2")
        buf.write("\2\u0271\u0272\7\66\2\2\u0272\u0090\3\2\2\2\u0273\u0274")
        buf.write("\7\64\2\2\u0274\u0275\7\67\2\2\u0275\u0092\3\2\2\2\u0276")
        buf.write("\u0277\7\64\2\2\u0277\u0278\78\2\2\u0278\u0094\3\2\2\2")
        buf.write("\u0279\u027a\7\64\2\2\u027a\u027b\79\2\2\u027b\u0096\3")
        buf.write("\2\2\2\u027c\u027d\7\64\2\2\u027d\u027e\7:\2\2\u027e\u0098")
        buf.write("\3\2\2\2\u027f\u0280\7\64\2\2\u0280\u0281\7;\2\2\u0281")
        buf.write("\u009a\3\2\2\2\u0282\u0283\7\65\2\2\u0283\u0284\7\62\2")
        buf.write("\2\u0284\u009c\3\2\2\2\u0285\u0286\7\65\2\2\u0286\u0287")
        buf.write("\7\63\2\2\u0287\u009e\3\2\2\2\u0288\u0289\7\65\2\2\u0289")
        buf.write("\u028a\7\64\2\2\u028a\u00a0\3\2\2\2\u028b\u028c\7\65\2")
        buf.write("\2\u028c\u028d\7\65\2\2\u028d\u00a2\3\2\2\2\u028e\u028f")
        buf.write("\7\65\2\2\u028f\u0290\7\66\2\2\u0290\u00a4\3\2\2\2\u0291")
        buf.write("\u0292\7\65\2\2\u0292\u0293\7\67\2\2\u0293\u00a6\3\2\2")
        buf.write("\2\u0294\u0295\7\65\2\2\u0295\u0296\78\2\2\u0296\u00a8")
        buf.write("\3\2\2\2\u0297\u0298\7\65\2\2\u0298\u0299\79\2\2\u0299")
        buf.write("\u00aa\3\2\2\2\u029a\u029b\7\65\2\2\u029b\u029c\7:\2\2")
        buf.write("\u029c\u00ac\3\2\2\2\u029d\u029e\7\65\2\2\u029e\u029f")
        buf.write("\7;\2\2\u029f\u00ae\3\2\2\2\u02a0\u02a1\7\66\2\2\u02a1")
        buf.write("\u02a2\7\62\2\2\u02a2\u00b0\3\2\2\2\u02a3\u02a4\7\66\2")
        buf.write("\2\u02a4\u02a5\7\63\2\2\u02a5\u00b2\3\2\2\2\u02a6\u02a7")
        buf.write("\7\66\2\2\u02a7\u02a8\7\64\2\2\u02a8\u00b4\3\2\2\2\u02a9")
        buf.write("\u02aa\7\66\2\2\u02aa\u02ab\7\65\2\2\u02ab\u00b6\3\2\2")
        buf.write("\2\u02ac\u02ad\7\66\2\2\u02ad\u02ae\7\66\2\2\u02ae\u00b8")
        buf.write("\3\2\2\2\u02af\u02b0\7\66\2\2\u02b0\u02b1\7\67\2\2\u02b1")
        buf.write("\u00ba\3\2\2\2\u02b2\u02b3\7\66\2\2\u02b3\u02b4\78\2\2")
        buf.write("\u02b4\u00bc\3\2\2\2\u02b5\u02b6\7\66\2\2\u02b6\u02b7")
        buf.write("\79\2\2\u02b7\u00be\3\2\2\2\u02b8\u02b9\7\66\2\2\u02b9")
        buf.write("\u02ba\7:\2\2\u02ba\u00c0\3\2\2\2\u02bb\u02bc\7\66\2\2")
        buf.write("\u02bc\u02bd\7;\2\2\u02bd\u00c2\3\2\2\2\u02be\u02bf\7")
        buf.write("\67\2\2\u02bf\u02c0\7\62\2\2\u02c0\u00c4\3\2\2\2\u02c1")
        buf.write("\u02c2\7\67\2\2\u02c2\u02c3\7\63\2\2\u02c3\u00c6\3\2\2")
        buf.write("\2\u02c4\u02c5\7\67\2\2\u02c5\u02c6\7\64\2\2\u02c6\u00c8")
        buf.write("\3\2\2\2\u02c7\u02c8\7\67\2\2\u02c8\u02c9\7\65\2\2\u02c9")
        buf.write("\u00ca\3\2\2\2\u02ca\u02cb\7\67\2\2\u02cb\u02cc\7\66\2")
        buf.write("\2\u02cc\u00cc\3\2\2\2\u02cd\u02ce\7\67\2\2\u02ce\u02cf")
        buf.write("\7\67\2\2\u02cf\u00ce\3\2\2\2\u02d0\u02d1\7\67\2\2\u02d1")
        buf.write("\u02d2\78\2\2\u02d2\u00d0\3\2\2\2\u02d3\u02d4\7\67\2\2")
        buf.write("\u02d4\u02d5\79\2\2\u02d5\u00d2\3\2\2\2\u02d6\u02d7\7")
        buf.write("\67\2\2\u02d7\u02d8\7:\2\2\u02d8\u00d4\3\2\2\2\u02d9\u02da")
        buf.write("\7\67\2\2\u02da\u02db\7;\2\2\u02db\u00d6\3\2\2\2\13\2")
        buf.write("\u00df\u00e1\u00e3\u00eb\u00ee\u00f3\u00f9\u0205\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class dslLexerGrammar(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    StringLiteral = 1
    UnterminatedStringLiteral = 2
    UNSIGNED_INT = 3
    UNSIGNED_FLOAT = 4
    LAT = 5
    TRUE = 6
    FALSE = 7
    ID = 8
    TWEET = 9
    REPLY_ID = 10
    STATUS = 11
    POSSIBLY_SENSITIVE = 12
    LONG = 13
    PLACE_ID = 14
    DISPLAY_COORDINATES = 15
    REPLY = 16
    RETWEET = 17
    DIRECT_MESSAGE = 18
    FAVOURITE = 19
    SCHEDULE = 20
    DATE = 21
    TIME = 22
    TEXT = 23
    COMMA = 24
    SEMICOLON = 25
    COLON = 26
    KEYWORD = 27
    FOLLOWALL = 28
    AUTOMATE_TIME = 29
    RESPONSE = 30
    AUTOMATE_REPLY_MENTIONS = 31
    WS = 32
    SLASH = 33
    DOT = 34
    FOUR_DIGIT = 35
    DIGIT = 36
    INT_0 = 37
    INT_1 = 38
    INT_2 = 39
    INT_3 = 40
    INT_4 = 41
    INT_5 = 42
    INT_6 = 43
    INT_7 = 44
    INT_8 = 45
    INT_9 = 46
    INT_00 = 47
    INT_01 = 48
    INT_02 = 49
    INT_03 = 50
    INT_04 = 51
    INT_05 = 52
    INT_06 = 53
    INT_07 = 54
    INT_08 = 55
    INT_09 = 56
    INT_10 = 57
    INT_11 = 58
    INT_12 = 59
    INT_13 = 60
    INT_14 = 61
    INT_15 = 62
    INT_16 = 63
    INT_17 = 64
    INT_18 = 65
    INT_19 = 66
    INT_20 = 67
    INT_21 = 68
    INT_22 = 69
    INT_23 = 70
    INT_24 = 71
    INT_25 = 72
    INT_26 = 73
    INT_27 = 74
    INT_28 = 75
    INT_29 = 76
    INT_30 = 77
    INT_31 = 78
    INT_32 = 79
    INT_33 = 80
    INT_34 = 81
    INT_35 = 82
    INT_36 = 83
    INT_37 = 84
    INT_38 = 85
    INT_39 = 86
    INT_40 = 87
    INT_41 = 88
    INT_42 = 89
    INT_43 = 90
    INT_44 = 91
    INT_45 = 92
    INT_46 = 93
    INT_47 = 94
    INT_48 = 95
    INT_49 = 96
    INT_50 = 97
    INT_51 = 98
    INT_52 = 99
    INT_53 = 100
    INT_54 = 101
    INT_55 = 102
    INT_56 = 103
    INT_57 = 104
    INT_58 = 105
    INT_59 = 106

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'lat'", "'True'", "'False'", "'id'", "'tweet'", "'in_reply_to_status_id'", 
            "'status'", "'possibly_sensitive'", "'long'", "'place_id'", 
            "'display_coordinates'", "'reply'", "'retweet'", "'direct_message'", 
            "'favourite'", "'schedule'", "'date'", "'time'", "'text'", "','", 
            "';'", "':'", "'keyword'", "'follow_all_followers'", "'automate_time_minutes'", 
            "'response'", "'automate_reply_to_mentions'", "'/'", "'.'", 
            "'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", 
            "'9'", "'00'", "'01'", "'02'", "'03'", "'04'", "'05'", "'06'", 
            "'07'", "'08'", "'09'", "'10'", "'11'", "'12'", "'13'", "'14'", 
            "'15'", "'16'", "'17'", "'18'", "'19'", "'20'", "'21'", "'22'", 
            "'23'", "'24'", "'25'", "'26'", "'27'", "'28'", "'29'", "'30'", 
            "'31'", "'32'", "'33'", "'34'", "'35'", "'36'", "'37'", "'38'", 
            "'39'", "'40'", "'41'", "'42'", "'43'", "'44'", "'45'", "'46'", 
            "'47'", "'48'", "'49'", "'50'", "'51'", "'52'", "'53'", "'54'", 
            "'55'", "'56'", "'57'", "'58'", "'59'" ]

    symbolicNames = [ "<INVALID>",
            "StringLiteral", "UnterminatedStringLiteral", "UNSIGNED_INT", 
            "UNSIGNED_FLOAT", "LAT", "TRUE", "FALSE", "ID", "TWEET", "REPLY_ID", 
            "STATUS", "POSSIBLY_SENSITIVE", "LONG", "PLACE_ID", "DISPLAY_COORDINATES", 
            "REPLY", "RETWEET", "DIRECT_MESSAGE", "FAVOURITE", "SCHEDULE", 
            "DATE", "TIME", "TEXT", "COMMA", "SEMICOLON", "COLON", "KEYWORD", 
            "FOLLOWALL", "AUTOMATE_TIME", "RESPONSE", "AUTOMATE_REPLY_MENTIONS", 
            "WS", "SLASH", "DOT", "FOUR_DIGIT", "DIGIT", "INT_0", "INT_1", 
            "INT_2", "INT_3", "INT_4", "INT_5", "INT_6", "INT_7", "INT_8", 
            "INT_9", "INT_00", "INT_01", "INT_02", "INT_03", "INT_04", "INT_05", 
            "INT_06", "INT_07", "INT_08", "INT_09", "INT_10", "INT_11", 
            "INT_12", "INT_13", "INT_14", "INT_15", "INT_16", "INT_17", 
            "INT_18", "INT_19", "INT_20", "INT_21", "INT_22", "INT_23", 
            "INT_24", "INT_25", "INT_26", "INT_27", "INT_28", "INT_29", 
            "INT_30", "INT_31", "INT_32", "INT_33", "INT_34", "INT_35", 
            "INT_36", "INT_37", "INT_38", "INT_39", "INT_40", "INT_41", 
            "INT_42", "INT_43", "INT_44", "INT_45", "INT_46", "INT_47", 
            "INT_48", "INT_49", "INT_50", "INT_51", "INT_52", "INT_53", 
            "INT_54", "INT_55", "INT_56", "INT_57", "INT_58", "INT_59" ]

    ruleNames = [ "StringLiteral", "UnterminatedStringLiteral", "UNSIGNED_INT", 
                  "UNSIGNED_FLOAT", "LAT", "TRUE", "FALSE", "ID", "TWEET", 
                  "REPLY_ID", "STATUS", "POSSIBLY_SENSITIVE", "LONG", "PLACE_ID", 
                  "DISPLAY_COORDINATES", "REPLY", "RETWEET", "DIRECT_MESSAGE", 
                  "FAVOURITE", "SCHEDULE", "DATE", "TIME", "TEXT", "COMMA", 
                  "SEMICOLON", "COLON", "KEYWORD", "FOLLOWALL", "AUTOMATE_TIME", 
                  "RESPONSE", "AUTOMATE_REPLY_MENTIONS", "WS", "SLASH", 
                  "DOT", "FOUR_DIGIT", "DIGIT", "INT_0", "INT_1", "INT_2", 
                  "INT_3", "INT_4", "INT_5", "INT_6", "INT_7", "INT_8", 
                  "INT_9", "INT_00", "INT_01", "INT_02", "INT_03", "INT_04", 
                  "INT_05", "INT_06", "INT_07", "INT_08", "INT_09", "INT_10", 
                  "INT_11", "INT_12", "INT_13", "INT_14", "INT_15", "INT_16", 
                  "INT_17", "INT_18", "INT_19", "INT_20", "INT_21", "INT_22", 
                  "INT_23", "INT_24", "INT_25", "INT_26", "INT_27", "INT_28", 
                  "INT_29", "INT_30", "INT_31", "INT_32", "INT_33", "INT_34", 
                  "INT_35", "INT_36", "INT_37", "INT_38", "INT_39", "INT_40", 
                  "INT_41", "INT_42", "INT_43", "INT_44", "INT_45", "INT_46", 
                  "INT_47", "INT_48", "INT_49", "INT_50", "INT_51", "INT_52", 
                  "INT_53", "INT_54", "INT_55", "INT_56", "INT_57", "INT_58", 
                  "INT_59" ]

    grammarFileName = "dslLexerGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


