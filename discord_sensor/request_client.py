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
        self,
        url: str,
        params: dict | None = None,
        method: str = "GET",
        content: bool = False,
    ) -> dict | bytes:
        response = await self.session.request(
            url=url,
            params=params,
            proxies=self.proxies,
            method=method,
        )

        try:
            if response.status_code != 200 and response.status_code != 404:
                raise DiscordSensorHTTPException("Response status code is not 200")

            if response.status_code == 404:
                data = response.json()
                raise DiscordSensorAPIException(data["error"])

            if content:
                data = response.content
            else:
                data = response.json()

            return data
        except Exception as e:
            raise DiscordSensorHTTPException(f"Invalid Response: {e}")

    async def method(
        self,
        method: str,
        params: dict | None = None,
        content: bool = False,
    ) -> dict | bytes:
        url = f"{self.base_url}/{method}"
        return await self.request(url=url, params=params, content=content)

    async def close(self):
        await self.session.close()
