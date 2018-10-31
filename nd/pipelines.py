# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class NdPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):  # initialize the DB Connection
        self.conn = mysql.connector.connect(user='root', password='gmw6504192658',
                                            host='127.0.0.1', database='nd', charset='utf8',
                                            use_unicode=True)
        self.cursor = self.conn.cursor()  # Database operation


    def process_item(self, item, spider):
        insert_sql = """
            insert into nd2(symbol,name,sector, industry, country, board, prof_margin, ppe, marketCap, descShort,url_reuter, url_marketwatch,ipo_year,NIGR_result,
            url,EPS,insideOwn,forwardPPE,nextYEPS, insideOwnTrans,instOwn, thisYGEPS, instOwnTrans, nextYGEPS, ROA, ROE, dividAnn, ROI, dividYieldAnn,
             dividPayoutRatio,avgVolumn3Month, priceNow, recomm, SMA20, SMA50, SMA200)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

        """
        self.cursor.execute(insert_sql, (item['symbol'], item['name'],item['sector'],item['industry'],item['country'],
                                         item['board'], item['prof_margin'],item['ppe'], item['marketCap'],
                                         item['descShort'], item['url_reuter'],item['url_marketwatch'],item['ipo_year'],item['NIGR_result'],
                                         item['url'], item['EPS'], item['insideOwn'],
                                         item['forwardPPE'], item['nextYEPS'],
                                         item['insideOwnTrans'], item['instOwn'], item['thisYGEPS'],
                                         item['instOwnTrans'], item['nextYGEPS'],
                                         item['ROA'], item['ROE'], item['dividAnn'],
                                         item['ROI'], item['dividYieldAnn'],
                                         item['dividPayoutRatio'], item['avgVolumn3Month'], item['priceNow'],
                                         item['recomm'], item['SMA20'], item['SMA50'],
                                         item['SMA200']))
        self.conn.commit()
        return item

'''    def process_item(self, item, spider):
        insert_sql = """
            insert into nd(symbol,name,sector, industry, country, board, prof_margin, ppe, vol, descShort,url_reuter, url_marketwatch,ipo_year,NIGR_result)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)

        """
        self.cursor.execute(insert_sql, (item['symbol'], item['name'],item['sector'],item['industry'],item['country'],
                                         item['board'], item['prof_margin'],item['ppe'], item['vol'],
                                         item['descShort'], item['url_reuter'],item['url_marketwatch'],item['ipo_year'],item['NIGR_result']))
        self.conn.commit()
        return item
        '''