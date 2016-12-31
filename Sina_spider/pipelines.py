# encoding=utf-8
import pymongo
from items import InformationItem, TweetsItem, FollowsItem, FansItem


class MongoDBPipleline(object):
    def __init__(self):
        self.init(pymongo.MongoClient("localhost", 27017)["weibos"])
        

    def init(self, db):
        self.tables = {
            "information" : db["Information"],
            "tweets" : db["Tweets"],
            "follows" : db["Follows"],
            "fans" : db["Fans"]        
        }

    # 插入多条
    def inserts(self, item, table):
        items = dict(item)
        rows = items.pop(table)
        for i in range(len(rows)):
            items[str(i + 1)] = rows[i]
        try:
            self.Follows.insert(items)
        except Exception:
            pass
 
    # 插入一条
    def insert(self, item, table):
        try:
            self.tables[table].insert(dict(item))
        except Exception:
            pass

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, InformationItem):
            self.insert(item, 'information')
        elif isinstance(item, TweetsItem):
            self.insert(item, 'tweets')
        elif isinstance(item, FollowsItem):
            self.inserts(item, "follows")
        elif isinstance(item, FansItem):
            self.inserts(item, "fans")
        return item
