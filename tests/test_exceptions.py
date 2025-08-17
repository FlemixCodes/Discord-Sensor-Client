import unittest
from unittest import IsolatedAsyncioTestCase

from discord_sensor.exceptions import (
    DiscordSensorAPIException,
    DiscordSensorHTTPException,
)

from discord_sensor.api_client import DiscordSensorClient


class TextExceptions(IsolatedAsyncioTestCase):
    async def test_api_exception(self):
        with self.assertRaises(DiscordSensorAPIException):
            client = DiscordSensorClient()
            await client.tracker.get_user_info(1212121212)

    async def test_http_exception(self):
        with self.assertRaises(DiscordSensorHTTPException):
            client = DiscordSensorClient()
            await client.request_client.request("https://youtube.com")


if __name__ == "__main__":
    unittest.main()
