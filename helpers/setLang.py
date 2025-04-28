
from models.user import User

def setLangUser(TelegramId, newLang):
    if User.setLangByTelegramId(TelegramId, newLang):
        return False
    
    return True