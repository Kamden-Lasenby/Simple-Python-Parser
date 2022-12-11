# Generated from PythonGrammar.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\"\n\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4\63")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5H\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6V\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7d\n\7\3\7\2\3")
        buf.write("\6\b\2\4\6\b\n\f\2\5\3\2\4\5\3\2\6\7\4\2\3\3\t\f\2q\2")
        buf.write("\20\3\2\2\2\4\26\3\2\2\2\6!\3\2\2\2\bG\3\2\2\2\nU\3\2")
        buf.write("\2\2\fc\3\2\2\2\16\21\5\4\3\2\17\21\5\6\4\2\20\16\3\2")
        buf.write("\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3")
        buf.write("\2\2\2\23\24\3\2\2\2\24\25\7\2\2\3\25\3\3\2\2\2\26\27")
        buf.write("\7\33\2\2\27\30\7\3\2\2\30\31\7\32\2\2\31\5\3\2\2\2\32")
        buf.write("\33\b\4\1\2\33\"\7\32\2\2\34\"\7\33\2\2\35\36\7\r\2\2")
        buf.write("\36\37\5\6\4\2\37 \7\16\2\2 \"\3\2\2\2!\32\3\2\2\2!\34")
        buf.write("\3\2\2\2!\35\3\2\2\2\"\61\3\2\2\2#$\f\t\2\2$%\t\2\2\2")
        buf.write("%\60\5\6\4\n&\'\f\b\2\2\'(\t\3\2\2(\60\5\6\4\t)*\f\7\2")
        buf.write("\2*+\7\b\2\2+\60\5\6\4\b,-\f\6\2\2-.\t\4\2\2.\60\5\6\4")
        buf.write("\7/#\3\2\2\2/&\3\2\2\2/)\3\2\2\2/,\3\2\2\2\60\63\3\2\2")
        buf.write("\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2\2\2\63\61\3\2\2")
        buf.write("\2\64H\3\2\2\2\65\66\7\33\2\2\66\67\7\17\2\2\67H\7\33")
        buf.write("\2\289\7\33\2\29:\7\20\2\2:H\7\33\2\2;<\7\33\2\2<=\7\21")
        buf.write("\2\2=H\7\33\2\2>?\7\33\2\2?@\7\22\2\2@H\7\33\2\2AB\7\33")
        buf.write("\2\2BC\7\23\2\2CH\7\33\2\2DE\7\33\2\2EF\7\24\2\2FH\7\33")
        buf.write("\2\2G\64\3\2\2\2G\65\3\2\2\2G8\3\2\2\2G;\3\2\2\2G>\3\2")
        buf.write("\2\2GA\3\2\2\2GD\3\2\2\2H\t\3\2\2\2IV\3\2\2\2JK\7\25\2")
        buf.write("\2KL\5\b\5\2LM\7\26\2\2MN\5\6\4\2NV\3\2\2\2OP\7\25\2\2")
        buf.write("PQ\5\b\5\2QR\7\26\2\2RS\5\6\4\2ST\5\f\7\2TV\3\2\2\2UI")
        buf.write("\3\2\2\2UJ\3\2\2\2UO\3\2\2\2V\13\3\2\2\2Wd\3\2\2\2XY\7")
        buf.write("\27\2\2YZ\5\b\5\2Z[\7\26\2\2[\\\5\6\4\2\\d\3\2\2\2]^\7")
        buf.write("\27\2\2^_\5\b\5\2_`\7\30\2\2`a\5\6\4\2ab\5\f\7\2bd\3\2")
        buf.write("\2\2cW\3\2\2\2cX\3\2\2\2c]\3\2\2\2d\r\3\2\2\2\n\20\22")
        buf.write("!/\61GUc")
        return buf.getvalue()


class PythonGrammarParser ( Parser ):

    grammarFileName = "PythonGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'%'", 
                     "'+='", "'-='", "'*='", "'/='", "'('", "')'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'if'", "':'", 
                     "'elif'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "INT", "ID", "WS" ]

    RULE_start = 0
    RULE_decl = 1
    RULE_expr = 2
    RULE_conditional = 3
    RULE_if_stmt = 4
    RULE_elif_stmt = 5

    ruleNames =  [ "start", "decl", "expr", "conditional", "if_stmt", "elif_stmt" ]

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
    NEWLINE=23
    INT=24
    ID=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PythonGrammarParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.DeclContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.DeclContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = PythonGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.expr(0)
                    pass


                self.state = 16 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonGrammarParser.T__10) | (1 << PythonGrammarParser.INT) | (1 << PythonGrammarParser.ID))) != 0)):
                    break

            self.state = 18
            self.match(PythonGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PythonGrammarParser.ID, 0)

        def INT(self):
            return self.getToken(PythonGrammarParser.INT, 0)

        def getRuleIndex(self):
            return PythonGrammarParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = PythonGrammarParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(PythonGrammarParser.ID)
            self.state = 21
            self.match(PythonGrammarParser.T__0)
            self.state = 22
            self.match(PythonGrammarParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PythonGrammarParser.INT, 0)

        def ID(self):
            return self.getToken(PythonGrammarParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonGrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PythonGrammarParser.INT]:
                self.state = 25
                self.match(PythonGrammarParser.INT)
                pass
            elif token in [PythonGrammarParser.ID]:
                self.state = 26
                self.match(PythonGrammarParser.ID)
                pass
            elif token in [PythonGrammarParser.T__10]:
                self.state = 27
                self.match(PythonGrammarParser.T__10)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(PythonGrammarParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 45
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = PythonGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(_la==PythonGrammarParser.T__1 or _la==PythonGrammarParser.T__2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = PythonGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==PythonGrammarParser.T__3 or _la==PythonGrammarParser.T__4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = PythonGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 40
                        self.match(PythonGrammarParser.T__5)
                        self.state = 41
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = PythonGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 43
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PythonGrammarParser.T__0) | (1 << PythonGrammarParser.T__6) | (1 << PythonGrammarParser.T__7) | (1 << PythonGrammarParser.T__8) | (1 << PythonGrammarParser.T__9))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(5)
                        pass

             
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PythonGrammarParser.ID)
            else:
                return self.getToken(PythonGrammarParser.ID, i)

        def getRuleIndex(self):
            return PythonGrammarParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = PythonGrammarParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditional)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(PythonGrammarParser.ID)
                self.state = 52
                self.match(PythonGrammarParser.T__12)
                self.state = 53
                self.match(PythonGrammarParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(PythonGrammarParser.ID)
                self.state = 55
                self.match(PythonGrammarParser.T__13)
                self.state = 56
                self.match(PythonGrammarParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(PythonGrammarParser.ID)
                self.state = 58
                self.match(PythonGrammarParser.T__14)
                self.state = 59
                self.match(PythonGrammarParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.match(PythonGrammarParser.ID)
                self.state = 61
                self.match(PythonGrammarParser.T__15)
                self.state = 62
                self.match(PythonGrammarParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.match(PythonGrammarParser.ID)
                self.state = 64
                self.match(PythonGrammarParser.T__16)
                self.state = 65
                self.match(PythonGrammarParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.match(PythonGrammarParser.ID)
                self.state = 67
                self.match(PythonGrammarParser.T__17)
                self.state = 68
                self.match(PythonGrammarParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(PythonGrammarParser.ConditionalContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExprContext,0)


        def elif_stmt(self):
            return self.getTypedRuleContext(PythonGrammarParser.Elif_stmtContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = PythonGrammarParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_stmt)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(PythonGrammarParser.T__18)
                self.state = 73
                self.conditional()
                self.state = 74
                self.match(PythonGrammarParser.T__19)
                self.state = 75
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(PythonGrammarParser.T__18)
                self.state = 78
                self.conditional()
                self.state = 79
                self.match(PythonGrammarParser.T__19)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(PythonGrammarParser.ConditionalContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonGrammarParser.ExprContext,0)


        def elif_stmt(self):
            return self.getTypedRuleContext(PythonGrammarParser.Elif_stmtContext,0)


        def getRuleIndex(self):
            return PythonGrammarParser.RULE_elif_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_stmt" ):
                listener.enterElif_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_stmt" ):
                listener.exitElif_stmt(self)




    def elif_stmt(self):

        localctx = PythonGrammarParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elif_stmt)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(PythonGrammarParser.T__20)
                self.state = 87
                self.conditional()
                self.state = 88
                self.match(PythonGrammarParser.T__19)
                self.state = 89
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(PythonGrammarParser.T__20)
                self.state = 92
                self.conditional()
                self.state = 93
                self.match(PythonGrammarParser.T__21)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




