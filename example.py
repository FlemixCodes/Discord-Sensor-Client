import asyncio
from pprint import pprint

from discord_sensor import DiscordSensorClient


async def main():
    client = DiscordSensorClient()

    servers = await client.servers.get_servers_by_rating()
    server_id = servers["guilds"][0]["id"]

    server_info = await client.servers.get_server_info(server_id)
    print(server_info)

    server_roles = await client.functions.get_server_roles(server_id)
    role_id = server_roles["roles"][0]["role_id"]
    role_members = await client.functions.get_role_members(server_id, role_id, 1, 1)
    print(role_members)


if __name__ == "__main__":
    asyncio.run(main())
