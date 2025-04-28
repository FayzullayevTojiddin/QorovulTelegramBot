from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from models.user import User

from helpers.getTypeChats import isPrivate
from helpers.setLang import setLangUser

from keyboards.inline_keyboards import (
    getLangsKeyboard, getMainKeyboard, getActionsKeyboard, goToMainKeyboard
)

from locales import Locales

class MainCallbackService():
    
    @classmethod
    async def getResponse(cls, callback: CallbackQuery, state: FSMContext):
        if isPrivate(callback.message):
            return await cls.getResponseInPrivate(callback, state)

    async def getResponseInPrivate(callback: CallbackQuery, state: FSMContext):
        callbackData = callback.data
        inState = await state.get_state()
        data = await state.get_data()
        langUser = User.getLangByTelegramId(callback.from_user.id)
        bot = await callback.bot.get_me()

        if callbackData.startswith('lang:'):
            newLang = callbackData.split(":")[1]
            text = Locales.getMessage(newLang, 'changed_language_message')
            keyboard = getLangsKeyboard(newLang)
            newState = inState
            setLangUser(callback.from_user.id, newLang)
            await callback.answer(text=text, show_alert=True)
        
        elif callbackData == 'langs':
            text = Locales.getMessage(langUser, 'edit_lang_message')
            keyboard = getLangsKeyboard(langUser)
            newState = inState

        elif callbackData == 'main':
            text = Locales.getMessage(langUser, 'start_message')
            keyboard = getMainKeyboard(langUser)
            newState = inState

        elif callbackData == 'start':
            text = Locales.getMessage(langUser, 'start_action_message')
            keyboard = getActionsKeyboard(bot.username, langUser)
            newState = inState

        elif callbackData == 'documentation':
            funcText = Locales.getMessage(langUser, 'documentation_message')
            link = Locales.getMessage(langUser, 'url_documentation')
            text = funcText(link)
            keyboard = goToMainKeyboard(langUser)
            newState = inState

        return text, keyboard, newState