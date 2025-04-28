from aiogram import Router

router = Router(name=__name__)

from .main_messages import router as start_messages_router

router.include_routers(
    start_messages_router
)