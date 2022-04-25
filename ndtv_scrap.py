"""
Spyder Editor

Sathyanarayan Rao
"""

# In this code, I am using web scraping to scrap data from NDTV website.
# I am mainly interested in open price of a particular stock.

from bs4 import BeautifulSoup
import requests


# get open price of BankNifty

website1 = 'https://www.ndtv.com/business/marketdata/domestic-index-nse_banknifty'
response = requests.get(website1)
soup = BeautifulSoup(response.content,'html.parser')
open_price1 = soup.find(id = 'open').get_text()

# get open price of TATA Motors

website1 = 'https://www.ndtv.com/business/stock/tata-motors-ltd_tatamotors'
response = requests.get(website1)
soup = BeautifulSoup(response.content,'html.parser')
open_price2 = soup.find(id = 'nseDayOpen').get_text()
