from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from scrapy.http import Request
from bs4 import BeautifulSoup
import pandas as pd


#chrome_options = Options()
#chrome_options.add_argument("--headless")
firefox_options = Options()
#firefox_options.add_argument("--headless")
#driver = webdriver.Chrome(executable_path=r"C:\driver\chromedriver.exe",chrome_options=chrome_options)
driver = webdriver.Firefox(executable_path=r"C:\driver_ff\geckodriver.exe",firefox_options=firefox_options)
#src = driver.find_element_by_name("quote_profile_iframe").get_attribute("src")
#url = parse.urljoin('https://www.cnbc.com/quotes/?symbol=AAPL&tab=profile', src)

def get_NIGR_js(url):
    driver.get('https://www.marketwatch.com/investing/stock/'+url+'/financials/income-statement')
    #print(driver.page_source)
    webpage = driver.page_source
    soup = BeautifulSoup(webpage, 'html.parser')
    net = soup.find(id="ratio_NetIncGrowth")
    if net is None:
        all_NetIncGrowth_ratio = ['-','-','-','-']
    else:
        all_NetIncGrowth_ratio = [net.findAll('td')[2].string,net.findAll('td')[3].string,net.findAll('td')[4].string,net.findAll('td')[5].string]
    index_year = ['2014-2013','2015-2014','2016-2015','2017-2016'] #used for dict store and json later into mysql

    df_NIGR = pd.Series(all_NetIncGrowth_ratio,index=index_year)
    df_NIGR_json = df_NIGR.to_json()
    return(df_NIGR_json)


