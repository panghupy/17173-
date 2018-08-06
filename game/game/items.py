# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 手游
class PhoneGameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url = scrapy.Field()
    title = scrapy.Field()
    # 评星
    star = scrapy.Field()
    # 风格
    style = scrapy.Field()
    # 游戏类型
    game_type = scrapy.Field()
    # 游戏语言
    game_language = scrapy.Field()
    # 是否收费
    is_free = scrapy.Field()
    # 支持平台
    item_plat = scrapy.Field()
    # 开发商
    kaifashang = scrapy.Field()
    # 注册网址
    register_url = scrapy.Field()
    # 运营商
    item_operator = scrapy.Field()
    # 简介
    content = scrapy.Field()


# 热门游戏
class HotGameItem(scrapy.Item):
    img_url = scrapy.Field()
    title = scrapy.Field()
    # 评星
    star = scrapy.Field()
    # 风格
    style = scrapy.Field()
    # 游戏类型
    game_type = scrapy.Field()
    # 游戏语言
    game_language = scrapy.Field()
    # 是否收费
    is_free = scrapy.Field()
    # 支持平台
    item_plat = scrapy.Field()
    # 开发商
    kaifashang = scrapy.Field()
    # 注册网址
    register_url = scrapy.Field()
    # 运营商
    item_operator = scrapy.Field()
    # 简介
    content = scrapy.Field()
    # 热门游戏榜名次
    ranking = scrapy.Field()
    # 票数
    votes = scrapy.Field()
    # 福利通知我人数
    fuli = scrapy.Field()