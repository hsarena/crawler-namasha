# -*- coding: utf-8 -*-
import scrapy


class VideosSpider(scrapy.Spider):
    name = 'videos'
    allowed_domains = ['www.namasha.com']
    start_urls = ['http://www.namasha.com/']

    def parse(self, response):
        pass
