grammar PythonGrammar ;
// INDENT DEDENT
tokens { INDENT, DEDENT }
//START VARIABLE
start: (decl | expr)+ EOF;

//PRODUCTIONS
decl: ID '=' INT;

expr : expr ('*' | '/') expr
     | expr ('+' | '-') expr
     | expr ('%') expr
     | expr ('=' | '+=' | '-=' | '*=' | '/=') expr
     | INT
     | ID
     | '(' expr ')';

conditional:
     | ID '<' ID
     | ID '>' ID
     | ID '<=' ID
     | ID '>=' ID
     | ID '==' ID
     | ID '!=' ID;

block: NEWLINE INDENT expr DEDENT;

if_stmt:
     | 'if' conditional ':' block
     | 'if' conditional ':' block elif_stmt
     | 'if' conditional ':' block else_stmt;

elif_stmt:
     | 'elif' conditional ':' block
     | 'elif' conditional ';' block elif_stmt
     | 'elif' conditional ';' block else_stmt;

else_stmt:
     | 'else' block;

while_stmt: 'while' conditional ':' block;

for_stmt: 'for' expr 'in' expr ':' block;



//TOKENS
NEWLINE: [\n]+;
INT    : [0-9]+ | '-'[1-9]*;
ID : [a-z][a-zA-Z0-9_]*; // identifiers
WS : [ \t\n]+ -> skip;
COMMENT : '#' ~[\r\n]* -> skip; // single line comments


