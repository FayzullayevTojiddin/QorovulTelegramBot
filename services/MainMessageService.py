from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from locales import Locales
from models.user import User

from keyboards.inline_keyboards import (
    getMainKeyboard, getLangsKeyboard
)

class MainMessageService():

    @classmethod
    async def getResponse(cls, message: Message, state: FSMContext):
        if message.chat.type == 'private':
            return await cls.getResponseInPrivate(message, state)

    @classmethod
    async def getResponseInPrivate(cls, message: Message, state: FSMContext):
        inState = await state.get_state()
        datas = await state.get_data()
        command = message.text
        langUser = User.getLangByTelegramId(message.from_user.id)
        
        if command == '/start':
            text = Locales.getMessage(langUser, 'start_message')
            keyboard = getMainKeyboard(langUser)
            newState = inState
        elif command == "/lang":
            text = Locales.getMessage(langUser, 'edit_lang_message')
            keyboard = getLangsKeyboard()
            newState = inState

        return text, keyboard, newState