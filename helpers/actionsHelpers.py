
from locales import Locales

def getActionsList(usernameBot, langUser):
    return [
        {
            "url": f'https://t.me/{usernameBot}?startgroup=true',
            "text": Locales.getMessage(langUser, 'add_to_group_action_button')
        },
        {
            "url": f'https://t.me/{usernameBot}?startgroup=true&start=clean_badwords',
            "text": Locales.getMessage(langUser, 'clean_badwords_action_button')
        },
        {
            "url": f'https://t.me/{usernameBot}?startgroup=true&start=clean_ads',
            "text": Locales.getMessage(langUser, 'clean_ads_action_button')
        },
    ]