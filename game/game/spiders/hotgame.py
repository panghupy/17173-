# -*- coding: utf-8 -*-
import scrapy
from game.items import HotGameItem
import re
import requests
import json


# 一周热榜
class HotgameSpider(scrapy.Spider):
    name = 'hotgame'
    allowed_domains = ['17173.com']
    start_urls = ['http://top.17173.com/list-2-0-0-0-0-0-0-0-0-0-1.html']
    page = 1

    def parse(self, response):
        if self.page <= 36:
            self.page += 1
            next_url = 'http://top.17173.com/list-2-0-0-0-0-0-0-0-0-0-' + str(self.page) + '.html'
            game_list = response.xpath('//ul[@class="list-plate js-rank"]//li')
            for game_info in game_list:
                game_title = game_info.xpath('.//div[@class="con"]/a/text()').extract_first()
                detail_url = game_info.xpath('.//div[@class="con"]/a/@href').extract_first()
                test_status = game_info.xpath('.//div[@class="c5"]/text()').extract_first().strip()
                game_id = re.findall('\d+', detail_url)[1]
                yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'game_id': game_id})
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        game_id = response.meta['game_id']
        print('游戏热榜详情')
        # 图片链接
        img_url = response.xpath('//span[@class="avatar-t"]//span/img/@href').extract_first()
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
        item_plat = response.xpath('//ul[@class="list-mater-info"]//li[4]//a/@title').extract_first()
        # 开发商
        kaifashang = response.xpath('//ul[@class="list-mater-info"]//li[5]//a/text()').extract_first()
        # 注册网址
        register_url = response.xpath('//ul[@class="list-mater-info"]//li[6]//span[2]/text()').extract_first()
        # 运营商
        item_operator = response.xpath('//ul[@class="list-mater-info"]//li[7]//span[2]//a/@title').extract_first()
        # 简介
        content = response.xpath('//div[@class="mod-mater-intro"]/p/text()').extract_first().strip()
        print('-' * 200)
        item = HotGameItem()
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
        item['content'] = content

        # 福利通知我的接口
        fuli_url = 'http://hao.17173.com/api/getGameScheCount?game_codes=' + str(
            game_id) + ' & callback=jsonp & callback=jQuery111105772122356899088_1532679883818 & _=1532679883819'
        response = requests.get(fuli_url).text
        response = re.search('{.*?}.*?}', response).group()
        result_dict = json.loads(response)
        fuli = result_dict['data'][game_id + ' ']
        item['fuli'] = fuli
        # 投票数和排名
        rank_url = 'http://top.17173.com/api/gamerankinfo?gameCode=' + str(game_id) + '.js&_=1532680359400'
        response = requests.get(rank_url).text
        result = re.findall('{.*?}', response)[2]
        result_dict = json.loads(result)
        ranking = result_dict['rank_num']
        votes = result_dict['heats_num']
        item['votes'] = votes
        item['ranking'] = ranking
        yield item