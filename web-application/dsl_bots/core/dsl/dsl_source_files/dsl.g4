grammar dsl;

import dslLexerGrammar;

twitbot
    : (stat SEMICOLON)+
    ;

stat
    : action
    ;

action
    : tweet
    | tweetImage
    | reply
    | retweet
    | favourite
    | scheduleTweet
    | directMessage
    | autoFavouriteRetweet
    | autoFollowFollowers
    | autoReplyMentions
    ;

tweet
    : TWEET tweet_required_parameter (COMMA tweet_optional_parameters)*
    ;

tweet_required_parameter
    : STATUS COLON stringValue
    ;

tweet_optional_parameters
    :  POSSIBLY_SENSITIVE COLON boolean
    |  LAT COLON number
    |  LONG COLON number
    |  PLACE_ID COLON stringValue
    |  DISPLAY_COORDINATES COLON boolean
    ;

tweetImage
    : TWEET_IMAGE tweet_required_parameter (COMMA tweet_image_required_parameter)+ (COMMA tweet_optional_parameters)*
    ;

tweet_image_required_parameter
    : IMAGE_NAME COLON stringValue
    ;

reply
    : REPLY reply_required_parameters (COMMA tweet_image_required_parameter)* (COMMA tweet_optional_parameters)*
    ;

reply_required_parameters
    : REPLY_ID COLON number COMMA STATUS COLON stringValue
    ;

retweet
    : RETWEET retweet_required_parameter
    ;

retweet_required_parameter
    : ID COLON number
    ;

favourite
    : FAVOURITE favourite_required_parameter
    ;

favourite_required_parameter
    : ID COLON number
    ;

scheduleTweet
    : SCHEDULE schedule_tweet_required_parameter
    ;

schedule_tweet_required_parameter
    : date_time_parameter COMMA tweet
    ;

date_time_parameter
    : minute COMMA hour COMMA day_of_month COMMA month
    ;

minute
    : MINUTE COLON numeric_minute
    ;

hour
    : HOUR COLON numeric_hour
    ;

day_of_month
    : DAY_OF_MONTH COLON numeric_day
    ;

month
    : MONTH COLON numeric_month
    ;

numeric_month
    : INT_1  | INT_2  | INT_3  | INT_4  | INT_5  | INT_6  | INT_7  | INT_8  | INT_9
    | INT_01 | INT_02 | INT_03 | INT_04 | INT_05 | INT_06 | INT_07 | INT_08 | INT_09
    | INT_10 | INT_11 | INT_12
    ;

numeric_day
    : INT_1  | INT_2  | INT_3  | INT_4  | INT_5  | INT_6  | INT_7  | INT_8  | INT_9
    | INT_01 | INT_02 | INT_03 | INT_04 | INT_05 | INT_06 | INT_07 | INT_08 | INT_09
    | INT_10 | INT_11 | INT_12 | INT_13 | INT_14 | INT_15 | INT_16 | INT_17 | INT_18
    | INT_19 | INT_20 | INT_21 | INT_22 | INT_23 | INT_24 | INT_25 | INT_26 | INT_27
    | INT_28 | INT_29 | INT_30 | INT_31
    ;

numeric_hour
    : INT_01 | INT_02 | INT_03 | INT_04 | INT_05 | INT_06 | INT_07 | INT_08 | INT_09
    | INT_1  | INT_2  | INT_3  | INT_4  | INT_5  | INT_6  | INT_7  | INT_8  | INT_9
    | INT_10 | INT_11 | INT_12 | INT_13 | INT_14 | INT_15 | INT_16 | INT_17 | INT_18
    | INT_19 | INT_20 | INT_21 | INT_22 | INT_23 | INT_24 | INT_00
    ;

numeric_minute
    : INT_01 | INT_02 | INT_03 | INT_04 | INT_05 | INT_06 | INT_07 | INT_08 | INT_09
    | INT_1  | INT_2  | INT_3  | INT_4  | INT_5  | INT_6  | INT_7  | INT_8  | INT_9
    | INT_10 | INT_11 | INT_12 | INT_13 | INT_14 | INT_15 | INT_16 | INT_17 | INT_18
    | INT_19 | INT_20 | INT_21 | INT_22 | INT_23 | INT_24 | INT_25 | INT_26 | INT_27
    | INT_28 | INT_29 | INT_30 | INT_31 | INT_32 | INT_33 | INT_34 | INT_35 | INT_36
    | INT_37 | INT_38 | INT_39 | INT_40 | INT_41 | INT_42 | INT_43 | INT_44 | INT_45
    | INT_46 | INT_47 | INT_48 | INT_49 | INT_50 | INT_51 | INT_52 | INT_53 | INT_54
    | INT_55 | INT_56 | INT_57 | INT_58 | INT_59 | INT_00
    ;

directMessage
    : DIRECT_MESSAGE direct_message_required_parameters
    ;

direct_message_required_parameters
    : RECIPIENT_ID COLON number COMMA TEXT COLON stringValue
    ;

autoFavouriteRetweet
    : AUTO_FAV_RETWEET keyword (COMMA keyword)*
    ;

autoFollowFollowers
    : FOLLOWALL
    ;

autoReplyMentions
    :   AUTOMATE_REPLY_MENTIONS automateReplyParameter (COMMA keyword)+
    ;

automateReplyParameter
    :   AUTOMATE_TIME COLON numeric_minute COMMA RESPONSE COLON stringValue
    ;

keyword
    :   KEYWORD COLON stringValue
    ;

stringValue
    : StringLiteral
    ;

number
    : unary_operator? unsigned_number
    ;

unary_operator
    : '+'
    | '-'
    ;

unsigned_number
    : UNSIGNED_INT
    | UNSIGNED_FLOAT
    ;

boolean
    : TRUE
    | FALSE
    ;