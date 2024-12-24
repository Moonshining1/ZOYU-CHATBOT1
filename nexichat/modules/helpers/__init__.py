from typing import Callable
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from nexichat import OWNER, nexichat

def is_admins(func: Callable) -> Callable:
    async def non_admin(c: nexichat, m: Message):
        try:
            if m.from_user.id == OWNER:
                return await func(c, m)

            admin = await c.get_chat_member(m.chat.id, m.from_user.id)
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return await func(c, m)
        except Exception as e:
            # Log the exception or handle it as necessary
            print(f"Error in is_admins decorator: {e}")
            return

    return non_admin

from .inline import *
from .read import *
from .language import *
