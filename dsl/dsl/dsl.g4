grammar dsl;

import dslLexerGrammar;

twitbot: login_stat SEMICOLON (stat SEMICOLON )* ;

login_stat: login login_parameter COMMA login_parameter COMMA login_parameter COMMA login_parameter ;

login: Login ;

login_parameter: login_identifier COLON value ;

login_identifier : LoginIdentifier ;

stat: action parameter (COMMA parameter)* ;

action: Action ;

parameter: identifier COLON value ;

identifier : Identifier ;

value : StringLiteral ;