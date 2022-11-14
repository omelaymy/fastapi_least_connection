import aioredis
from settings import AIOREDIS_URL


async def redis_client():
    redis = aioredis.from_url(AIOREDIS_URL, decode_responses=True)
    await redis.hset("servers", mapping={
                                      'http://0.0.0.0:8000': 0,
                                      'http://0.0.0.0:8001': 2,
                                      'http://0.0.0.0:8002': 3,
                                      'http://0.0.0.0:8003': 4,
                                      'http://0.0.0.0:8004': 5
                                      })








