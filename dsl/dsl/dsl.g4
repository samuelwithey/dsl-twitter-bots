grammar dsl;

twitbot: (stat ';' )* ;

stat: action parameter (',' parameter)* ;

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

fragment CHAR_NO_NL : 'a'..'z'|'A'..'Z'|'\t'|'\\'|EOF;

COMMA : ',' ;

SEMICOLON : ';' ;

WS  :   [ \t\n\r]+ -> skip ;




