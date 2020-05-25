lexer grammar dslLexerGrammar;

import NumericLexer ;

StringLiteral
  : UnterminatedStringLiteral '"'
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
  ;

UNSIGNED_INT
    : ('0' | '1'..'9' '0'..'9'*)
    ;

UNSIGNED_FLOAT
    :   ('0'..'9')+ '.' ('0'..'9')*
    ;

LAT
    : 'lat'
    ;

TRUE
    : 'True'
    ;

FALSE
    : 'False'
    ;

ID
    : 'id'
    ;

TWEET
    : 'tweet'
    ;

REPLY_ID
    : 'in_reply_to_status_id'
    ;

STATUS
    : 'status'
    ;

POSSIBLY_SENSITIVE
    : 'possibly_sensitive'
    ;

LONG
    : 'long'
    ;

PLACE_ID
    : 'place_id'
    ;

DISPLAY_COORDINATES
    : 'display_coordinates'
    ;

REPLY
    : 'reply'
    ;

RETWEET
    : 'retweet'
    ;

DIRECT_MESSAGE
    : 'direct_message'
    ;

FAVOURITE
    : 'favourite'
    ;

SCHEDULE
    : 'schedule'
    ;

DATE
    : 'date'
    ;

TIME
    : 'time'
    ;

TEXT
    : 'text'
    ;

COMMA
    : ','
    ;

SEMICOLON
    : ';'
    ;

COLON
    : ':'
    ;

KEYWORD
    : 'keyword'
    ;

FOLLOWALL
    : 'follow_all_followers'
    ;

AUTOMATE_TIME
    : 'automate_time'
    ;

RESPONSE
    : 'response'
    ;

AUTOMATE_REPLY_MENTIONS
    : 'automate_reply_to_mentions'
    ;

WS
    : [ \t\n\r]+ -> skip
    ;

SLASH
    : '/'
    ;

DOT
    : '.'
    ;