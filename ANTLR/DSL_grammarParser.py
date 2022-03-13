# Generated from DSL_grammar.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

from DSL_grammarLexer import DSL_grammarLexer


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\u027b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\7\29\n\2\f\2\16\2<\13")
        buf.write("\2\3\2\3\2\7\2@\n\2\f\2\16\2C\13\2\3\2\3\2\7\2G\n\2\f")
        buf.write("\2\16\2J\13\2\3\2\5\2M\n\2\3\3\3\3\7\3Q\n\3\f\3\16\3T")
        buf.write("\13\3\3\3\3\3\7\3X\n\3\f\3\16\3[\13\3\3\3\3\3\5\3_\n\3")
        buf.write("\3\4\3\4\6\4c\n\4\r\4\16\4d\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\7\6o\n\6\f\6\16\6r\13\6\3\6\3\6\3\6\3\6\7\6x\n")
        buf.write("\6\f\6\16\6{\13\6\5\6}\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\7\n\u0087\n\n\f\n\16\n\u008a\13\n\3\n\3\n\7\n\u008e")
        buf.write("\n\n\f\n\16\n\u0091\13\n\3\n\3\n\5\n\u0095\n\n\3\13\3")
        buf.write("\13\7\13\u0099\n\13\f\13\16\13\u009c\13\13\6\13\u009e")
        buf.write("\n\13\r\13\16\13\u009f\3\13\3\13\7\13\u00a4\n\13\f\13")
        buf.write("\16\13\u00a7\13\13\3\13\3\13\3\13\7\13\u00ac\n\13\f\13")
        buf.write("\16\13\u00af\13\13\3\13\3\13\6\13\u00b3\n\13\r\13\16\13")
        buf.write("\u00b4\3\13\3\13\7\13\u00b9\n\13\f\13\16\13\u00bc\13\13")
        buf.write("\3\13\3\13\7\13\u00c0\n\13\f\13\16\13\u00c3\13\13\3\13")
        buf.write("\3\13\3\13\3\13\6\13\u00c9\n\13\r\13\16\13\u00ca\3\13")
        buf.write("\3\13\7\13\u00cf\n\13\f\13\16\13\u00d2\13\13\3\13\3\13")
        buf.write("\7\13\u00d6\n\13\f\13\16\13\u00d9\13\13\3\13\3\13\3\13")
        buf.write("\7\13\u00de\n\13\f\13\16\13\u00e1\13\13\3\13\3\13\3\13")
        buf.write("\3\13\6\13\u00e7\n\13\r\13\16\13\u00e8\3\13\3\13\7\13")
        buf.write("\u00ed\n\13\f\13\16\13\u00f0\13\13\3\13\3\13\7\13\u00f4")
        buf.write("\n\13\f\13\16\13\u00f7\13\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00fd\n\13\f\13\16\13\u0100\13\13\5\13\u0102\n\13\3\f")
        buf.write("\3\f\7\f\u0106\n\f\f\f\16\f\u0109\13\f\3\f\3\f\7\f\u010d")
        buf.write("\n\f\f\f\16\f\u0110\13\f\3\f\3\f\5\f\u0114\n\f\3\f\7\f")
        buf.write("\u0117\n\f\f\f\16\f\u011a\13\f\3\f\3\f\3\f\7\f\u011f\n")
        buf.write("\f\f\f\16\f\u0122\13\f\3\f\3\f\7\f\u0126\n\f\f\f\16\f")
        buf.write("\u0129\13\f\3\f\3\f\5\f\u012d\n\f\3\f\7\f\u0130\n\f\f")
        buf.write("\f\16\f\u0133\13\f\5\f\u0135\n\f\3\r\3\r\6\r\u0139\n\r")
        buf.write("\r\r\16\r\u013a\3\r\3\r\3\r\3\r\3\r\6\r\u0142\n\r\r\r")
        buf.write("\16\r\u0143\3\r\3\r\3\r\3\r\3\r\6\r\u014b\n\r\r\r\16\r")
        buf.write("\u014c\3\r\3\r\3\r\5\r\u0152\n\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\6\21\u015c\n\21\r\21\16\21\u015d\3")
        buf.write("\21\3\21\3\21\5\21\u0163\n\21\3\21\3\21\7\21\u0167\n\21")
        buf.write("\f\21\16\21\u016a\13\21\3\21\3\21\6\21\u016e\n\21\r\21")
        buf.write("\16\21\u016f\3\21\3\21\7\21\u0174\n\21\f\21\16\21\u0177")
        buf.write("\13\21\3\21\3\21\3\21\5\21\u017c\n\21\3\21\3\21\7\21\u0180")
        buf.write("\n\21\f\21\16\21\u0183\13\21\3\21\3\21\3\21\7\21\u0188")
        buf.write("\n\21\f\21\16\21\u018b\13\21\3\21\3\21\6\21\u018f\n\21")
        buf.write("\r\21\16\21\u0190\3\21\3\21\3\21\5\21\u0196\n\21\3\21")
        buf.write("\3\21\7\21\u019a\n\21\f\21\16\21\u019d\13\21\3\21\3\21")
        buf.write("\6\21\u01a1\n\21\r\21\16\21\u01a2\3\21\3\21\7\21\u01a7")
        buf.write("\n\21\f\21\16\21\u01aa\13\21\3\21\3\21\3\21\5\21\u01af")
        buf.write("\n\21\3\21\3\21\7\21\u01b3\n\21\f\21\16\21\u01b6\13\21")
        buf.write("\3\21\3\21\7\21\u01ba\n\21\f\21\16\21\u01bd\13\21\3\21")
        buf.write("\3\21\3\21\7\21\u01c2\n\21\f\21\16\21\u01c5\13\21\3\21")
        buf.write("\3\21\7\21\u01c9\n\21\f\21\16\21\u01cc\13\21\5\21\u01ce")
        buf.write("\n\21\3\22\3\22\3\23\3\23\5\23\u01d4\n\23\3\23\7\23\u01d7")
        buf.write("\n\23\f\23\16\23\u01da\13\23\3\23\3\23\7\23\u01de\n\23")
        buf.write("\f\23\16\23\u01e1\13\23\3\23\3\23\5\23\u01e5\n\23\3\23")
        buf.write("\7\23\u01e8\n\23\f\23\16\23\u01eb\13\23\3\23\3\23\7\23")
        buf.write("\u01ef\n\23\f\23\16\23\u01f2\13\23\3\23\7\23\u01f5\n\23")
        buf.write("\f\23\16\23\u01f8\13\23\3\24\3\24\3\24\3\24\7\24\u01fe")
        buf.write("\n\24\f\24\16\24\u0201\13\24\3\24\5\24\u0204\n\24\3\25")
        buf.write("\3\25\7\25\u0208\n\25\f\25\16\25\u020b\13\25\3\25\3\25")
        buf.write("\7\25\u020f\n\25\f\25\16\25\u0212\13\25\3\25\3\25\6\25")
        buf.write("\u0216\n\25\r\25\16\25\u0217\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0221\n\27\3\27\3\27\7\27\u0225\n\27\f")
        buf.write("\27\16\27\u0228\13\27\3\27\3\27\3\27\3\27\5\27\u022e\n")
        buf.write("\27\3\27\3\27\7\27\u0232\n\27\f\27\16\27\u0235\13\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\7\27\u023c\n\27\f\27\16\27\u023f")
        buf.write("\13\27\3\27\3\27\3\27\3\27\3\27\7\27\u0246\n\27\f\27\16")
        buf.write("\27\u0249\13\27\3\27\3\27\3\27\3\27\3\27\7\27\u0250\n")
        buf.write("\27\f\27\16\27\u0253\13\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u025a\n\27\f\27\16\27\u025d\13\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u0264\n\27\f\27\16\27\u0267\13\27\5\27\u0269")
        buf.write("\n\27\3\30\3\30\3\31\3\31\3\32\3\32\7\32\u0271\n\32\f")
        buf.write("\32\16\32\u0274\13\32\3\32\3\32\3\33\3\33\3\33\3\33\2")
        buf.write("\2\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\2\7\3\2\b\t\3\2\22\23\3\2\24\32\4\2\3\3$$\3")
        buf.write("\2**\2\u02cc\2L\3\2\2\2\4^\3\2\2\2\6`\3\2\2\2\bh\3\2\2")
        buf.write("\2\n|\3\2\2\2\f~\3\2\2\2\16\u0080\3\2\2\2\20\u0082\3\2")
        buf.write("\2\2\22\u0094\3\2\2\2\24\u0101\3\2\2\2\26\u0134\3\2\2")
        buf.write("\2\30\u0151\3\2\2\2\32\u0153\3\2\2\2\34\u0155\3\2\2\2")
        buf.write("\36\u0157\3\2\2\2 \u01cd\3\2\2\2\"\u01cf\3\2\2\2$\u01d3")
        buf.write("\3\2\2\2&\u0203\3\2\2\2(\u0205\3\2\2\2*\u0219\3\2\2\2")
        buf.write(",\u0268\3\2\2\2.\u026a\3\2\2\2\60\u026c\3\2\2\2\62\u026e")
        buf.write("\3\2\2\2\64\u0277\3\2\2\2\66:\5\4\3\2\679\7+\2\28\67\3")
        buf.write("\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2")
        buf.write("\2=A\5\22\n\2>@\7+\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2A")
        buf.write("B\3\2\2\2BH\3\2\2\2CA\3\2\2\2DE\7\3\2\2EG\5\64\33\2FD")
        buf.write("\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2IM\3\2\2\2JH\3\2")
        buf.write("\2\2KM\5\22\n\2L\66\3\2\2\2LK\3\2\2\2M\3\3\2\2\2NR\5\6")
        buf.write("\4\2OQ\7+\2\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2")
        buf.write("S_\3\2\2\2TR\3\2\2\2UY\5\6\4\2VX\7+\2\2WV\3\2\2\2X[\3")
        buf.write("\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\5\4")
        buf.write("\3\2]_\3\2\2\2^N\3\2\2\2^U\3\2\2\2_\5\3\2\2\2`b\7%\2\2")
        buf.write("ac\7+\2\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2ef\3")
        buf.write("\2\2\2fg\5\b\5\2g\7\3\2\2\2hi\5\n\6\2i\t\3\2\2\2jp\5\f")
        buf.write("\7\2ko\5\f\7\2lo\5\16\b\2mo\7\4\2\2nk\3\2\2\2nl\3\2\2")
        buf.write("\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q}\3\2\2\2r")
        buf.write("p\3\2\2\2sy\7\4\2\2tx\5\f\7\2ux\5\16\b\2vx\7\4\2\2wt\3")
        buf.write("\2\2\2wu\3\2\2\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2")
        buf.write("\2z}\3\2\2\2{y\3\2\2\2|j\3\2\2\2|s\3\2\2\2}\13\3\2\2\2")
        buf.write("~\177\7&\2\2\177\r\3\2\2\2\u0080\u0081\7\'\2\2\u0081\17")
        buf.write("\3\2\2\2\u0082\u0083\7(\2\2\u0083\21\3\2\2\2\u0084\u0088")
        buf.write("\5\24\13\2\u0085\u0087\7+\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u0095\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008f\5")
        buf.write("\24\13\2\u008c\u008e\7+\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\5")
        buf.write("\22\n\2\u0093\u0095\3\2\2\2\u0094\u0084\3\2\2\2\u0094")
        buf.write("\u008b\3\2\2\2\u0095\23\3\2\2\2\u0096\u009a\5\30\r\2\u0097")
        buf.write("\u0099\7+\2\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009e\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u0096\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a5\5 \21\2\u00a2\u00a4\7+\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u0102\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00ad\5\26\f\2\u00a9\u00ac\7+\2\2\u00aa")
        buf.write("\u00ac\5\22\n\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2")
        buf.write("\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u0102\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0")
        buf.write("\u00b2\7\5\2\2\u00b1\u00b3\7+\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00ba\5$\23\2\u00b7\u00b9")
        buf.write("\7+\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bd\u00c1\7\6\2\2\u00be\u00c0\7")
        buf.write("+\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c4\u00c5\5\22\n\2\u00c5\u0102\3\2\2")
        buf.write("\2\u00c6\u00c8\7\5\2\2\u00c7\u00c9\7+\2\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00d0\5$\23\2")
        buf.write("\u00cd\u00cf\7+\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3")
        buf.write("\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3")
        buf.write("\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d7\7\6\2\2\u00d4")
        buf.write("\u00d6\7+\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3")
        buf.write("\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\5\22\n\2\u00db")
        buf.write("\u00df\7\7\2\2\u00dc\u00de\7+\2\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3")
        buf.write("\5\22\n\2\u00e3\u0102\3\2\2\2\u00e4\u00e6\t\2\2\2\u00e5")
        buf.write("\u00e7\7+\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3")
        buf.write("\2\2\2\u00ea\u00ee\5$\23\2\u00eb\u00ed\7+\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f1\u00f5\7\6\2\2\u00f2\u00f4\7+\2\2\u00f3\u00f2\3")
        buf.write("\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8")
        buf.write("\u00f9\5\22\n\2\u00f9\u0102\3\2\2\2\u00fa\u00fe\5,\27")
        buf.write("\2\u00fb\u00fd\7+\2\2\u00fc\u00fb\3\2\2\2\u00fd\u0100")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u009d\3\2\2\2")
        buf.write("\u0101\u00a8\3\2\2\2\u0101\u00b0\3\2\2\2\u0101\u00c6\3")
        buf.write("\2\2\2\u0101\u00e4\3\2\2\2\u0101\u00fa\3\2\2\2\u0102\25")
        buf.write("\3\2\2\2\u0103\u0107\5\b\5\2\u0104\u0106\7+\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u010a\u010e\7\n\2\2\u010b\u010d\7+\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0113\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0111\u0114\5&\24\2\u0112\u0114\5(\25\2\u0113\u0111\3")
        buf.write("\2\2\2\u0113\u0112\3\2\2\2\u0114\u0118\3\2\2\2\u0115\u0117")
        buf.write("\7+\2\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0135\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\5\b\5\2\u011c\u0120\5")
        buf.write("*\26\2\u011d\u011f\7+\2\2\u011e\u011d\3\2\2\2\u011f\u0122")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0123\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0127\7\n\2\2")
        buf.write("\u0124\u0126\7+\2\2\u0125\u0124\3\2\2\2\u0126\u0129\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012c")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012d\5&\24\2\u012b")
        buf.write("\u012d\5(\25\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\u0131\3\2\2\2\u012e\u0130\7+\2\2\u012f\u012e\3")
        buf.write("\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0134")
        buf.write("\u0103\3\2\2\2\u0134\u011b\3\2\2\2\u0135\27\3\2\2\2\u0136")
        buf.write("\u0138\7\13\2\2\u0137\u0139\7+\2\2\u0138\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\5\32\16\2\u013d")
        buf.write("\u013e\7\6\2\2\u013e\u0152\3\2\2\2\u013f\u0141\7\f\2\2")
        buf.write("\u0140\u0142\7+\2\2\u0141\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\5\34\17\2\u0146\u0147\7\6\2\2\u0147")
        buf.write("\u0152\3\2\2\2\u0148\u014a\7\r\2\2\u0149\u014b\7+\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f")
        buf.write("\5\36\20\2\u014f\u0150\7\6\2\2\u0150\u0152\3\2\2\2\u0151")
        buf.write("\u0136\3\2\2\2\u0151\u013f\3\2\2\2\u0151\u0148\3\2\2\2")
        buf.write("\u0152\31\3\2\2\2\u0153\u0154\5\b\5\2\u0154\33\3\2\2\2")
        buf.write("\u0155\u0156\5\b\5\2\u0156\35\3\2\2\2\u0157\u0158\5\b")
        buf.write("\5\2\u0158\37\3\2\2\2\u0159\u015b\7\16\2\2\u015a\u015c")
        buf.write("\7+\2\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0168\3\2\2\2")
        buf.write("\u015f\u0163\5\32\16\2\u0160\u0163\5\34\17\2\u0161\u0163")
        buf.write("\5\36\20\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7\17\2")
        buf.write("\2\u0165\u0167\3\2\2\2\u0166\u0162\3\2\2\2\u0167\u016a")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016b\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016d\5\"\22")
        buf.write("\2\u016c\u016e\7+\2\2\u016d\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0175\7\20\2\2\u0172\u0174\7+\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176\u0181\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0178\u017c\5\32\16\2\u0179\u017c\5\34\17\2\u017a")
        buf.write("\u017c\5\36\20\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2")
        buf.write("\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\7\17\2\2\u017e\u0180\3\2\2\2\u017f\u017b\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0189\5")
        buf.write("\"\22\2\u0185\u0188\7+\2\2\u0186\u0188\5 \21\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u01ce\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018c\u018e\7\16\2\2\u018d\u018f")
        buf.write("\7+\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u019b\3\2\2\2")
        buf.write("\u0192\u0196\5\32\16\2\u0193\u0196\5\34\17\2\u0194\u0196")
        buf.write("\5\36\20\2\u0195\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\7\17\2")
        buf.write("\2\u0198\u019a\3\2\2\2\u0199\u0195\3\2\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019e\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a0\5\"\22")
        buf.write("\2\u019f\u01a1\7+\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a8\7\20\2\2\u01a5\u01a7\7+\2\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01b4\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01af\5\32\16\2\u01ac\u01af\5\34\17\2\u01ad")
        buf.write("\u01af\5\36\20\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2")
        buf.write("\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1")
        buf.write("\7\17\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01ae\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01bb\5")
        buf.write("\"\22\2\u01b8\u01ba\7+\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\7\21\2")
        buf.write("\2\u01bf\u01c3\7\6\2\2\u01c0\u01c2\7+\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c6\u01ca\5\60\31\2\u01c7\u01c9\5 \21\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cd\u0159\3\2\2\2\u01cd\u018c\3\2\2\2\u01ce!\3\2\2")
        buf.write("\2\u01cf\u01d0\5\b\5\2\u01d0#\3\2\2\2\u01d1\u01d4\5&\24")
        buf.write("\2\u01d2\u01d4\5(\25\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d8\3\2\2\2\u01d5\u01d7\7+\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2")
        buf.write("\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01db\u01df\5.\30\2\u01dc\u01de\7+\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e4\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e2\u01e5\5&\24\2\u01e3\u01e5\5(\25\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e9\3\2\2\2\u01e6\u01e8")
        buf.write("\7+\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01f6\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01f0\t\3\2\2\u01ed\u01ef\7")
        buf.write("+\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f3\u01f5\5$\23\2\u01f4\u01ec\3\2\2\2")
        buf.write("\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3")
        buf.write("\2\2\2\u01f7%\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u0204")
        buf.write("\5\b\5\2\u01fa\u0204\5\60\31\2\u01fb\u01ff\5\20\t\2\u01fc")
        buf.write("\u01fe\5\16\b\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2")
        buf.write("\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0204")
        buf.write("\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0204\5,\27\2\u0203")
        buf.write("\u01f9\3\2\2\2\u0203\u01fa\3\2\2\2\u0203\u01fb\3\2\2\2")
        buf.write("\u0203\u0202\3\2\2\2\u0204\'\3\2\2\2\u0205\u0215\5&\24")
        buf.write("\2\u0206\u0208\7+\2\2\u0207\u0206\3\2\2\2\u0208\u020b")
        buf.write("\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020c\3\2\2\2\u020b\u0209\3\2\2\2\u020c\u0210\5*\26\2")
        buf.write("\u020d\u020f\7+\2\2\u020e\u020d\3\2\2\2\u020f\u0212\3")
        buf.write("\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213")
        buf.write("\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0214\5&\24\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u0209\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218)\3\2\2")
        buf.write("\2\u0219\u021a\t\4\2\2\u021a+\3\2\2\2\u021b\u021c\7\33")
        buf.write("\2\2\u021c\u0220\7\34\2\2\u021d\u0221\5\32\16\2\u021e")
        buf.write("\u0221\5\34\17\2\u021f\u0221\5\36\20\2\u0220\u021d\3\2")
        buf.write("\2\2\u0220\u021e\3\2\2\2\u0220\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0226\7\35\2\2\u0223\u0225\7+\2\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0269\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0229\u022a\7\36\2\2\u022a\u022d\7\34\2\2\u022b")
        buf.write("\u022e\5\32\16\2\u022c\u022e\5\34\17\2\u022d\u022b\3\2")
        buf.write("\2\2\u022d\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0233")
        buf.write("\7\35\2\2\u0230\u0232\7+\2\2\u0231\u0230\3\2\2\2\u0232")
        buf.write("\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2")
        buf.write("\u0234\u0269\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\7")
        buf.write("\37\2\2\u0237\u0238\7\34\2\2\u0238\u0239\5\32\16\2\u0239")
        buf.write("\u023d\7\35\2\2\u023a\u023c\7+\2\2\u023b\u023a\3\2\2\2")
        buf.write("\u023c\u023f\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e\3")
        buf.write("\2\2\2\u023e\u0269\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0241")
        buf.write("\7 \2\2\u0241\u0242\7\34\2\2\u0242\u0243\5\"\22\2\u0243")
        buf.write("\u0247\7\35\2\2\u0244\u0246\7+\2\2\u0245\u0244\3\2\2\2")
        buf.write("\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3")
        buf.write("\2\2\2\u0248\u0269\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b")
        buf.write("\7!\2\2\u024b\u024c\7\34\2\2\u024c\u024d\5\"\22\2\u024d")
        buf.write("\u0251\7\35\2\2\u024e\u0250\7+\2\2\u024f\u024e\3\2\2\2")
        buf.write("\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3")
        buf.write("\2\2\2\u0252\u0269\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u0255")
        buf.write("\7\"\2\2\u0255\u0256\7\34\2\2\u0256\u0257\5\"\22\2\u0257")
        buf.write("\u025b\7\35\2\2\u0258\u025a\7+\2\2\u0259\u0258\3\2\2\2")
        buf.write("\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3")
        buf.write("\2\2\2\u025c\u0269\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f")
        buf.write("\7#\2\2\u025f\u0260\7\34\2\2\u0260\u0261\5\"\22\2\u0261")
        buf.write("\u0265\7\35\2\2\u0262\u0264\7+\2\2\u0263\u0262\3\2\2\2")
        buf.write("\u0264\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0266\u0269\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u021b")
        buf.write("\3\2\2\2\u0268\u0229\3\2\2\2\u0268\u0236\3\2\2\2\u0268")
        buf.write("\u0240\3\2\2\2\u0268\u024a\3\2\2\2\u0268\u0254\3\2\2\2")
        buf.write("\u0268\u025e\3\2\2\2\u0269-\3\2\2\2\u026a\u026b\7)\2\2")
        buf.write("\u026b/\3\2\2\2\u026c\u026d\5\62\32\2\u026d\61\3\2\2\2")
        buf.write("\u026e\u0272\7$\2\2\u026f\u0271\n\5\2\2\u0270\u026f\3")
        buf.write("\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0273")
        buf.write("\3\2\2\2\u0273\u0275\3\2\2\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0276\7$\2\2\u0276\63\3\2\2\2\u0277\u0278\7\3\2\2\u0278")
        buf.write("\u0279\n\6\2\2\u0279\65\3\2\2\2[:AHLRY^dnpwy|\u0088\u008f")
        buf.write("\u0094\u009a\u009f\u00a5\u00ab\u00ad\u00b4\u00ba\u00c1")
        buf.write("\u00ca\u00d0\u00d7\u00df\u00e8\u00ee\u00f5\u00fe\u0101")
        buf.write("\u0107\u010e\u0113\u0118\u0120\u0127\u012c\u0131\u0134")
        buf.write("\u013a\u0143\u014c\u0151\u015d\u0162\u0168\u016f\u0175")
        buf.write("\u017b\u0181\u0187\u0189\u0190\u0195\u019b\u01a2\u01a8")
        buf.write("\u01ae\u01b4\u01bb\u01c3\u01ca\u01cd\u01d3\u01d8\u01df")
        buf.write("\u01e4\u01e9\u01f0\u01f6\u01ff\u0203\u0209\u0210\u0217")
        buf.write("\u0220\u0226\u022d\u0233\u023d\u0247\u0251\u025b\u0265")
        buf.write("\u0268\u0272")
        return buf.getvalue()


class DSL_grammarParser ( Parser ):

    grammarFileName = "DSL_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'_'", "'if'", "':'", "'else'", 
                     "'while'", "'for'", "'='", "'STORY'", "'STAGE'", "'SECTION'", 
                     "'FROM'", "'.'", "'TO'", "'ACTION'", "'&&'", "'||'", 
                     "'+'", "'-'", "'*'", "'**'", "'/'", "'//'", "'%'", 
                     "'nr_nodes'", "'('", "')'", "'nr_sections'", "'nr_stages'", 
                     "'nr_of_interactions'", "'color'", "'width'", "'style'", 
                     "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TYPE", "LETTERS", 
                      "DIGITS", "NENULE_DIGITS", "SIGNS", "NEWLINE", "WHITESPACE" ]

    RULE_source_code = 0
    RULE_variables_declaration = 1
    RULE_variable_declaration = 2
    RULE_variable = 3
    RULE_identifier = 4
    RULE_letter = 5
    RULE_digit = 6
    RULE_nenule_digit = 7
    RULE_set_of_affirmations = 8
    RULE_set_of_affirmation = 9
    RULE_variable_attribution = 10
    RULE_act_description = 11
    RULE_story = 12
    RULE_stage = 13
    RULE_section = 14
    RULE_flow_description = 15
    RULE_node = 16
    RULE_conditions = 17
    RULE_operand = 18
    RULE_composed_operand = 19
    RULE_operation = 20
    RULE_function = 21
    RULE_condition = 22
    RULE_string = 23
    RULE_characters = 24
    RULE_comments = 25

    ruleNames =  [ "source_code", "variables_declaration", "variable_declaration", 
                   "variable", "identifier", "letter", "digit", "nenule_digit", 
                   "set_of_affirmations", "set_of_affirmation", "variable_attribution", 
                   "act_description", "story", "stage", "section", "flow_description", 
                   "node", "conditions", "operand", "composed_operand", 
                   "operation", "function", "condition", "string", "characters", 
                   "comments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    TYPE=35
    LETTERS=36
    DIGITS=37
    NENULE_DIGITS=38
    SIGNS=39
    NEWLINE=40
    WHITESPACE=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    def parse(argv):
        from DSL_grammarListener import DSL_grammarListener
        if len(sys.argv) > 1:
            input = FileStream(argv[1])
            lexer = DSL_grammarLexer(input)
            stream = CommonTokenStream(lexer)
            parser = DSL_grammarParser(stream)
            tree = parser.source_code()
            printer = DSL_grammarListener()
            walker = ParseTreeWalker()
            walker.walk(printer, tree)
        else:
            print('Error : Expected a valid file')


    class Source_codeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declaration(self):
            return self.getTypedRuleContext(DSL_grammarParser.Variables_declarationContext,0)


        def set_of_affirmations(self):
            return self.getTypedRuleContext(DSL_grammarParser.Set_of_affirmationsContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def comments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.CommentsContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.CommentsContext,i)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_source_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource_code" ):
                listener.enterSource_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource_code" ):
                listener.exitSource_code(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource_code" ):
                return visitor.visitSource_code(self)
            else:
                return visitor.visitChildren(self)




    def source_code(self):

        localctx = DSL_grammarParser.Source_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_source_code)
        self._la = 0 # Token type
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DSL_grammarParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.variables_declaration()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 53
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self.set_of_affirmations()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 60
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.T__0:
                    self.state = 66
                    self.match(DSL_grammarParser.T__0)
                    self.state = 67
                    self.comments()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [DSL_grammarParser.T__1, DSL_grammarParser.T__2, DSL_grammarParser.T__5, DSL_grammarParser.T__6, DSL_grammarParser.T__8, DSL_grammarParser.T__9, DSL_grammarParser.T__10, DSL_grammarParser.T__24, DSL_grammarParser.T__27, DSL_grammarParser.T__28, DSL_grammarParser.T__29, DSL_grammarParser.T__30, DSL_grammarParser.T__31, DSL_grammarParser.T__32, DSL_grammarParser.LETTERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.set_of_affirmations()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(DSL_grammarParser.Variable_declarationContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def variables_declaration(self):
            return self.getTypedRuleContext(DSL_grammarParser.Variables_declarationContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_variables_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables_declaration" ):
                listener.enterVariables_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables_declaration" ):
                listener.exitVariables_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declaration" ):
                return visitor.visitVariables_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variables_declaration(self):

        localctx = DSL_grammarParser.Variables_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variables_declaration)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.variable_declaration()
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 77
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 82
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.variable_declaration()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 84
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
                self.variables_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(DSL_grammarParser.TYPE, 0)

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = DSL_grammarParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(DSL_grammarParser.TYPE)
            self.state = 96 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 95
                self.match(DSL_grammarParser.WHITESPACE)
                self.state = 98 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DSL_grammarParser.WHITESPACE):
                    break

            self.state = 100
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(DSL_grammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = DSL_grammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.LetterContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.LetterContext,i)


        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.DigitContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.DigitContext,i)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = DSL_grammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DSL_grammarParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.letter()
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 108
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [DSL_grammarParser.LETTERS]:
                            self.state = 105
                            self.letter()
                            pass
                        elif token in [DSL_grammarParser.DIGITS]:
                            self.state = 106
                            self.digit()
                            pass
                        elif token in [DSL_grammarParser.T__1]:
                            self.state = 107
                            self.match(DSL_grammarParser.T__1)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 112
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(DSL_grammarParser.T__1)
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 117
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [DSL_grammarParser.LETTERS]:
                            self.state = 114
                            self.letter()
                            pass
                        elif token in [DSL_grammarParser.DIGITS]:
                            self.state = 115
                            self.digit()
                            pass
                        elif token in [DSL_grammarParser.T__1]:
                            self.state = 116
                            self.match(DSL_grammarParser.T__1)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 121
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTERS(self):
            return self.getToken(DSL_grammarParser.LETTERS, 0)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_letter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetter" ):
                listener.enterLetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetter" ):
                listener.exitLetter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetter" ):
                return visitor.visitLetter(self)
            else:
                return visitor.visitChildren(self)




    def letter(self):

        localctx = DSL_grammarParser.LetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_letter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(DSL_grammarParser.LETTERS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(DSL_grammarParser.DIGITS, 0)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)




    def digit(self):

        localctx = DSL_grammarParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(DSL_grammarParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nenule_digitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NENULE_DIGITS(self):
            return self.getToken(DSL_grammarParser.NENULE_DIGITS, 0)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_nenule_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNenule_digit" ):
                listener.enterNenule_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNenule_digit" ):
                listener.exitNenule_digit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNenule_digit" ):
                return visitor.visitNenule_digit(self)
            else:
                return visitor.visitChildren(self)




    def nenule_digit(self):

        localctx = DSL_grammarParser.Nenule_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nenule_digit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(DSL_grammarParser.NENULE_DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_of_affirmationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def set_of_affirmation(self):
            return self.getTypedRuleContext(DSL_grammarParser.Set_of_affirmationContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def set_of_affirmations(self):
            return self.getTypedRuleContext(DSL_grammarParser.Set_of_affirmationsContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_set_of_affirmations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_of_affirmations" ):
                listener.enterSet_of_affirmations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_of_affirmations" ):
                listener.exitSet_of_affirmations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_of_affirmations" ):
                return visitor.visitSet_of_affirmations(self)
            else:
                return visitor.visitChildren(self)




    def set_of_affirmations(self):

        localctx = DSL_grammarParser.Set_of_affirmationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_set_of_affirmations)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.set_of_affirmation()
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 131
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 136
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.set_of_affirmation()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 138
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 144
                self.set_of_affirmations()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_of_affirmationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flow_description(self):
            return self.getTypedRuleContext(DSL_grammarParser.Flow_descriptionContext,0)


        def act_description(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.Act_descriptionContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.Act_descriptionContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def variable_attribution(self):
            return self.getTypedRuleContext(DSL_grammarParser.Variable_attributionContext,0)


        def set_of_affirmations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.Set_of_affirmationsContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.Set_of_affirmationsContext,i)


        def conditions(self):
            return self.getTypedRuleContext(DSL_grammarParser.ConditionsContext,0)


        def function(self):
            return self.getTypedRuleContext(DSL_grammarParser.FunctionContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_set_of_affirmation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_of_affirmation" ):
                listener.enterSet_of_affirmation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_of_affirmation" ):
                listener.exitSet_of_affirmation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_of_affirmation" ):
                return visitor.visitSet_of_affirmation(self)
            else:
                return visitor.visitChildren(self)




    def set_of_affirmation(self):

        localctx = DSL_grammarParser.Set_of_affirmationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_set_of_affirmation)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 148
                    self.act_description()
                    self.state = 152
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DSL_grammarParser.WHITESPACE:
                        self.state = 149
                        self.match(DSL_grammarParser.WHITESPACE)
                        self.state = 154
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 157 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DSL_grammarParser.T__8) | (1 << DSL_grammarParser.T__9) | (1 << DSL_grammarParser.T__10))) != 0)):
                        break

                self.state = 159
                self.flow_description()
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 160
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 165
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.variable_attribution()
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 169
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [DSL_grammarParser.WHITESPACE]:
                            self.state = 167
                            self.match(DSL_grammarParser.WHITESPACE)
                            pass
                        elif token in [DSL_grammarParser.T__1, DSL_grammarParser.T__2, DSL_grammarParser.T__5, DSL_grammarParser.T__6, DSL_grammarParser.T__8, DSL_grammarParser.T__9, DSL_grammarParser.T__10, DSL_grammarParser.T__24, DSL_grammarParser.T__27, DSL_grammarParser.T__28, DSL_grammarParser.T__29, DSL_grammarParser.T__30, DSL_grammarParser.T__31, DSL_grammarParser.T__32, DSL_grammarParser.LETTERS]:
                            self.state = 168
                            self.set_of_affirmations()
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 173
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(DSL_grammarParser.T__2)
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 175
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 178 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 180
                self.conditions()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 181
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 187
                self.match(DSL_grammarParser.T__3)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 188
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 194
                self.set_of_affirmations()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(DSL_grammarParser.T__2)
                self.state = 198 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 197
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 200 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 202
                self.conditions()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 203
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 209
                self.match(DSL_grammarParser.T__3)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 210
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 216
                self.set_of_affirmations()
                self.state = 217
                self.match(DSL_grammarParser.T__4)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 218
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 224
                self.set_of_affirmations()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                _la = self._input.LA(1)
                if not(_la==DSL_grammarParser.T__5 or _la==DSL_grammarParser.T__6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 227
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 230 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 232
                self.conditions()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 233
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 239
                self.match(DSL_grammarParser.T__3)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 240
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 246
                self.set_of_affirmations()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.function()
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 249
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 254
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_attributionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def operand(self):
            return self.getTypedRuleContext(DSL_grammarParser.OperandContext,0)


        def composed_operand(self):
            return self.getTypedRuleContext(DSL_grammarParser.Composed_operandContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def operation(self):
            return self.getTypedRuleContext(DSL_grammarParser.OperationContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_variable_attribution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_attribution" ):
                listener.enterVariable_attribution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_attribution" ):
                listener.exitVariable_attribution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_attribution" ):
                return visitor.visitVariable_attribution(self)
            else:
                return visitor.visitChildren(self)




    def variable_attribution(self):

        localctx = DSL_grammarParser.Variable_attributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_attribution)
        self._la = 0 # Token type
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.variable()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 258
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 264
                self.match(DSL_grammarParser.T__7)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 265
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 270
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.operand()
                    pass

                elif la_ == 2:
                    self.state = 272
                    self.composed_operand()
                    pass


                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 275
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 280
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.variable()
                self.state = 282
                self.operation()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 283
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
                self.match(DSL_grammarParser.T__7)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 290
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 298
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 296
                    self.operand()
                    pass

                elif la_ == 2:
                    self.state = 297
                    self.composed_operand()
                    pass


                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 300
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 305
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Act_descriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def story(self):
            return self.getTypedRuleContext(DSL_grammarParser.StoryContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def stage(self):
            return self.getTypedRuleContext(DSL_grammarParser.StageContext,0)


        def section(self):
            return self.getTypedRuleContext(DSL_grammarParser.SectionContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_act_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAct_description" ):
                listener.enterAct_description(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAct_description" ):
                listener.exitAct_description(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAct_description" ):
                return visitor.visitAct_description(self)
            else:
                return visitor.visitChildren(self)




    def act_description(self):

        localctx = DSL_grammarParser.Act_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_act_description)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DSL_grammarParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(DSL_grammarParser.T__8)
                self.state = 310 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 309
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 312 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 314
                self.story()
                self.state = 315
                self.match(DSL_grammarParser.T__3)
                pass
            elif token in [DSL_grammarParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(DSL_grammarParser.T__9)
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 318
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 321 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 323
                self.stage()
                self.state = 324
                self.match(DSL_grammarParser.T__3)
                pass
            elif token in [DSL_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(DSL_grammarParser.T__10)
                self.state = 328 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 327
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 330 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 332
                self.section()
                self.state = 333
                self.match(DSL_grammarParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_story

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStory" ):
                listener.enterStory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStory" ):
                listener.exitStory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStory" ):
                return visitor.visitStory(self)
            else:
                return visitor.visitChildren(self)




    def story(self):

        localctx = DSL_grammarParser.StoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_story)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_stage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStage" ):
                listener.enterStage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStage" ):
                listener.exitStage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStage" ):
                return visitor.visitStage(self)
            else:
                return visitor.visitChildren(self)




    def stage(self):

        localctx = DSL_grammarParser.StageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = DSL_grammarParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flow_descriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.NodeContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.NodeContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def flow_description(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.Flow_descriptionContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.Flow_descriptionContext,i)


        def story(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.StoryContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.StoryContext,i)


        def stage(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.StageContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.StageContext,i)


        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.SectionContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.SectionContext,i)


        def string(self):
            return self.getTypedRuleContext(DSL_grammarParser.StringContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_flow_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlow_description" ):
                listener.enterFlow_description(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlow_description" ):
                listener.exitFlow_description(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow_description" ):
                return visitor.visitFlow_description(self)
            else:
                return visitor.visitChildren(self)




    def flow_description(self):

        localctx = DSL_grammarParser.Flow_descriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_flow_description)
        self._la = 0 # Token type
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(DSL_grammarParser.T__11)
                self.state = 345 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 344
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 347 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 352
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                        if la_ == 1:
                            self.state = 349
                            self.story()
                            pass

                        elif la_ == 2:
                            self.state = 350
                            self.stage()
                            pass

                        elif la_ == 3:
                            self.state = 351
                            self.section()
                            pass


                        self.state = 354
                        self.match(DSL_grammarParser.T__12) 
                    self.state = 360
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

                self.state = 361
                self.node()
                self.state = 363 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 362
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 365 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 367
                self.match(DSL_grammarParser.T__13)
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 368
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 373
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 377
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                        if la_ == 1:
                            self.state = 374
                            self.story()
                            pass

                        elif la_ == 2:
                            self.state = 375
                            self.stage()
                            pass

                        elif la_ == 3:
                            self.state = 376
                            self.section()
                            pass


                        self.state = 379
                        self.match(DSL_grammarParser.T__12) 
                    self.state = 385
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                self.state = 386
                self.node()
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 389
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [DSL_grammarParser.WHITESPACE]:
                            self.state = 387
                            self.match(DSL_grammarParser.WHITESPACE)
                            pass
                        elif token in [DSL_grammarParser.T__11]:
                            self.state = 388
                            self.flow_description()
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 393
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(DSL_grammarParser.T__11)
                self.state = 396 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 395
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 398 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 403
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                        if la_ == 1:
                            self.state = 400
                            self.story()
                            pass

                        elif la_ == 2:
                            self.state = 401
                            self.stage()
                            pass

                        elif la_ == 3:
                            self.state = 402
                            self.section()
                            pass


                        self.state = 405
                        self.match(DSL_grammarParser.T__12) 
                    self.state = 411
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

                self.state = 412
                self.node()
                self.state = 414 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 413
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 416 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==DSL_grammarParser.WHITESPACE):
                        break

                self.state = 418
                self.match(DSL_grammarParser.T__13)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 419
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 424
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 428
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                        if la_ == 1:
                            self.state = 425
                            self.story()
                            pass

                        elif la_ == 2:
                            self.state = 426
                            self.stage()
                            pass

                        elif la_ == 3:
                            self.state = 427
                            self.section()
                            pass


                        self.state = 430
                        self.match(DSL_grammarParser.T__12) 
                    self.state = 436
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

                self.state = 437
                self.node()
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 438
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 444
                self.match(DSL_grammarParser.T__14)
                self.state = 445
                self.match(DSL_grammarParser.T__3)
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.WHITESPACE:
                    self.state = 446
                    self.match(DSL_grammarParser.WHITESPACE)
                    self.state = 451
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 452
                self.string()
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 453
                        self.flow_description() 
                    self.state = 458
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNode" ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)




    def node(self):

        localctx = DSL_grammarParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(DSL_grammarParser.ConditionContext,0)


        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.OperandContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.OperandContext,i)


        def composed_operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.Composed_operandContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.Composed_operandContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def conditions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.ConditionsContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.ConditionsContext,i)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_conditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditions" ):
                listener.enterConditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditions" ):
                listener.exitConditions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditions" ):
                return visitor.visitConditions(self)
            else:
                return visitor.visitChildren(self)




    def conditions(self):

        localctx = DSL_grammarParser.ConditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_conditions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 463
                self.operand()
                pass

            elif la_ == 2:
                self.state = 464
                self.composed_operand()
                pass


            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DSL_grammarParser.WHITESPACE:
                self.state = 467
                self.match(DSL_grammarParser.WHITESPACE)
                self.state = 472
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 473
            self.condition()
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DSL_grammarParser.WHITESPACE:
                self.state = 474
                self.match(DSL_grammarParser.WHITESPACE)
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 480
                self.operand()
                pass

            elif la_ == 2:
                self.state = 481
                self.composed_operand()
                pass


            self.state = 487
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 484
                    self.match(DSL_grammarParser.WHITESPACE) 
                self.state = 489
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,72,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 490
                    _la = self._input.LA(1)
                    if not(_la==DSL_grammarParser.T__15 or _la==DSL_grammarParser.T__16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 494
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DSL_grammarParser.WHITESPACE:
                        self.state = 491
                        self.match(DSL_grammarParser.WHITESPACE)
                        self.state = 496
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 497
                    self.conditions() 
                self.state = 502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(DSL_grammarParser.VariableContext,0)


        def string(self):
            return self.getTypedRuleContext(DSL_grammarParser.StringContext,0)


        def nenule_digit(self):
            return self.getTypedRuleContext(DSL_grammarParser.Nenule_digitContext,0)


        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.DigitContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.DigitContext,i)


        def function(self):
            return self.getTypedRuleContext(DSL_grammarParser.FunctionContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = DSL_grammarParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DSL_grammarParser.T__1, DSL_grammarParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.variable()
                pass
            elif token in [DSL_grammarParser.T__33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.string()
                pass
            elif token in [DSL_grammarParser.NENULE_DIGITS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 505
                self.nenule_digit()
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DSL_grammarParser.DIGITS:
                    self.state = 506
                    self.digit()
                    self.state = 511
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [DSL_grammarParser.T__24, DSL_grammarParser.T__27, DSL_grammarParser.T__28, DSL_grammarParser.T__29, DSL_grammarParser.T__30, DSL_grammarParser.T__31, DSL_grammarParser.T__32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composed_operandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.OperandContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.OperandContext,i)


        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DSL_grammarParser.OperationContext)
            else:
                return self.getTypedRuleContext(DSL_grammarParser.OperationContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_composed_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComposed_operand" ):
                listener.enterComposed_operand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComposed_operand" ):
                listener.exitComposed_operand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposed_operand" ):
                return visitor.visitComposed_operand(self)
            else:
                return visitor.visitChildren(self)




    def composed_operand(self):

        localctx = DSL_grammarParser.Composed_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_composed_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.operand()
            self.state = 531 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 519
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DSL_grammarParser.WHITESPACE:
                        self.state = 516
                        self.match(DSL_grammarParser.WHITESPACE)
                        self.state = 521
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 522
                    self.operation()
                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DSL_grammarParser.WHITESPACE:
                        self.state = 523
                        self.match(DSL_grammarParser.WHITESPACE)
                        self.state = 528
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 529
                    self.operand()

                else:
                    raise NoViableAltException(self)
                self.state = 533 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = DSL_grammarParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DSL_grammarParser.T__17) | (1 << DSL_grammarParser.T__18) | (1 << DSL_grammarParser.T__19) | (1 << DSL_grammarParser.T__20) | (1 << DSL_grammarParser.T__21) | (1 << DSL_grammarParser.T__22) | (1 << DSL_grammarParser.T__23))) != 0)):
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def story(self):
            return self.getTypedRuleContext(DSL_grammarParser.StoryContext,0)


        def stage(self):
            return self.getTypedRuleContext(DSL_grammarParser.StageContext,0)


        def section(self):
            return self.getTypedRuleContext(DSL_grammarParser.SectionContext,0)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(DSL_grammarParser.WHITESPACE)
            else:
                return self.getToken(DSL_grammarParser.WHITESPACE, i)

        def node(self):
            return self.getTypedRuleContext(DSL_grammarParser.NodeContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = DSL_grammarParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function)
        try:
            self.state = 614
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DSL_grammarParser.T__24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(DSL_grammarParser.T__24)
                self.state = 538
                self.match(DSL_grammarParser.T__25)
                self.state = 542
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 539
                    self.story()
                    pass

                elif la_ == 2:
                    self.state = 540
                    self.stage()
                    pass

                elif la_ == 3:
                    self.state = 541
                    self.section()
                    pass


                self.state = 544
                self.match(DSL_grammarParser.T__26)
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 545
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 550
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.match(DSL_grammarParser.T__27)
                self.state = 552
                self.match(DSL_grammarParser.T__25)
                self.state = 555
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
                if la_ == 1:
                    self.state = 553
                    self.story()
                    pass

                elif la_ == 2:
                    self.state = 554
                    self.stage()
                    pass


                self.state = 557
                self.match(DSL_grammarParser.T__26)
                self.state = 561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 558
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 563
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 564
                self.match(DSL_grammarParser.T__28)
                self.state = 565
                self.match(DSL_grammarParser.T__25)
                self.state = 566
                self.story()
                self.state = 567
                self.match(DSL_grammarParser.T__26)
                self.state = 571
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 568
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 573
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 574
                self.match(DSL_grammarParser.T__29)
                self.state = 575
                self.match(DSL_grammarParser.T__25)
                self.state = 576
                self.node()
                self.state = 577
                self.match(DSL_grammarParser.T__26)
                self.state = 581
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 578
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 583
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__30]:
                self.enterOuterAlt(localctx, 5)
                self.state = 584
                self.match(DSL_grammarParser.T__30)
                self.state = 585
                self.match(DSL_grammarParser.T__25)
                self.state = 586
                self.node()
                self.state = 587
                self.match(DSL_grammarParser.T__26)
                self.state = 591
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,84,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 588
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 593
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,84,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__31]:
                self.enterOuterAlt(localctx, 6)
                self.state = 594
                self.match(DSL_grammarParser.T__31)
                self.state = 595
                self.match(DSL_grammarParser.T__25)
                self.state = 596
                self.node()
                self.state = 597
                self.match(DSL_grammarParser.T__26)
                self.state = 601
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 598
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 603
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

                pass
            elif token in [DSL_grammarParser.T__32]:
                self.enterOuterAlt(localctx, 7)
                self.state = 604
                self.match(DSL_grammarParser.T__32)
                self.state = 605
                self.match(DSL_grammarParser.T__25)
                self.state = 606
                self.node()
                self.state = 607
                self.match(DSL_grammarParser.T__26)
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,86,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 608
                        self.match(DSL_grammarParser.WHITESPACE) 
                    self.state = 613
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,86,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNS(self):
            return self.getToken(DSL_grammarParser.SIGNS, 0)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DSL_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(DSL_grammarParser.SIGNS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def characters(self):
            return self.getTypedRuleContext(DSL_grammarParser.CharactersContext,0)


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = DSL_grammarParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.characters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharactersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DSL_grammarParser.RULE_characters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacters" ):
                listener.enterCharacters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacters" ):
                listener.exitCharacters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacters" ):
                return visitor.visitCharacters(self)
            else:
                return visitor.visitChildren(self)




    def characters(self):

        localctx = DSL_grammarParser.CharactersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_characters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            self.match(DSL_grammarParser.T__33)
            self.state = 624
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DSL_grammarParser.T__1) | (1 << DSL_grammarParser.T__2) | (1 << DSL_grammarParser.T__3) | (1 << DSL_grammarParser.T__4) | (1 << DSL_grammarParser.T__5) | (1 << DSL_grammarParser.T__6) | (1 << DSL_grammarParser.T__7) | (1 << DSL_grammarParser.T__8) | (1 << DSL_grammarParser.T__9) | (1 << DSL_grammarParser.T__10) | (1 << DSL_grammarParser.T__11) | (1 << DSL_grammarParser.T__12) | (1 << DSL_grammarParser.T__13) | (1 << DSL_grammarParser.T__14) | (1 << DSL_grammarParser.T__15) | (1 << DSL_grammarParser.T__16) | (1 << DSL_grammarParser.T__17) | (1 << DSL_grammarParser.T__18) | (1 << DSL_grammarParser.T__19) | (1 << DSL_grammarParser.T__20) | (1 << DSL_grammarParser.T__21) | (1 << DSL_grammarParser.T__22) | (1 << DSL_grammarParser.T__23) | (1 << DSL_grammarParser.T__24) | (1 << DSL_grammarParser.T__25) | (1 << DSL_grammarParser.T__26) | (1 << DSL_grammarParser.T__27) | (1 << DSL_grammarParser.T__28) | (1 << DSL_grammarParser.T__29) | (1 << DSL_grammarParser.T__30) | (1 << DSL_grammarParser.T__31) | (1 << DSL_grammarParser.T__32) | (1 << DSL_grammarParser.TYPE) | (1 << DSL_grammarParser.LETTERS) | (1 << DSL_grammarParser.DIGITS) | (1 << DSL_grammarParser.NENULE_DIGITS) | (1 << DSL_grammarParser.SIGNS) | (1 << DSL_grammarParser.NEWLINE) | (1 << DSL_grammarParser.WHITESPACE))) != 0):
                self.state = 621
                _la = self._input.LA(1)
                if _la <= 0 or _la==DSL_grammarParser.T__0 or _la==DSL_grammarParser.T__33:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 626
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 627
            self.match(DSL_grammarParser.T__33)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(DSL_grammarParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DSL_grammarParser.RULE_comments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComments" ):
                listener.enterComments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComments" ):
                listener.exitComments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComments" ):
                return visitor.visitComments(self)
            else:
                return visitor.visitChildren(self)




    def comments(self):

        localctx = DSL_grammarParser.CommentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(DSL_grammarParser.T__0)
            self.state = 630
            _la = self._input.LA(1)
            if _la <= 0 or _la==DSL_grammarParser.NEWLINE:
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





