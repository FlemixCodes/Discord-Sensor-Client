from ._base import BaseCategory


class ServersCategory(BaseCategory):
    async def _get_servers(self, sort_by: str):
        params = {"sort_by": sort_by}
        return await self.request_client.method(
            f"servers/get-guilds-info", params=params
        )

    async def _get_server(self, server_id: int, endpoint: str):
        return await self.request_client.method(f"servers/{endpoint}/{server_id}")

    async def _get_server_history(
        self,
        server_id: int,
        history_type: str,
        page: int,
        limit: int,
    ):
        params = {"type": history_type, "page": page, "limit": limit}
        return await self.request_client.method(
            f"get-latest-events/{server_id}", params
        )

    async def get_servers_by_rating(self):
        return await self._get_servers("rating")

    async def get_servers_by_members_count(self):
        return await self._get_servers("membersCount")

    async def get_servers_by_voice_online(self):
        return await self._get_servers("voiceOnline")

    async def get_servers_by_online(self):
        return await self._get_servers("online")

    async def get_servers_by_members_join_week(self):
        return await self._get_servers("membersDeltaPct")

    async def get_server_info(self, server_id: int):
        return await self._get_server(server_id, "get-detail-guild-info")

    async def get_server_channels(self, server_id: int):
        return await self._get_server(server_id, "channels")

    async def get_server_join_leave_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "join_leave", page, limit)

    async def get_server_join_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "join", page, limit)

    async def get_server_leave_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "leave", page, limit)

    async def get_server_boost_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "boost", page, limit)

    async def get_server_rename_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "rename", page, limit)

    async def get_server_tag_history(
        self,
        server_id: int,
        page: int,
        limit: int,
    ):
        return await self._get_server_history(server_id, "tag_history", page, limit)
