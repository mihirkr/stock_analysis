from pprint import pprint

import lxml
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Agent": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",  # Do Not Track Request Header
    "Connection": "close",
}


def fetch_data(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + ".NS/?p=" + ticker + ".NS"
    data = requests.get(url, headers=headers, timeout=5)
    # print(f"Status Code: {data.status_code}")
    return data


def parse_data(ticker):
    stockDict = {}
    page_contents = fetch_data(ticker).content
    soup = BeautifulSoup(page_contents, "html.parser")
    stock_data = soup.find_all("table")
    for table in stock_data:
        trs = table.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) > 0:
                stockDict[tds[0].text] = tds[1].text
    return stockDict
