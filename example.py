import asyncio
from pprint import pprint

from discord_sensor import DiscordSensorAPIClient


async def main():
    user_id = 326648771377102850
    client = DiscordSensorAPIClient()

    resp = await client.tracker.get_user_info(user_id)
    pprint(resp)


if __name__ == "__main__":
    asyncio.run(main())
