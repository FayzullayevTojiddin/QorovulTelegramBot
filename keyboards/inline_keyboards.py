from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales import Locales

from helpers.actionsHelpers import getActionsList

def getMainKeyboard(lang):
    keyboard = InlineKeyboardBuilder()
    buttons = {
        'start' : Locales.getMessage(lang, 'start_button'),
        'documentation' : Locales.getMessage(lang, 'documentation_button'),
        'langs' : Locales.getMessage(lang, 'edit_lang_button')
    }
    for callback, text in buttons.items():
        keyboard.button(
            text=text, callback_data=callback
        )
    keyboard.adjust(2)
    return keyboard.as_markup()

def getLangsKeyboard(lang):
    keyboard = InlineKeyboardBuilder()
    langs = Locales.getLangs()
    for callback, name in langs.items():
        keyboard.button(
            text=name, callback_data=f"lang:{callback}"
        )
    keyboard.button(
        text=Locales.getMessage(lang, 'main_menu_button'),
        callback_data='main'
    )
    keyboard.adjust(2)
    return keyboard.as_markup()

def getActionsKeyboard(usernameBot, langUser, isGroup=False):
    keyboard = InlineKeyboardBuilder()
    buttons = getActionsList(usernameBot, langUser)
    for button in buttons:
        keyboard.button(text=button["text"], url=button["url"])
    
    if not isGroup:
        keyboard.button(
            text=Locales.getMessage(langUser, 'main_menu_button'),
            callback_data='main'
        )
        
    keyboard.adjust(1)
    return keyboard.as_markup()

def goToMainKeyboard(lang):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text=Locales.getMessage(lang, 'main_menu_button'),
        callback_data='main'
    )
    return keyboard.as_markup()