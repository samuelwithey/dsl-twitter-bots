from django.contrib import admin

from core.models import TwitterAccount, TwitterCampaign, ScheduledPost


class TwitterAccountAdmin(admin.ModelAdmin):
    fields = ['username', 'consumer_key', 'consumer_secret_key', 'access_token', 'access_token_secret']
    list_display = ['username']


class TwitterCampaignAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'twitter_account', 'dsl_program_upload', 'image_upload']
    list_display = ['name', 'description', 'twitter_account', 'dsl_program_upload', 'image_upload']


class ScheduledPostAdmin(admin.ModelAdmin):
    fields = ['campaign_name', 'status', 'scheduled_time']
    list_display = ['campaign_name', 'status', 'scheduled_time']


admin.site.register(TwitterAccount, TwitterAccountAdmin)
admin.site.register(TwitterCampaign, TwitterCampaignAdmin)
admin.site.register(ScheduledPost, ScheduledPostAdmin)
