from ._base import BaseCategory


class TrackerCategory(BaseCategory):
    async def _get(self, user_id: int, endpoint: str, params: dict | None = None):
        return await self.request_client.method(f"tracker/{endpoint}/{user_id}", params)

    async def get_user_info(self, user_id: int):
        return await self._get(user_id, f"/get-user-info")

    async def get_servers(self, user_id: int):
        return await self._get(user_id, f"/get-user-info")

    async def get_nicknames(self, user_id: int, page: int):
        return await self._get(user_id, f"/get-user-info", {"page": page})

    async def get_friends(self, user_id: int, page: int):
        return await self._get(user_id, f"/get-friends", {"page": page})
