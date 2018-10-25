# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#https://finviz.com/quote.ashx?t=aapl
#https://www.ipoboutique.com/ipo-calendar.html
import scrapy


class NdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()
    ipo_year = scrapy.Field()
    name = scrapy.Field()
    sector = scrapy.Field()
    industry = scrapy.Field()
    country = scrapy.Field()
    board = scrapy.Field()
    prof_margin = scrapy.Field()
    ppe = scrapy.Field()
    vol = scrapy.Field()
    descShort = scrapy.Field()
    url_marketwatch = scrapy.Field()
    url_reuter = scrapy.Field()
    pass
