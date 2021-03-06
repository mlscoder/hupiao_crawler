# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
租房信息相关字段
"""


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 创建时间
    createDate = scrapy.Field()
    # 内容
    text = scrapy.Field()
    # 爬取时间
    crawDate = scrapy.Field()
    # 页面的url
    url = scrapy.Field()
    # 信息创建者
    creator = scrapy.Field()
    # 图片
    image_urls = scrapy.Field()
