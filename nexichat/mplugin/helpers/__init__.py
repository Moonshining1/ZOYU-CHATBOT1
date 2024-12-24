from typing import Callable
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from nexichat import OWNER, nexichat

# Decorator to check if the user is an admin
def is_admins(func: Callable) -> Callable:
    async def non_admin(c: nexichat, m: Message):
        try:
            if m.from_user.id == OWNER:
                return await func(c, m)
            admin = await c.get_chat_member(m.chat.id, m.from_user.id)
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return await func(c, m)
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error in is_admins decorator: {e}")
    return non_admin

# Importing necessary modules
from .inline import *
from .read import *
from .language import *
from .cowner import *
