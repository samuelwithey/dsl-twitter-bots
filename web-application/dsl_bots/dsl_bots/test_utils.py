import random
import string

from core.models import TwitterAccount, TwitterCampaign


def set_if_not_present(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value


def create_twitter_account(**kwargs):
    d = kwargs.copy()
    set_if_not_present(d, 'username', '@dev_project_dsl')
    with open('core/api_keys.txt', 'r') as file:
        data = file.read().splitlines()
    set_if_not_present(d, 'consumer_key', data[0])
    set_if_not_present(d, 'consumer_secret_key', data[1])
    set_if_not_present(d, 'access_token', data[2])
    set_if_not_present(d, 'access_token_secret', data[3])
    return TwitterAccount.objects.get_or_create(**d)[0]


def create_twitter_campaign(**kwargs):
    d = kwargs.copy()
    set_if_not_present(d, 'name', 'campaign_1')
    set_if_not_present(d, 'description', 'test')
    set_if_not_present(d, 'dsl_program_upload', '')
    set_if_not_present(d, 'image_upload', '')
    set_if_not_present(d, 'twitter_account', create_twitter_account())
    return TwitterCampaign.objects.get_or_create(**d)[0]


def generate_random_string():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))