lexer grammar dslLexerGrammar;

StringLiteral
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;
COMMA : ',' ;
SEMICOLON : ';' ;
COLON : ':' ;
WS  :   [ \t\n\r]+ -> skip;