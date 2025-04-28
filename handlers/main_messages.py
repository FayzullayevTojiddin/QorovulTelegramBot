from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from services.MainMessageService import MainMessageService
from services.MainCallbackService import MainCallbackService

router = Router(name=__name__)

@router.message()
async def getstart(message: types.Message, state: FSMContext):
    try:
        text, keyboard, newState = await MainMessageService.getResponse(message=message, state=state)
        await state.set_state(newState)
        await message.answer(
            text=text,
            reply_markup=keyboard,
            reply_to_message_id=message.message_id
        )
    except Exception as error:
        print(error)
        await message.answer(
            text="Xatolik !"
        )

@router.callback_query()
async def getCallbackResponse(callback: types.CallbackQuery, state: FSMContext):
    try:
        text, keyboard, newState = await MainCallbackService.getResponse(callback, state)
        await callback.message.bot.edit_message_text(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=keyboard,
        )
        await state.set_state(newState)
    except Exception as error:
        print(error)
        await callback.answer(error)