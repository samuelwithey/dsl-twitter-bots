lexer grammar dslLexerGrammar;

import NumericLexer ;

StringLiteral
  : UnterminatedStringLiteral '"' {self.text = self.text[1:-1]}
  ;

UnterminatedStringLiteral
  : '"' (~["\\\r\n] | '\\' (. | EOF))*
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
    : 'automate_time_minutes'
    ;

MINUTE
    : 'minute'
    ;

HOUR
    : 'hour'
    ;

MONTH
    : 'month'
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

DAY_OF_MONTH
    : 'day_of_month'
    ;

AUTO_FAV_RETWEET
    : 'automate_favourites_retweets'
    ;

RECIPIENT_ID
    : 'recipient_id'
    ;
