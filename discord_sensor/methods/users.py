from ._base import BaseCategory


class UsersCategory(BaseCategory):
    async def get_events(self, user_id: int, limit: int, page: int, events_type: str):
        params = {"subTab": events_type, "limit": limit, "page": page}
        return await self.request_client.method(
            f"api/users/get-latest-events/{user_id}", params
        )

    async def get_server_history(self, user_id: int, limit: int, page: int):
        return await self.get_events(user_id, limit, page, "server_history")

    async def get_boost_history(self, user_id: int, limit: int, page: int):
        return await self.get_events(user_id, limit, page, "boost_history")

    async def get_about_me_history(self, user_id: int, limit: int, page: int):
        return await self.get_events(user_id, limit, page, "about_me_history")

    async def get_voice_history(self, user_id: int, limit: int, page: int):
        return await self.get_events(user_id, limit, page, "voice_history")
