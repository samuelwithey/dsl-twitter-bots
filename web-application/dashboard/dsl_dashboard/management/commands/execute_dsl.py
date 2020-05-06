from django.core import management
from django.core.management.base import BaseCommand

from dsl_dashboard.models import TwitterAccount, TwitterCampaign


class Command(BaseCommand):
    help = "Execute dsl commands through management commands"

    def add_arguments(self, parser):
        parser.add_argument('--account-id', type=int)
        parser.add_argument('--campaign-id', type=int)

    def get_account(self, account_id):
        return TwitterAccount.objects.get(id=account_id)

    def get_campaign(self, account, campaign_id):
        return TwitterCampaign.objects.get(twitter_account=account).filter(id=campaign_id)

    def execute(self):
        account = self.get_account(account_id=options['account_id'])
        campaign = self.get_campaign(account=account, campaign_id=options['campaign_id'])