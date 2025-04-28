from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from locales import Locales
from models.user import User

from helpers.getTypeChats import (
    isPrivate, isPublic
)
from helpers.filterMessage import (
    isCommand, isCommandForMe, getText
)

from keyboards.inline_keyboards import (
    getMainKeyboard, getLangsKeyboard, getActionsKeyboard
)

class MainMessageService():

    @classmethod
    async def getResponse(cls, message: Message, state: FSMContext):
        if isPrivate(message):
            return await cls.getResponseInPrivate(message, state)
        elif isPublic(message):
            return await cls.getResponseInPublic(message, state)

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
            keyboard = getLangsKeyboard(langUser)
            newState = inState

        return text, keyboard, newState
    
    @classmethod
    async def getResponseInPublic(cls, message: Message, state: FSMContext):
        bot = await message.bot.get_me()
        usernameBot = bot.username
        langUser = User.getLangByTelegramId(message.from_user.id)
        inState = await state.get_state()
        if isCommand(message.text) and isCommandForMe(message.text, usernameBot):
            command = message.text.split("@")[0]
            
            if command == '/start':
                text = Locales.getMessage(langUser, 'start_message')
                keyboard = getActionsKeyboard(usernameBot, langUser, isGroup=True)
                newState = inState

            else:
                text = Locales.getMessage(langUser, 'unknown_command_group_message')
                keyboard = None
                newState = inState

        else:
            messageText = getText(message)
            text = "Bu buyruq mavjud emas hali"
            keyboard = None
            newState = inState

        return text, keyboard, newState