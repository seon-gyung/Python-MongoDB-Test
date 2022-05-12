# 크롤링

# python -m pip install beautifulsoup4, bs4
# python -m pip install requests

from datetime import datetime
from bs4 import BeautifulSoup
import requests

lists = []

aid = []

for i in range(1, 21):
    #print(str(i).zfill(10))
    aid.append(str(i).zfill(10))
    
#print(aid)

now = datetime.now()
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
# print(nowDatetime)  


for a in aid:
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
            
        if html.status_code == 200:
            
            soup = BeautifulSoup(html.text, 'html.parser')
            
            news_title_el = soup.select_one(".media_end_head_headline")
            news_company_el = soup.select_one(".media_end_linked_more_point")
            data_createAt_el = nowDatetime
            # print(news_el)
            # print(news_title_el.get_text())
            # print(news_company_el.get_text())
            
            news_data = {news_title_el.get_text(), news_company_el.get_text(), data_createAt_el}
            # print(news_data)
            #print(data_createAt_el)
            lists.append(news_data)
            
    except Exception as e:
        pass

# print(lists)
# print(len(lists))
# print(lists[0])