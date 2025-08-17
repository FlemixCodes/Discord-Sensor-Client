import unittest
from unittest import IsolatedAsyncioTestCase

from discord_sensor.api_client import DiscordSensorClient


class TestMethods(IsolatedAsyncioTestCase):
    async def test_tracker(self):
        client = DiscordSensorClient()
        await client.tracker.get_user_info(326648771377102850)


if __name__ == "__main__":
    unittest.main()
