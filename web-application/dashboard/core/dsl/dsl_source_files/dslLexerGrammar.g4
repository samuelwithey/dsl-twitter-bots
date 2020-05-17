lexer grammar dslLexerGrammar;

StringLiteral
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;

ID: 'id' ;

Tweet: 'tweet' ;

Status: 'status' ;

Reply: 'reply' ;

Retweet: 'retweet' ;

Direct_message: 'direct_message' ;

Favourite: 'favourite' ;

Schedule: 'schedule' ;

Tweet_parameter: 'attachment_url' | 'possibly_sensitive' | 'lat' | 'long' | 'place_id' | 'display_coordinates' ;

Date_time: 'date_time' ;

Text: 'text' ;

Identifier: [A-Za-z0-9]+ ;

COMMA : ',' ;

SEMICOLON : ';' ;

COLON : ':' ;

WS  :   [ \t\n\r]+ -> skip;