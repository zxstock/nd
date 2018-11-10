import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import json

server = '127.0.0.1'

conn = mysql.connector.connect(user='root', password='gmw6504192658',
                                            host=server, database='nd', charset='utf8',
                                            use_unicode=True)
cursor = conn.cursor()  # Database operation

df_allndlist= pd.read_sql('SELECT * FROM ndall', con=conn)

#df_allndlist= pd.read_sql('SELECT * FROM nyse', con=conn)

def CustomParser(data):
    j1 = json.loads(data)
    return j1

df_allndlist['NIGR_result'] = df_allndlist['NIGR_result'].apply(CustomParser)
df_allndlist[sorted(df_allndlist['NIGR_result'][0].keys())] = df_allndlist['NIGR_result'].apply(pd.Series)
df_allndlist.drop(columns='NIGR_result',inplace = True)


def conv_str_BM(text):  # [round(float(i), 2) for i in mylist]
    if text != '-':
        if text[-1] == 'B':
            return round(float(text[:-1]) * 1000, 3)
        else:
            return round(float(text[:-1]) * 1, 3)
    else:
        return 0


def conv_str_KM(text):  # [round(float(i), 2) for i in mylist]
    if text != '-':
        if text[-1] == 'K':
            return round(float(text[:-1]) / 1000, 3)
        else:
            return round(float(text[:-1]) * 1, 3)
    else:
        return 0


df_allndlist['marketCap'] = df_allndlist['marketCap'].apply(conv_str_BM)
df_allndlist.rename(columns={'marketCap': 'marketCapMillion'}, inplace=True)

df_allndlist['avgVolumn3Month'] = df_allndlist['avgVolumn3Month'].apply(conv_str_KM)
df_allndlist.rename(columns={'avgVolumn3Month': 'avgVolumn3MonthMillion'}, inplace=True)
# print(df_allndlist['marketCap'].unique())

def p2f_comma(x):
    if x!= '-':
        return float((x.replace(',', "").strip('%')))/100
    else:
        return 0

def p2f(x):
    if x!= '-':
        return round(float(x.strip('%'))/100,4)
    else:
        return 0

def str2float(x):
    if x!= '-':
        return round(float(x)/100,4)
    else:
        return 0

df_allndlist['ppe'] =df_allndlist['ppe'].apply(str2float)
df_allndlist['EPS'] =df_allndlist['EPS'].apply(str2float)
df_allndlist['forwardPPE'] =df_allndlist['forwardPPE'].apply(str2float)
df_allndlist['nextYEPS'] =df_allndlist['nextYEPS'].apply(str2float)
df_allndlist['dividAnn'] =df_allndlist['dividAnn'].apply(str2float)
df_allndlist['priceNow'] =df_allndlist['priceNow'].apply(str2float)
df_allndlist['recomm'] =df_allndlist['recomm'].apply(str2float)
df_allndlist.rename(columns={'recomm':'recomm1buy5sell'}, inplace=True)


df_allndlist['relVolumn'] =df_allndlist['relVolumn'].apply(str2float)  #for NYSE stock, not for ND for now@11.7.2018
df_allndlist['PEG'] =df_allndlist['PEG'].apply(str2float)
df_allndlist['PSR'] =df_allndlist['PSR'].apply(str2float)
df_allndlist['PBR'] =df_allndlist['PBR'].apply(str2float)
df_allndlist['PFCF'] =df_allndlist['PFCF'].apply(str2float)
df_allndlist['DEBTtoEquity'] =df_allndlist['DEBTtoEquity'].apply(str2float)
df_allndlist['Beta'] =df_allndlist['Beta'].apply(str2float)

df_allndlist['ipo_year'] = df_allndlist['ipo_year'].apply(lambda x: int(x[:-2] if (len(x) == 6) else 0))



df_allndlist['prof_margin']=df_allndlist['prof_margin'].apply(p2f)
df_allndlist.rename(columns={'prof_margin':'prof_marginPCT'}, inplace=True)
df_allndlist['insideOwn']=df_allndlist['insideOwn'].apply(p2f)
df_allndlist.rename(columns={'insideOwn':'insideOwnPCT'}, inplace=True)
df_allndlist['insideOwnTrans']=df_allndlist['insideOwnTrans'].apply(p2f)
df_allndlist.rename(columns={'insideOwnTrans':'insideOwnTrans6monthPCT'}, inplace=True)
df_allndlist['instOwn']=df_allndlist['instOwn'].apply(p2f)
df_allndlist.rename(columns={'instOwn':'instOwnPCT'}, inplace=True)
df_allndlist['thisYGEPS']=df_allndlist['thisYGEPS'].apply(p2f)
df_allndlist.rename(columns={'thisYGEPS':'thisYearGrowthEPSPCT'}, inplace=True)
df_allndlist['instOwnTrans']=df_allndlist['instOwnTrans'].apply(p2f)
df_allndlist.rename(columns={'instOwnTrans':'instOwnTrans3monthPCT'}, inplace=True)
df_allndlist['nextYGEPS']=df_allndlist['nextYGEPS'].apply(p2f)
df_allndlist.rename(columns={'nextYGEPS':'nextYearGrowthEPSPCT'}, inplace=True)
df_allndlist['ROA']=df_allndlist['ROA'].apply(p2f)
df_allndlist.rename(columns={'ROA':'ROAPCT'}, inplace=True)
df_allndlist['ROE']=df_allndlist['ROE'].apply(p2f)
df_allndlist.rename(columns={'ROE':'ROEPCT'}, inplace=True)
df_allndlist['ROI']=df_allndlist['ROI'].apply(p2f)
df_allndlist.rename(columns={'ROI':'ROIPCT'}, inplace=True)
df_allndlist['dividYieldAnn']=df_allndlist['dividYieldAnn'].apply(p2f)
df_allndlist.rename(columns={'dividYieldAnn':'dividYieldAnnPCT'}, inplace=True)
df_allndlist['dividPayoutRatio']=df_allndlist['dividPayoutRatio'].apply(p2f)
df_allndlist.rename(columns={'dividPayoutRatio':'dividPayoutRatioPCT'}, inplace=True)
df_allndlist['SMA20']=df_allndlist['SMA20'].apply(p2f)
df_allndlist.rename(columns={'SMA20':'SMA20PCT'}, inplace=True)
df_allndlist['SMA50']=df_allndlist['SMA50'].apply(p2f)
df_allndlist.rename(columns={'SMA50':'SMA50PCT'}, inplace=True)
df_allndlist['SMA200']=df_allndlist['SMA200'].apply(p2f)
df_allndlist.rename(columns={'SMA200':'SMA200PCT'}, inplace=True)

df_allndlist['2017-2016'] = df_allndlist['2017-2016'].apply(p2f_comma)
df_allndlist['2016-2015'] = df_allndlist['2016-2015'].apply(p2f_comma)
df_allndlist['2015-2014'] = df_allndlist['2015-2014'].apply(p2f_comma)
df_allndlist['2014-2013'] = df_allndlist['2014-2013'].apply(p2f_comma)
df_allndlist.rename(columns={'2014-2013':'2014to2013'}, inplace=True)
df_allndlist.rename(columns={'2015-2014':'2015to2014'}, inplace=True)
df_allndlist.rename(columns={'2016-2015':'2016to2015'}, inplace=True)
df_allndlist.rename(columns={'2017-2016':'2017to2016'}, inplace=True)

#df_allndlist.to_csv('list_ndall.csv',encoding='utf-8',index=False)
df_allndlist.to_csv('list_ndall_3051.csv',encoding='utf-8',index=False)
