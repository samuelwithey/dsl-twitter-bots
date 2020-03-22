grammar dsl;

import dslLexerGrammar;

twitbot: (stat SEMICOLON )* ;

stat: action parameter (COMMA parameter)* ;

action: ACTION ;

parameter: identifier COLON string ;

identifier : IDENTIFIER ;

string : StringLiteral ;