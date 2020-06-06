from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/campaign_<name>/filename
    return 'user_{0}/{1}/file/{2}'.format(instance.twitter_account.id, instance, filename)


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
    dsl_program_upload = models.FileField(upload_to=user_directory_path)
    image_upload = models.ImageField(upload_to=user_directory_path, blank=True)
    twitter_account = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE, related_name='twitter_account')

