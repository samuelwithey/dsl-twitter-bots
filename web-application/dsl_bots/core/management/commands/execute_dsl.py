from django.core import management
from django.core.management.base import BaseCommand

from core.execute import Execute
from core.models import TwitterAccount, TwitterCampaign


class Command(BaseCommand):
    help = "Execute dsl commands through management commands"

    def add_arguments(self, parser):
        parser.add_argument('--account-id', type=int)
        parser.add_argument('--campaign-id', type=int)

    def execute(self, **options):
        account = TwitterAccount.objects.get(id=options['account_id'])
        campaign = TwitterCampaign.objects.get(id=options['campaign_id'])
        execute = Execute(account=account, campaign=campaign)
        api = execute.tweepy_auth()
        parser = execute.build_lexer_parser()
        tree = execute.build_tree(parser=parser)
        execute.traverse_tree(tree=tree, api=api)
