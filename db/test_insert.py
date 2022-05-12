# 크롤링

# python -m pip install beautifulsoup4, bs4
# python -m pip install requests

from datetime import datetime
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from pymongo.cursor import CursorType


lists = []

aid = []

for i in range(1, 21):
    aid.append(str(i).zfill(10))
    
now = datetime.now()
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")

for a in aid:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
            
        if html.status_code == 200:
            
            soup = BeautifulSoup(html.text, 'html.parser')
            
            news_title_el = soup.select_one(".media_end_head_headline")
            news_company_el = soup.select_one(".media_end_linked_more_point")
            data_createAt_el = nowDatetime
            
            news_data = {"title" : news_title_el.get_text(), "company" : news_company_el.get_text(), "createAt" : data_createAt_el}

            lists.append(news_data)
            
    except Exception as e:
        pass

# Mongo insert
def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result

# Mongo 연결
mongo = MongoClient("localhost", 20000)

mongo_save(mongo, lists, "greendb", "navers")  # List안에 dict을 넣어야 함

