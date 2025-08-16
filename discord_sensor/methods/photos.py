from ._base import BaseCategory


class PhotosCategory(BaseCategory):
    async def get_avatars(self, user_id: int, page: int):
        return await self.request_client.method(
            f"photos/list", {"type": "avatars", "page": page, "sort_by": user_id}
        )

    async def get_selfie(self, user_id: int, page: int):
        return await self.request_client.method(
            f"photos/list", {"type": "selfie", "page": page, "sort_by": user_id}
        )

    async def get_streams(self, user_id: int, page: int):
        return await self.request_client.method(
            f"photos/list", {"type": "streams", "page": page, "sort_by": user_id}
        )

    async def get_deleted(self, user_id: int, page: int):
        return await self.request_client.method(
            f"photos/list", {"type": "deleted", "page": page, "sort_by": user_id}
        )
