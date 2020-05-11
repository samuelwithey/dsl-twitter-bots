import tweepy


class Execute:

    def __init__(self, account, campaign):
        self.account = account
        self.campaign = campaign

    def get_consumer_key(self, account):
        return account.consumer_key

    def get_consumer_secret_key(self, account):
        return account.consumer_secret_key

    def get_access_token(self, account):
        return account.access_token

    def get_access_token_secret(self, account):
        return account.access_token_secret

    def tweepy_auth(self):
        auth = tweepy.OAuthHandler(self.get_consumer_key(self.account), self.get_consumer_secret_key(self.account))
        auth.set_access_token(self.get_access_token(account=self.account), self.get_access_token_secret(account=self.account))
        return tweepy.API(auth)