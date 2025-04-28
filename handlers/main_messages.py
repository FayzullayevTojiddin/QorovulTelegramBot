from aiogram import Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from services.MainMessageService import MainMessageService

router = Router(name=__name__)

@router.message()
async def getstart(message: types.Message, state: FSMContext):
    try:
        text, keyboard, newState = await MainMessageService.getResponse(message=message, state=state)
        await state.set_state(newState)
        await message.answer(
            text=text,
            reply_markup=keyboard
        )
    except Exception as error:
        print(error)
        await message.answer(
            text="Xatolik !"
        )