grammar PythonGrammar ;
start: (expr NEWLINE)*;
expr : expr ('*' | '/') expr
     | expr ('+' | '-') expr
     | INT
     | '(' expr ')'
     | printRule;


NEWLINE: [\n]+ ;
INT    : [0-9]+ ;
