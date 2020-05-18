grammar dsl;

import dslLexerGrammar;

twitbot: stat SEMICOLON ( stat SEMICOLON )* ;

stat: action ;

// List of possible actions
action  : tweet
        | reply
        | retweet
        | favourite
        | schedule
        | direct_message
        ;

// Tweet action
tweet : Tweet tweet_required_parameter (COMMA tweet_optional_parameter)* ;
tweet_required_parameter : status COLON value ;
status: Status ;
tweet_optional_parameter: tweet_parameter COLON value ;
tweet_parameter: Tweet_parameter ;

// Reply action
reply: Reply reply_required_parameter (COMMA tweet_optional_parameter)* ;
reply_required_parameter: account_id COLON value COMMA status COLON value ;
account_id: ID ;

// Retweet action
retweet: Retweet retweet_required_parameter ;
retweet_required_parameter: retweet_id COLON value ;
retweet_id: ID ;

// Favourite action
favourite: Favourite favourite_required_parameter ;
favourite_required_parameter: account_id COLON value;

// Schedule action
schedule: Schedule schedule_required_parameter ;
schedule_required_parameter: date_time COLON value COMMA tweet ;
date_time: Date_time ;

// Direct_message action
direct_message: Direct_message direct_message_required_parameter ;
direct_message_required_parameter: recipient_id COLON value COMMA text COLON value ;
recipient_id: ID ;
text: Text ;

// Value
value: StringLiteral;