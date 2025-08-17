import asyncio
from pprint import pprint

from discord_sensor import DiscordSensorClient


async def main():
    # Инициаилизируем объект клиента
    client = DiscordSensorClient()

    # Получаем все сервера по рейтингу
    servers = await client.servers.get_servers_by_rating()

    # Получаем айди первого сервера
    server_id = servers["guilds"][0]["id"]

    # Получаем информацию о сервере
    server_info = await client.servers.get_server_info(server_id)
    pprint(server_info)

    # Получаем роли сервера
    server_roles = await client.functions.get_server_roles(server_id)

    # Берем первую роль
    role_id = server_roles["roles"][0]["role_id"]

    # Получаем всех участников с этой ролью
    role_members = await client.functions.get_role_members(server_id, role_id, 1, 1)
    pprint(role_members)


if __name__ == "__main__":
    asyncio.run(main())
