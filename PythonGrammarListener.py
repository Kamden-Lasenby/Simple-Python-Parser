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


    # Enter a parse tree produced by PythonGrammarParser#block.
    def enterBlock(self, ctx:PythonGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#block.
    def exitBlock(self, ctx:PythonGrammarParser.BlockContext):
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


    # Enter a parse tree produced by PythonGrammarParser#else_stmt.
    def enterElse_stmt(self, ctx:PythonGrammarParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#else_stmt.
    def exitElse_stmt(self, ctx:PythonGrammarParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonGrammarParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonGrammarParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonGrammarParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonGrammarParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#parameters.
    def enterParameters(self, ctx:PythonGrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#parameters.
    def exitParameters(self, ctx:PythonGrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by PythonGrammarParser#function_def.
    def enterFunction_def(self, ctx:PythonGrammarParser.Function_defContext):
        pass

    # Exit a parse tree produced by PythonGrammarParser#function_def.
    def exitFunction_def(self, ctx:PythonGrammarParser.Function_defContext):
        pass



del PythonGrammarParser