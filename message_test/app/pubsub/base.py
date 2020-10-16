# coding:utf-8

import redis


class RedisSubPub(object):
    def __init__(self,
                 host='localhost',
                 port=6379,
                 db=13,
                 password='',
                 pub='dewei',
                 sub='dewei'
                 ):
        pool = redis.ConnectionPool(host=host,
                                    port=port,
                                    db=db,
                                    password=password)
        self.__conn = redis.StrictRedis(connection_pool=pool)
        self.sub = sub
        self.pub = pub
        self.__sub = None

    def public(self, msg):

        if self.pub:
            self.__conn.publish(self.pub, msg)  # 开始发布消息了
            return True
        else:
            return False

    def subscribe(self):

        if self.sub:
            self._sub = self.__conn.pubsub()  # 开始订阅
            self._sub.subscribe(self.sub)  # 订阅频道
            self._sub.parse_response()  # 准备接受

            return self._sub

