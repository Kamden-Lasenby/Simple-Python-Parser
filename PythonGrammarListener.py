# Generated from PythonGrammar.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonGrammarParser import PythonGrammarParser
else:
    from PythonGrammarParser import PythonGrammarParser

# This class defines a complete listener for a parse tree produced by PythonGrammarParser.
class PythonGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PythonGrammarParser#start.
    def enterStart(self, ctx:PythonGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#start.
    def exitStart(self, ctx:PythonGrammarParser.StartContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#decl.
    def enterDecl(self, ctx:PythonGrammarParser.DeclContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#decl.
    def exitDecl(self, ctx:PythonGrammarParser.DeclContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#expr.
    def enterExpr(self, ctx:PythonGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#expr.
    def exitExpr(self, ctx:PythonGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#conditional.
    def enterConditional(self, ctx:PythonGrammarParser.ConditionalContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#conditional.
    def exitConditional(self, ctx:PythonGrammarParser.ConditionalContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonGrammarParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonGrammarParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#elif_stmt.
    def enterElif_stmt(self, ctx:PythonGrammarParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#elif_stmt.
    def exitElif_stmt(self, ctx:PythonGrammarParser.Elif_stmtContext):
        pass



del PythonGrammarParser