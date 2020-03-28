from django.db import models


class TwitterAccount(models.Model):
    username = models.CharField(max_length=200)
    consumer_key = models.CharField(max_length=200)
    consumer_secret_key = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class TwitterCampaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    twitter_account = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE, related_name='twitter_account')

    def __str__(self):
        return self.name


class ScheduledPost(models.Model):
    campaign_name = models.ForeignKey(TwitterCampaign, on_delete=models.CASCADE, related_name='campaign_name')
    status = models.CharField(max_length=240)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.campaign_name
