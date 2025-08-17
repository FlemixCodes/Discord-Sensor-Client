from ._base import BaseCategory


class FunctionsCategory(BaseCategory):
    async def _get(
        self,
        server_id: int,
        endpoint: str,
        role_id: int | None = None,
        params: dict | None = None,
    ):
        if role_id:
            url = f"functions/{endpoint}/{server_id}/{role_id}"
        else:
            url = f"functions/{endpoint}/{server_id}"

        return await self.request_client.method(url, params)

    async def get_server_roles(self, server_id: int):
        return await self._get(server_id, "get-server-roles")

    async def get_role_channels(self, server_id: int, role_id: int):
        return await self._get(server_id, "get-role-channels", role_id=role_id)

    async def get_role_members(
        self,
        server_id: int,
        role_id: int,
        page: int,
        limit: int,
    ):
        params = {"page": page, "limit": limit}
        return await self._get(
            server_id, "get-role-members", role_id=role_id, params=params
        )
