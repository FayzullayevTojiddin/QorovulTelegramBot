
def isCommand(text: str) -> bool:
    return text.strip().startswith('/')

def isCommandForMe(text: str, usernameBot: str) -> bool:
    if '@' in text:
        command_bot = text.split('@')[1].strip()
        return command_bot.lower() == usernameBot.lower()
    return False

def getText(message):
    return message.text or message.caption