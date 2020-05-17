grammar dsl;

import dslLexerGrammar;

twitbot: stat SEMICOLON (stat SEMICOLON )* ;

stat: action parameter (COMMA parameter)* ;

action: Action ;

parameter: identifier COLON value ;

identifier : Identifier ;

value : StringLiteral ;