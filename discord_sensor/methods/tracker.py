from ._base import BaseCategory


class TrackerCategory(BaseCategory):
    async def get_user_info(self, user_id: int):
        return await self.request_client.method(f"tracker/get-user-info/{user_id}")

    async def get_servers(self, user_id: int):
        return await self.request_client.method(f"tracker/get-mutual-guilds/{user_id}")

    async def get_nicknames(self, user_id: int, page: int):
        return await self.request_client.method(
            f"tracker/get-nicknames/{user_id}", {"page": page}
        )

    async def get_friends(self, user_id: int, page: int):
        return await self.request_client.method(
            f"tracker/get-friends/{user_id}", {"page": page}
        )
