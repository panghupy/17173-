# -*- coding: utf-8 -*-
import scrapy
import json
from game.items import PhoneGameItem

# 手游
class GameSpiderSpider(scrapy.Spider):
    name = 'game_spider'
    allowed_domains = ['17173.com']
    start_urls = ['http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page=1']
    page = 1

    def parse(self, response):
        print(response.url)
        print('*' * 100)
        self.page += 1
        next_url = 'http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page=' + str(self.page)
        result = json.loads(response.text)
        for game_info in result['data']['dataSet']:
            # print(game_info)
            # 游戏名字
            print(game_info['info_chname'])
            # 开测时间
            print(game_info['test_stime'])
            # 测试名称
            print(game_info['test_name'])
            # 游戏类型
            print(game_info['game_type_name'])
            # 游戏平台
            print(game_info['info_platform'])
            # 状态
            print(game_info['test_status_name'])
            # 游戏详情链接
            game_url = game_info['game_url']
            yield scrapy.Request(game_url, callback=self.parse_detail)
        yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        print('手游详情')
        # 图片链接
        img_url = response.xpath(
            '//div[@class="pn-bd"]//div[@class="mod-mater-avatar mod-mater-avatar-ex "]/img/@src').extract_first()
        # 游戏名称
        title = response.xpath('//h1/text()').extract_first()
        # 评星
        star = response.xpath('//div[@class="mod-mater-info"]/div/text()').extract_first().strip('')
        # 风格
        style = ''
        for item in response.xpath('//div[@class="box-mater-cate"]//a'):
            style += item.xpath('./text()').extract_first() + ','
        # 游戏类型
        game_type = response.xpath('//ul[@class="list-mater-info"]//li[1]//a/text()').extract_first()
        # 游戏语言
        game_language = response.xpath('//ul[@class="list-mater-info"]//li[2]//a/text()').extract_first()
        # 是否收费
        is_free = response.xpath('//ul[@class="list-mater-info"]//li[3]//span[2]/text()').extract_first().strip()
        # 支持平台
        item_plat = response.xpath('//ul[@class="list-mater-info"]//li[4]//a/text()').extract_first()
        # 开发商
        kaifashang = response.xpath('//ul[@class="list-mater-info"]//li[5]//span[2]/text()').extract_first()
        # 注册王者
        register_url = response.xpath('//ul[@class="list-mater-info"]//li[6]//span[2]/text()').extract_first()
        # 运营商
        item_operator = response.xpath('//ul[@class="list-mater-info"]//li[7]//span[2]/text()').extract_first()
        # 简介
        content = response.xpath('//div[@class="mod-mater-intro"]/p/text()').extract_first()
        item = PhoneGameItem()
        item['img_url'] = img_url
        item['title'] = title
        item['star'] = star
        item['style'] = style
        item['game_type'] = game_type
        item['game_language'] = game_language
        item['is_free'] = is_free
        item['item_plat'] = item_plat
        item['kaifashang'] = kaifashang
        item['register_url'] = register_url
        item['item_operator'] = item_operator
        yield item

