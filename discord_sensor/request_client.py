import niquests

from .exceptions import DiscordSensorHTTPException, DiscordSensorAPIException


class RequestClient:
    base_url = "https://discord-sensor.com/api"

    def __init__(
        self,
        session: niquests.AsyncSession | None = None,
        proxies: dict | None = None,
    ):
        self.proxies = proxies
        self.session = session if session else niquests.AsyncSession()

    async def request(
        self, url: str, params: dict | None = None, method: str = "GET"
    ) -> dict:
        response = await self.session.request(
            url=url,
            params=params,
            proxies=self.proxies,
            method=method,
        )

        try:
            data = response.json()
        except:
            raise DiscordSensorHTTPException("Response is invalid")

        if data.get("error"):
            raise DiscordSensorAPIException(data["error"])

        if response.status_code != 200:
            raise DiscordSensorHTTPException("Response status code is not 200")

        return data

    async def method(self, method: str, params: dict | None = None) -> dict:
        url = f"{self.base_url}/{method}"
        return await self.request(url=url, params=params)

    async def close(self):
        await self.session.close()
        self.session.adapters
