from nexichat import mongodb
from typing import List

sudoersdb = mongodb.sudoers

async def get_sudoers() -> List[int]:
    try:
        sudoers = await sudoersdb.find_one({"sudo": "sudo"})
        return sudoers["sudoers"] if sudoers else []
    except Exception as e:
        print(f"Error in get_sudoers: {e}")
        return []

async def add_sudo(user_id: int) -> bool:
    try:
        sudoers = await get_sudoers()
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
            )
        return True
    except Exception as e:
        print(f"Error in add_sudo: {e}")
        return False

async def remove_sudo(user_id: int) -> bool:
    try:
        sudoers = await get_sudoers()
        if user_id in sudoers:
            sudoers.remove(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
            )
        return True
    except Exception as e:
        print(f"Error in remove_sudo: {e}")
        return False
