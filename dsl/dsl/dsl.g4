grammar dsl;

import dslLexerGrammar;

twitbot: (stat SEMICOLON )* ;

stat: action parameter (COMMA parameter)* ;

action: ACTION ;

parameter: IDENTIFIER COLON StringLiteral ;