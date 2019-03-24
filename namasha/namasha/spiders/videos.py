# -*- coding: utf-8 -*-
import scrapy
from namasha.items import NamashaItem


class VideosSpider(scrapy.Spider):
    name = 'videos'
    allowed_domains = ['www.namasha.com']

    categories = ['funny', 'sport', 'technology',
                  'animation', 'educational', 'vehicle',
                  'news', 'music', 'game',
                  'animals', 'accidents', 'religious']

    start_urls = ['https://www.namasha.com/playlist/{0}'.format(category) for category in categories]
    custom_settings = {
        'DEPTH_LIMIT': '1',
    }

    def parse(self, response):
        items = []
        category = response.xpath('//*[@id="content"]/div[1]/h1/text()').get()
        videos = response.xpath('//*[@id="content"]/div[2]/div/div')
        for video in videos:
            item = NamashaItem()
            item['category'] = category
            item['title'] = video.xpath('div/a/text()').get()
            item['link'] = video.xpath('div/a/@href').get()
            items.append(item)
        print(items)
        return items
