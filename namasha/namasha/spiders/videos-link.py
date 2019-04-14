# -*- coding: utf-8 -*-
import scrapy
from namasha.items import NamashaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class VideosSpider(CrawlSpider):
    name = 'videos-link'
    allowed_domains = ['www.namasha.com']

    start_urls = ['https://www.namasha.com/']

    rules = (Rule(LinkExtractor('https://www.namasha.com/v/'), callback='parse_item', follow=True),)

    def parse_item(self, response):

        item = NamashaItem()
        item['title'] = response.xpath('// *[ @ id = "content"] / div[1] / div[1] / div[2] / div / h1/text()').get()
        item['category'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[6]/div/a/text()').get()
        item['link'] = response.url
        item['publisher'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[5]/div[1]/a/text()').get()
        item['publisher_logo'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[5]/img/@src').get()
        tmp = str(response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[5]/div[1]/text()').extract())
        item['date_added'] = str(''.join(tmp.split())).strip()
        item['description'] = str(response.xpath('//*[@id="video-desc"]').get())
        item['view_count'] = str(response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/span/text()').get()).strip()
        print(item)
        return item

