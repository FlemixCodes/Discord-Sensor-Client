from ._base import BaseCategory


class AttachmentsCategory(BaseCategory):
    async def _get_attachment(self, photo_id: int, attachment_type: str):
        attachment_types = {
            "avatar": "e20",
            "deleted": "e21",
            "selfie": "e22",
            "screenshot": "e23",
        }

        type_ = attachment_types[attachment_type]
        return await self.request_client.method(
            f"attachments/{type_}/{photo_id}", content=True
        )

    async def get_avatar(self, photo_id: int):
        return await self._get_attachment(photo_id, "avatar")

    async def get_deleted(self, photo_id: int):
        return await self._get_attachment(photo_id, "deleted")

    async def get_selfie(self, photo_id: int):
        return await self._get_attachment(photo_id, "selfie")

    async def get_screenshot(self, photo_id: int):
        return await self._get_attachment(photo_id, "screenshot")
