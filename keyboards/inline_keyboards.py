from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales import Locales

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

def getLangsKeyboard():
    keyboard = InlineKeyboardBuilder()
    langs = Locales.getLangs()
    for callback, name in langs.items():
        keyboard.button(
            text=name, callback_data=f"lang:{callback}"
        )
    keyboard.adjust(2)
    return keyboard.as_markup()