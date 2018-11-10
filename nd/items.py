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
    url = scrapy.Field()
    name = scrapy.Field()
    sector = scrapy.Field()
    industry = scrapy.Field()
    country = scrapy.Field()
    board = scrapy.Field()
    prof_margin = scrapy.Field()
    ppe = scrapy.Field()
    marketCap = scrapy.Field()
    descShort = scrapy.Field()
    url_marketwatch = scrapy.Field()
    url_reuter = scrapy.Field()
    NIGR_result = scrapy.Field()
    url = scrapy.Field()

    EPS = scrapy.Field()
    insideOwn = scrapy.Field()
    forwardPPE = scrapy.Field()
    nextYEPS = scrapy.Field()
    insideOwnTrans = scrapy.Field()
    instOwn = scrapy.Field()
    thisYGEPS = scrapy.Field()
    instOwnTrans = scrapy.Field()
    nextYGEPS = scrapy.Field()
    ROA = scrapy.Field()
    ROE = scrapy.Field()
    dividAnn = scrapy.Field()
    ROI = scrapy.Field()
    dividYieldAnn = scrapy.Field()
    dividPayoutRatio = scrapy.Field()
    avgVolumn3Month = scrapy.Field()
    priceNow = scrapy.Field()
    recomm = scrapy.Field()
    SMA20 = scrapy.Field()
    SMA50 = scrapy.Field()
    SMA200 = scrapy.Field()
    relVolumn = scrapy.Field()

    PEG = scrapy.Field()
    PSR = scrapy.Field()
    fiftytwoWeekRange = scrapy.Field()

    PBR = scrapy.Field()
    PFCF = scrapy.Field()
    DEBTtoEquity = scrapy.Field()
    Beta = scrapy.Field()
    Volatility = scrapy.Field()

    pass

