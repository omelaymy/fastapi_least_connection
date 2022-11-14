import asyncio
import aioredis
import httpx
from fastapi import Fastapi, BackgroundTasks
from typing import Union
from settings import SERVERS, AIOREDIS_URL
from redis_client import redis_client
import uvicorn

app = Fastapi()



# def servers_mapping():
#     redis = aioredis.from_url(AIOREDIS_URL, decode_responses=True)
#     servers_mapping = await redis.hgetall('servers')
#     print(servers_mapping)
#     return min_status_founder(servers_mapping)
#
#
# def min_status_founder(servers_mapping):
#     min_status_server = min(servers_mapping, key=servers_mapping.get)
#     print(min_status_server)

@app.get("/{path:path}")
async def balancer(background_check_server: BackgroundTasks, path: Union[str, None] = None):
    redis = aioredis.from_url(AIOREDIS_URL, decode_responses=True)
    servers = await redis.hgetall("servers")
    min_status_found = min(servers, key=servers.get)
    #host_name = check_status_server(host_name, servers, background_check_server)
    print(min_status_found, servers)
    async with httpx.AsyncClient() as client:
        await redis.hincrby("servers", min_status_found, amount=1)
        response = await client.get(f'http://{min_status_found}/{path}')
        background_check_server.add_task(health_check_background, min_status_found, redis)
    return servers


# def check_status_server(host_name, servers, background_check_server):
#     """
#     Проверка работоспособности сервера, если жив > вернуть адресс,
#     если нет, отправить его в фоновую задачу и взять следующий адрес из очереди
#     """
#     try:
#         httpx.get(f'http://{host_name}/health/')
#         return host_name
#     except httpx.ConnectError:
#         background_check_server.add_task(health_check_background, host_name)
#         try:
#             host_name = min(servers, key=servers.get)
#             return check_status_server(host_name, servers, background_check_server)
#         except IndexError:
#             return 'Все сломалось, расходимся'


# def health_check_background(host_name):
#     """
#     Фоновая проверка мертвого сервера, каждые 5 секунд отправляет запрос,
#     когда сервер ответит, он добавится в очередь
#     """
#     while True:
#         time.sleep(5)
#         try:
#             httpx.get(f'http://{host_name}/health/')
#             #servers.append(host_name)
#             break
#         except httpx.ConnectError:
#             continue

def health_check_background(host_name, redis):
    redis.hincrby("servers", host_name, amount=-1)

if __name__ == "__main__":
    asyncio.run(redis_client())
