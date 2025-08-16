from ._base import BaseCategory


class AttachmentsCategory(BaseCategory):
    async def get_avatar(self, photo_id: int):
        return await self.request_client.method(f"attachments/e20/{photo_id}")

    async def get_deleted(self, photo_id: int):
        return await self.request_client.method(f"attachments/e21/{photo_id}")

    async def get_selfie(self, photo_id: int):
        return await self.request_client.method(f"attachments/e22/{photo_id}")

    async def get_screenshot(self, photo_id: int):
        return await self.request_client.method(f"attachments/e23/{photo_id}")
