grammar dsl;

twitbot: (stat SEMICOLON )* ;

stat: action parameter (COMMA parameter)* ;

action
   :   'tweet'
   |   'retweet'
   |   'reply'
   |   'login'
   |   'favourite'
   |   'schedule-tweet'
   |   'direct-message'
   ;

parameter:   STRING ':' STRING ;

STRING : '"' CHAR_NO_NL* '"' ;

fragment CHAR_NO_NL : 'a'..'z'|'A'..'Z'|'0'..'9'|'\t'|'\\'|EOF;

COMMA : ',' ;

SEMICOLON : ';' ;

WS  :   [ \t\n\r]+ -> skip ;