# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from game.items import PhoneGameItem, HotGameItem


class GamePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, PhoneGameItem):
            client = pymongo.MongoClient('127.0.0.1:27017')
            db = client['Game']
            phoneGameInfo = db['PhoneGameInfo']
            doc = {
                'img_url': item['img_url'],
                'title': item['title'],
                'star': item['star'],
                'style': item['style'],
                'game_type': item['game_type'],
                'game_language': item['item_plat'],
                'kaifashang': item['item_plat'],
                'is_free': item['is_free'],
                'item_plat': item['item_plat'],
                'register_url': item['register_url'],
                'item_operator': item['item_operator'],
                'content': item['content'],
            }
            phoneGameInfo.insert(doc)
        if isinstance(item, HotGameItem):
            client = pymongo.MongoClient('127.0.0.1:27017')
            db = client['Game']
            hotGameInfo = db['HotGameInfo']
            doc = {
                'img_url': item['img_url'],
                'title': item['title'],
                'star': item['star'],
                'style': item['style'],
                'game_type': item['game_type'],
                'game_language': item['item_plat'],
                'kaifashang': item['item_plat'],
                'is_free': item['is_free'],
                'item_plat': item['item_plat'],
                'register_url': item['register_url'],
                'item_operator': item['item_operator'],
                'content': item['content'],
                'ranking': item['ranking'],
                'votes': item['votes'],
                'fuli': item['fuli']
            }
            hotGameInfo.insert(doc)

        return item
