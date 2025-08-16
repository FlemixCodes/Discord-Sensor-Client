from ._base import BaseCategory


class UsersCategory(BaseCategory):
    async def get_server_history(self, user_id: int, limit: int, page: int):
        return await self.request_client.method(
            f"api/users/get-latest-events/{user_id}",
            {"subTab": "server_history", "limit": limit, "page": page},
        )

    async def get_boost_history(self, user_id: int, limit: int, page: int):
        return await self.request_client.method(
            f"api/users/get-latest-events/{user_id}",
            {"subTab": "boost_history", "limit": limit, "page": page},
        )

    async def get_about_me_history(self, user_id: int, limit: int, page: int):
        return await self.request_client.method(
            f"api/users/get-latest-events/{user_id}",
            {"subTab": "about_me_history", "limit": limit, "page": page},
        )

    async def get_voice_history(self, user_id: int, limit: int, page: int):
        return await self.request_client.method(
            f"api/users/get-latest-events/{user_id}",
            {"subTab": "voice_history", "limit": limit, "page": page},
        )
