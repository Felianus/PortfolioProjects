from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd
import os
def check_price():
    url = "https://www.amazon.de/Advanced-Analytics-Power-Excel-visualization/dp/9391246702/ref=sr_1_1_sspa?keywords=data+analytics&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(id="price").get_text().strip()
    today = datetime.date.today()
    header = ["Title", "Price", "Date"]
    data = [title, price, today]
    if not os.path.exists(r"C:\Users\Kevin\PycharmProjects\Amazon_Webscraper\AmazonData.csv"):
        with open("AmazonData.csv", "w", newline="", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
    else:
        with open("AmazonData.csv", "a+", newline="", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(data)
while True:
    check_price()
    time.sleep(5)
    df = pd.read_csv(r"C:\Users\Kevin\PycharmProjects\Amazon_Webscraper\AmazonData.csv")
    print(df)
