lexer grammar dslLexerGrammar;

Login: 'login' ;

LoginIdentifier : 'consumer-key' | 'consumer-secret' | 'access-token' | 'access-token-secret' ;

StringLiteral
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;

Action: 'tweet' | 'retweet' | 'reply' | 'favourite' | 'schedule' | 'direct-message' ;

Identifier: [A-Za-z0-9]+ ;

COMMA : ',' ;

SEMICOLON : ';' ;

COLON : ':' ;

WS  :   [ \t\n\r]+ -> skip;