import niquests

from .request_client import RequestClient
from .methods import (
    AttachmentsCategory,
    PhotosCategory,
    TrackerCategory,
    UsersCategory,
    FunctionsCategory,
    ServersCategory,
)


class DiscordSensorClient:
    def __init__(
        self,
        session: niquests.AsyncSession | None = None,
        proxies: dict | None = None,
    ):
        self.request_client = RequestClient(session=session, proxies=proxies)

        self.attachments = AttachmentsCategory(self.request_client)
        self.photos = PhotosCategory(self.request_client)
        self.tracker = TrackerCategory(self.request_client)
        self.users = UsersCategory(self.request_client)
        self.functions = FunctionsCategory(self.request_client)
        self.servers = ServersCategory(self.request_client)

    async def method(
        self,
        method: str,
        params: dict | None = None,
        content: bool = False,
    ) -> dict | bytes:
        return await self.request_client.method(method, params, content=content)
