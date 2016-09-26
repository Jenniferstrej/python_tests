import redis


class Session(object):

    def __new__(self, settings):
        return RedisSession(settings)


class RedisSession(object):

    def __init__(self, settings):
        self.expire_key = settings.redis_expire_key
        self.r = redis.StrictRedis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db)

    def store_value(self, execution_id, key, value):
        self.r.hset(execution_id, key, value)
        self.r.expire(execution_id, self.expire_key)

    def get_value(self, execution_id, key):
        return self.r.hget(execution_id,key)