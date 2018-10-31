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
    name = 'nd'
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
            yield scrapy.Request('https://finviz.com/quote.ashx?t='+symbol.lower(),
                                 meta={'item_symbol': symbol,'ipo_year':IPO_year },
                                 callback=self.parse_detail)

        pass



    def parse_detail(self, response):
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
        prof_margin= response.css(".snapshot-td2 span::text").extract()[14]
        ppe = response.css(".table-dark-row:nth-child(1) td:nth-child(4) b::text").extract_first()
        vol = response.css(".snapshot-td2 b::text").extract()[4]
        #NdItem_result["url"] = response.meta['item_url']
        NdItem_result["symbol"] = response.meta['item_symbol']
        NdItem_result["name"] = name
        NdItem_result["sector"] = sector
        NdItem_result["industry"] = industry
        NdItem_result["country"] = country
        NdItem_result["board"] = board
        NdItem_result["prof_margin"] = prof_margin
        NdItem_result["ppe"] = ppe
        NdItem_result["vol"] = vol
        NdItem_result["url_reuter"] = url_reuter
        NdItem_result["url_marketwatch"] = url_marketwatch
        NdItem_result["ipo_year"] = response.meta['ipo_year']
        NdItem_result["descShort"] = desc
        NdItem_result["NIGR_result"] = NIGR_result

        yield NdItem_result  # pass to item
        pass
