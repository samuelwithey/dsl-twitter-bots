lexer grammar dslLexerGrammar;

StringLiteral
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;

ACTION: 'tweet' | 'retweet' | 'reply' | 'favourite' | 'schedule' | 'direct-message' ;

IDENTIFIER: [A-Za-z0-9]+ ;

COMMA : ',' ;

SEMICOLON : ';' ;

COLON : ':' ;

WS  :   [ \t\n\r]+ -> skip;