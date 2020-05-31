# Final Year Project
A domain specific language designed to operate and automate Twitter accounts/bots using Tweepy API.
## Domain Specific Language design and scripts
- The domain specific language is designed to be one or more statements followed by semi-colon after each statement.
- Each statement consists of an action (tweet, retweet, reply, favourite, schedule, direct-message) followed by 1 or more parameters.
- Each parameter consists of an identifier, colon and value as a string.
## Setting up the virtual-env
```bash
git clone https://github.com/samuelwithey/final-year-project.git
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
## Generating ANTLR files and running dsl using Ubuntu Terminal (optional)
```bash
cd web-application/dsl_bots/core/dsl/antlr4/
module load ./antlr4module
antlr4py3 dsl.g4
pygrun dsl twitbot --tokens input.txt
```
