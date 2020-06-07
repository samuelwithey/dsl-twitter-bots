# Final Year Project
A domain specific language designed to operate and automate Twitter accounts/bots using Tweepy API.
## Domain Specific Language Grammar
## Setting up the virtual-env
```bash
cd web-application/dsl_bots/
. ./activate
```
## Running management commands to execute the domain specific language
- Create a Twitter Account in Django admin
- Create a Twitter Campagin in Django admin and upload dsl script as `.txt` file
- Use Ubuntu terminal to execute the Django management command
```bash
python manage.py execute_dsl --account-id {id-number} --campaign-id {id-number}
```
## Generating ANTLR files
```bash
cd web-application/dsl_bots/core/dsl/antlr4/
module load ./antlr4module
antlr4py3 -visitor dsl.g4
antlr4py3 dslLexerGrammar.g4
antrl4py3 NumericLexer.g4
```
## Running unit tests
```bash
cd web-application/dsl_bots
# Run all unit tests
./manage.py test core.tests
# Run TwitterAccountCampaignUploadTest class
./manage.py test core.tests.TwitterAccountCampaignUploadTest
# Run DSLParsingTest class
./manage.py test core.tests.DSLParsingTest
# Run DSLVisitorWalkerAPITests class
./manage.py test core.tests.DSLVisitorWalkerAPITests
# Run BotScriptTest class, will require Control-C to kill process
./manage.py test core.tests.BotScriptTest
```
## Running Domain Specific Language token example
```bash
cd web-application/dsl_bots/core/dsl/dsl_source_files/
echo tweet status : "Testing tokens" \; > input.txt
pygrun dsl twitbot --tokens input.txt
```
