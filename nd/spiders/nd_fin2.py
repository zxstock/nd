import scrapy
import numpy as np
import pandas as pd
import datetime
from scrapy.http import Request
from urllib import parse
from nd.items import NdItem
from nd.model import marketwatch_bs
#from scrapy.loader import ItemLoader



from nd.model.csv_symbol import return_symbols

symbol_list = return_symbols('nasdaq.csv')

# -*- coding: utf-8 -*-

class ndlistSpider(scrapy.Spider):
    name = 'nd2'
    #allowed_domains = ['www.cnbc.com/'] this will allow urls beyond the basic start url
    base_url = 'https://finviz.com/'

    start_urls = ['https://finviz.com/']
    #start_urls = ['https://www.cnbc.com/']

    def parse(self, response):
        #yield scrapy.Request(self.base_url + 'nasdaq-100/', callback=self.parse)
        #Nd100Item_result = Nd100Item()


        # Extract information inside each page
        # using css to extract

        df_nasdaq = pd.read_csv('nasdaq.csv')


        #names = response.css(".data.quoteTable tbody tr td:nth-of-type(2)").extract()  #only return empty list
        for i in np.arange(len(symbol_list)):
            symbol = symbol_list[i]
            IPO_year = df_nasdaq.loc[df_nasdaq['Symbol'] == symbol].get('IPOyear').item()
            url = 'https://finviz.com/quote.ashx?t='+symbol.lower()
            yield scrapy.Request(url,
                                 meta={'item_symbol': symbol,'ipo_year':IPO_year,'url': url},
                                 callback=self.parse_detail)

        pass



    def parse_detail(self, response):

        def checkspan(str):
            if response.css(str).extract_first() is None:
                new_str = str[:-6] + ' span' + '::text'
                return response.css(new_str)
            else:
                return response.css(str)

        NdItem_result = NdItem()
        url_reuter =  response.css("table.fullview-links .tab-link::attr(href)").extract()[0]
        url_marketwatch = response.css("table.fullview-links .tab-link::attr(href)").extract()[1]
        NIGR_result = marketwatch_bs.get_NIGR_js(response.meta['item_symbol'])

        desc = response.css(".fullview-profile::text").extract_first()
        name = response.css(".fullview-title a.tab-link b::text").extract()[0]
        sector = response.css(".fullview-title .tab-link::text").extract()[0]
        industry = response.css(".fullview-title .tab-link::text").extract()[1]
        country = response.css(".fullview-title .tab-link::text").extract()[2]
        board = response.css(".fullview-title span.body-table::text").extract()[0]
        #financial related numbers

        prof_margin= checkspan(".table-dark-row:nth-child(10) td:nth-child(8) b::text").extract_first()
        ppe = checkspan(".table-dark-row:nth-child(1) td:nth-child(4) b::text").extract_first()
        marketCap = checkspan(".table-dark-row:nth-child(2) td:nth-child(2) b::text").extract_first()

        EPS = checkspan(".table-dark-row:nth-child(1) td:nth-child(6) b::text").extract_first()
        insideOwn = checkspan(".table-dark-row:nth-child(1) td:nth-child(8) b::text").extract_first()
        forwardPPE = checkspan(".table-dark-row:nth-child(2) td:nth-child(4) b::text").extract_first()
        nextYEPS = checkspan(".table-dark-row:nth-child(2) td:nth-child(6) b::text").extract_first()
        insideOwnTrans = checkspan(".table-dark-row:nth-child(2) td:nth-child(8) b::text").extract_first()
        instOwn = checkspan(".table-dark-row:nth-child(3) td:nth-child(8) b::text").extract_first()
        thisYGEPS = checkspan(".table-dark-row:nth-child(4) td:nth-child(6) b::text").extract_first()
        instOwnTrans = checkspan(".table-dark-row:nth-child(4) td:nth-child(8) b::text").extract_first()
        nextYGEPS = checkspan(".table-dark-row:nth-child(5) td:nth-child(6) b::text").extract_first()
        ROA = checkspan(".table-dark-row:nth-child(5) td:nth-child(8) b::text").extract_first()
        ROE = checkspan(".table-dark-row:nth-child(6) td:nth-child(8) b::text").extract_first()
        dividAnn = checkspan(".table-dark-row:nth-child(7) td:nth-child(2) b::text").extract_first()
        ROI = checkspan(".table-dark-row:nth-child(7) td:nth-child(8) b::text").extract_first()
        dividYieldAnn = checkspan(".table-dark-row:nth-child(8) td:nth-child(2) b::text").extract_first()
        dividPayoutRatio = checkspan(".table-dark-row:nth-child(11) td:nth-child(8) b::text").extract_first()
        avgVolumn3Month = checkspan(".table-dark-row:nth-child(11) td:nth-child(10) b::text").extract_first()
        priceNow = checkspan(".table-dark-row:nth-child(11) td:nth-child(12) b::text").extract_first()
        recomm = checkspan(".table-dark-row:nth-child(12) td:nth-child(2) b::text").extract_first()
        SMA20 = checkspan(".table-dark-row:nth-child(12) td:nth-child(4) b::text").extract_first()
        SMA50 = checkspan(".table-dark-row:nth-child(12) td:nth-child(6) b::text").extract_first()
        SMA200 = checkspan(".table-dark-row:nth-child(12) td:nth-child(8) b::text").extract_first()

        NdItem_result["EPS"] = EPS
        NdItem_result["insideOwn"] = insideOwn
        NdItem_result["forwardPPE"] = forwardPPE
        NdItem_result["nextYEPS"] = nextYEPS
        NdItem_result["insideOwnTrans"] = insideOwnTrans
        NdItem_result["instOwn"] = instOwn
        NdItem_result["thisYGEPS"] = thisYGEPS
        NdItem_result["instOwnTrans"] = instOwnTrans
        NdItem_result["nextYGEPS"] = nextYGEPS
        NdItem_result["ROA"] = ROA
        NdItem_result["ROE"] = ROE
        NdItem_result["dividAnn"] = dividAnn
        NdItem_result["ROI"] = ROI
        NdItem_result["dividYieldAnn"] = dividYieldAnn
        NdItem_result["dividPayoutRatio"] = dividPayoutRatio
        NdItem_result["avgVolumn3Month"] = avgVolumn3Month
        NdItem_result["priceNow"] = priceNow
        NdItem_result["recomm"] = recomm
        NdItem_result["SMA20"] = SMA20
        NdItem_result["SMA50"] = SMA50
        NdItem_result["SMA200"] = SMA200



        NdItem_result["url"] = response.meta['url']
        NdItem_result["symbol"] = response.meta['item_symbol']
        NdItem_result["name"] = name
        NdItem_result["sector"] = sector
        NdItem_result["industry"] = industry
        NdItem_result["country"] = country
        NdItem_result["board"] = board
        NdItem_result["prof_margin"] = prof_margin
        NdItem_result["ppe"] = ppe
        NdItem_result["marketCap"] = marketCap
        NdItem_result["url_reuter"] = url_reuter
        NdItem_result["url_marketwatch"] = url_marketwatch
        NdItem_result["ipo_year"] = response.meta['ipo_year']
        NdItem_result["descShort"] = desc
        NdItem_result["NIGR_result"] = NIGR_result




        yield NdItem_result  # pass to item
        pass
