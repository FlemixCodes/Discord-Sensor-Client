from ._base import BaseCategory


class PhotosCategory(BaseCategory):
    async def get_photo(self, user_id: int, page: int, photo_type: str):
        params = {"type": photo_type, "page": page, "sort_by": user_id}
        return await self.request_client.method(f"photos/list", params)

    async def get_avatars(self, user_id: int, page: int):
        return await self.get_photo(user_id, page, "avatars")

    async def get_selfie(self, user_id: int, page: int):
        return await self.get_photo(user_id, page, "selfie")

    async def get_streams(self, user_id: int, page: int):
        return await self.get_photo(user_id, page, "streams")

    async def get_deleted(self, user_id: int, page: int):
        return await self.get_photo(user_id, page, "deleted")
