# Simple-Python-Parser
Hi this is a really simple python parser made using the ANTLR4 framework. To run this repository you'll need the latest antlr4 jar as well as the python runtime tools associated with that jar.__

In this antlr4 project I am running the antlr-4.9.2-complete.jar file and the corresponding version for the python runtime tools. The project WILL NOT work if any or all dependencies are in different versions. You find out the hard way.__

To generate your parser and lexer for your grammer you can run antlr4 -Dlanguage=Python3 PythonGrammar.g4 the grammar file will be included in the repository.__

After that you should be able to run the python script
antlr_project.py, type in your python example syntax, and it will print out the correspoding parsed grammar tree.__

Video Demo: https://youtu.be/ambWsu9_qtU
