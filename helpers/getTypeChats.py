def isPrivate(message):
    return message.chat.type == 'private'

def isPublic(message):
    return message.chat.type == 'channel' or message.chat.type == 'group' or message.chat.type == 'supergroup'