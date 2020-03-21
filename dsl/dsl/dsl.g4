grammar dsl;

import dslLexerGrammar;

twitbot: (stat SEMICOLON )* ;

stat: action parameter (COMMA parameter)* ;

action: StringLiteral ;

parameter:   StringLiteral COLON StringLiteral ;

COMMA : ',' ;
SEMICOLON : ';' ;
COLON : ':' ;