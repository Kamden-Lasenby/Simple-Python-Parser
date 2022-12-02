grammar PythonGrammar ;
start: (expr NEWLINE)*;

statements: statement+;

statement: compound_stmt | simple_stmts;

simple_stmts:
     | ';'.simple_stmt+ [';'] NEWLINE;

simple_stmt:
     | assignment;

compound_stmt:
     | if_stmt;

expr : expr ('*' | '/') expr
     | expr ('+' | '-') expr
     | expr ('%') expr
     | expr ('=' | '+=' | '-=' | '*=' | '/=') expr
     | INT
     | '(' expr ')';


NEWLINE: [\n]+ ;
INT    : [0-9]+ ;

block:
     | NEWLINE INDENT statements DEDENT
     | simple_stmts;

if_stmt:
     | 'if' expr ':' block elif_stmt
     | 'if' expr ':' block [elif_block];
elif_stmt:
     | 'elif' expr ':' block elif_stmt
     | 'elif' expr ':' block [else_block];
else_block:
     | 'else' ';' block;
