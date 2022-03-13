# Generated from DSL_grammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2+")
        buf.write("\u012f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\5$\u010b\n$\3%\5%\u010e\n%\3&\3&\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0122\n(\3)\6)\u0125")
        buf.write("\n)\r)\16)\u0126\3)\3)\3*\6*\u012c\n*\r*\16*\u012d\2\2")
        buf.write("+\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+\3\2\7\4\2C\\c|\3\2\62;\3\2\63;\4\2>>@@\4\2\13\f")
        buf.write("\17\17\2\u013a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\3U\3\2\2\2\5W\3\2\2\2\7Y\3\2\2\2\t\\\3")
        buf.write("\2\2\2\13^\3\2\2\2\rc\3\2\2\2\17i\3\2\2\2\21m\3\2\2\2")
        buf.write("\23o\3\2\2\2\25u\3\2\2\2\27{\3\2\2\2\31\u0083\3\2\2\2")
        buf.write("\33\u0088\3\2\2\2\35\u008a\3\2\2\2\37\u008d\3\2\2\2!\u0094")
        buf.write("\3\2\2\2#\u0097\3\2\2\2%\u009a\3\2\2\2\'\u009c\3\2\2\2")
        buf.write(")\u009e\3\2\2\2+\u00a0\3\2\2\2-\u00a3\3\2\2\2/\u00a5\3")
        buf.write("\2\2\2\61\u00a8\3\2\2\2\63\u00aa\3\2\2\2\65\u00b3\3\2")
        buf.write("\2\2\67\u00b5\3\2\2\29\u00b7\3\2\2\2;\u00c3\3\2\2\2=\u00cd")
        buf.write("\3\2\2\2?\u00e0\3\2\2\2A\u00e6\3\2\2\2C\u00ec\3\2\2\2")
        buf.write("E\u00f2\3\2\2\2G\u010a\3\2\2\2I\u010d\3\2\2\2K\u010f\3")
        buf.write("\2\2\2M\u0111\3\2\2\2O\u0121\3\2\2\2Q\u0124\3\2\2\2S\u012b")
        buf.write("\3\2\2\2UV\7%\2\2V\4\3\2\2\2WX\7a\2\2X\6\3\2\2\2YZ\7k")
        buf.write("\2\2Z[\7h\2\2[\b\3\2\2\2\\]\7<\2\2]\n\3\2\2\2^_\7g\2\2")
        buf.write("_`\7n\2\2`a\7u\2\2ab\7g\2\2b\f\3\2\2\2cd\7y\2\2de\7j\2")
        buf.write("\2ef\7k\2\2fg\7n\2\2gh\7g\2\2h\16\3\2\2\2ij\7h\2\2jk\7")
        buf.write("q\2\2kl\7t\2\2l\20\3\2\2\2mn\7?\2\2n\22\3\2\2\2op\7U\2")
        buf.write("\2pq\7V\2\2qr\7Q\2\2rs\7T\2\2st\7[\2\2t\24\3\2\2\2uv\7")
        buf.write("U\2\2vw\7V\2\2wx\7C\2\2xy\7I\2\2yz\7G\2\2z\26\3\2\2\2")
        buf.write("{|\7U\2\2|}\7G\2\2}~\7E\2\2~\177\7V\2\2\177\u0080\7K\2")
        buf.write("\2\u0080\u0081\7Q\2\2\u0081\u0082\7P\2\2\u0082\30\3\2")
        buf.write("\2\2\u0083\u0084\7H\2\2\u0084\u0085\7T\2\2\u0085\u0086")
        buf.write("\7Q\2\2\u0086\u0087\7O\2\2\u0087\32\3\2\2\2\u0088\u0089")
        buf.write("\7\60\2\2\u0089\34\3\2\2\2\u008a\u008b\7V\2\2\u008b\u008c")
        buf.write("\7Q\2\2\u008c\36\3\2\2\2\u008d\u008e\7C\2\2\u008e\u008f")
        buf.write("\7E\2\2\u008f\u0090\7V\2\2\u0090\u0091\7K\2\2\u0091\u0092")
        buf.write("\7Q\2\2\u0092\u0093\7P\2\2\u0093 \3\2\2\2\u0094\u0095")
        buf.write("\7(\2\2\u0095\u0096\7(\2\2\u0096\"\3\2\2\2\u0097\u0098")
        buf.write("\7~\2\2\u0098\u0099\7~\2\2\u0099$\3\2\2\2\u009a\u009b")
        buf.write("\7-\2\2\u009b&\3\2\2\2\u009c\u009d\7/\2\2\u009d(\3\2\2")
        buf.write("\2\u009e\u009f\7,\2\2\u009f*\3\2\2\2\u00a0\u00a1\7,\2")
        buf.write("\2\u00a1\u00a2\7,\2\2\u00a2,\3\2\2\2\u00a3\u00a4\7\61")
        buf.write("\2\2\u00a4.\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\7")
        buf.write("\61\2\2\u00a7\60\3\2\2\2\u00a8\u00a9\7\'\2\2\u00a9\62")
        buf.write("\3\2\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7a\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7f\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7u\2\2\u00b2\64")
        buf.write("\3\2\2\2\u00b3\u00b4\7*\2\2\u00b4\66\3\2\2\2\u00b5\u00b6")
        buf.write("\7+\2\2\u00b68\3\2\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7t\2\2\u00b9\u00ba\7a\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2:\3\2\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5\u00c6\7a\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7i\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7u\2\2\u00cc<\3\2\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0\7a\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3\7a\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da")
        buf.write("\7e\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7u\2\2\u00df>\3")
        buf.write("\2\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7t\2\2\u00e5@\3")
        buf.write("\2\2\2\u00e6\u00e7\7y\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7f\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7j\2\2\u00ebB\3")
        buf.write("\2\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef")
        buf.write("\7{\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7g\2\2\u00f1D\3")
        buf.write("\2\2\2\u00f2\u00f3\7$\2\2\u00f3F\3\2\2\2\u00f4\u00f5\7")
        buf.write("k\2\2\u00f5\u00f6\7p\2\2\u00f6\u010b\7v\2\2\u00f7\u00f8")
        buf.write("\7h\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u010b\7v\2\2\u00fc\u00fd\7u\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u010b\7i\2\2\u0102\u0103\7e\2\2\u0103\u0104")
        buf.write("\7j\2\2\u0104\u0105\7c\2\2\u0105\u010b\7t\2\2\u0106\u0107")
        buf.write("\7d\2\2\u0107\u0108\7q\2\2\u0108\u0109\7q\2\2\u0109\u010b")
        buf.write("\7n\2\2\u010a\u00f4\3\2\2\2\u010a\u00f7\3\2\2\2\u010a")
        buf.write("\u00fc\3\2\2\2\u010a\u0102\3\2\2\2\u010a\u0106\3\2\2\2")
        buf.write("\u010bH\3\2\2\2\u010c\u010e\t\2\2\2\u010d\u010c\3\2\2")
        buf.write("\2\u010eJ\3\2\2\2\u010f\u0110\t\3\2\2\u0110L\3\2\2\2\u0111")
        buf.write("\u0112\t\4\2\2\u0112N\3\2\2\2\u0113\u0122\t\5\2\2\u0114")
        buf.write("\u0115\7@\2\2\u0115\u0122\7?\2\2\u0116\u0117\7>\2\2\u0117")
        buf.write("\u0122\7?\2\2\u0118\u0119\7?\2\2\u0119\u0122\7?\2\2\u011a")
        buf.write("\u011b\7#\2\2\u011b\u0122\7?\2\2\u011c\u011d\7k\2\2\u011d")
        buf.write("\u0122\7p\2\2\u011e\u011f\7p\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0122\7v\2\2\u0121\u0113\3\2\2\2\u0121\u0114\3\2\2\2")
        buf.write("\u0121\u0116\3\2\2\2\u0121\u0118\3\2\2\2\u0121\u011a\3")
        buf.write("\2\2\2\u0121\u011c\3\2\2\2\u0121\u011e\3\2\2\2\u0122P")
        buf.write("\3\2\2\2\u0123\u0125\t\6\2\2\u0124\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0129\b)\2\2\u0129R\3\2\2\2")
        buf.write("\u012a\u012c\7\"\2\2\u012b\u012a\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012eT")
        buf.write("\3\2\2\2\b\2\u010a\u010d\u0121\u0126\u012d\3\b\2\2")
        return buf.getvalue()


class DSL_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    TYPE = 35
    LETTERS = 36
    DIGITS = 37
    NENULE_DIGITS = 38
    SIGNS = 39
    NEWLINE = 40
    WHITESPACE = 41

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#'", "'_'", "'if'", "':'", "'else'", "'while'", "'for'", "'='", 
            "'STORY'", "'STAGE'", "'SECTION'", "'FROM'", "'.'", "'TO'", 
            "'ACTION'", "'&&'", "'||'", "'+'", "'-'", "'*'", "'**'", "'/'", 
            "'//'", "'%'", "'nr_nodes'", "'('", "')'", "'nr_sections'", 
            "'nr_stages'", "'nr_of_interactions'", "'color'", "'width'", 
            "'style'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "LETTERS", "DIGITS", "NENULE_DIGITS", "SIGNS", "NEWLINE", 
            "WHITESPACE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "TYPE", "LETTERS", "DIGITS", "NENULE_DIGITS", 
                  "SIGNS", "NEWLINE", "WHITESPACE" ]

    grammarFileName = "DSL_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


