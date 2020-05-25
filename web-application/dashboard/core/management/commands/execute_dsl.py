from django.core import management
from django.core.management.base import BaseCommand

from core.execute import Execute
from core.models import TwitterAccount, TwitterCampaign


class Command(BaseCommand):
    help = "Execute dsl commands through management commands"

    def add_arguments(self, parser):
        parser.add_argument('--account-id', type=int)
        parser.add_argument('--campaign-id', type=int)

    def get_account(self, account_id):
        return TwitterAccount.objects.get(id=account_id)

    def get_campaign(self, campaign_id):
        return TwitterCampaign.objects.get(id=campaign_id)

    def execute(self, **options):
        account = self.get_account(account_id=options['account_id'])
        campaign = self.get_campaign(campaign_id=options['campaign_id'])
        execute = Execute(campaign=campaign, account=account)
        parser = execute.build_lexer_parser()
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree)
