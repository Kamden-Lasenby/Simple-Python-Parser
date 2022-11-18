import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from PythonGrammarLexer import PythonGrammarLexer
from PythonGrammarParser import PythonGrammarParser


def main(argv):
    # io_stream = FileStream(argv[1])

    if len(sys.argv) > 1:
        io_stream = FileStream(sys.argv[1])
    else:
        io_stream = InputStream(sys.stdin.readline())

    lexer = PythonGrammarLexer(io_stream)
    tokens = CommonTokenStream(lexer)
    parser = PythonGrammarParser(tokens)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)


