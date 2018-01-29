from app import redis


class RedisModel(object):

    new_visitor = "New:Visitor:"

    new_follow = "New:Follow:Add:"

    @staticmethod
    def add_new_message(user_id, message):
        """
        添加新的消息
        :param user_id: 用户id
        :param message: 消息类型
        """
        cache_key = message + str(user_id)
        redis.inc(cache_key)

    @staticmethod
    def query_new_message(user_id, message):
        cache_key = message + str(user_id)
        return redis.get(cache_key)