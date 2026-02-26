from bs4 import BeautifulSoup
import requests
import pandas as pd

from package_sql.pd_sql import SQLUtils
        
class BsScraper:
    def __init__(self):
        self.target_url = "https://www.sidhakura.com/policy?page="
        self.news_list = []

    def scrap_page(self, page=1):
        response = requests.get(f"{self.target_url}{page}")

        html_text = response.text

        soup = BeautifulSoup(html_text)

        full_news_div = soup.find("div", {"class":"full-samachar-list"})
        for i in full_news_div.find_all("div"):
            title = i.find("h2").find("a").text
            image = i.find("img").get("data-src")
            publish_date = i.find("span").text
            
            self.news_list.append({
                "title":title, 
                "image":image,
                "publish_date":publish_date,
            })
            print(f"""
                TITLE :: {title}
                IMAGE :: {image}
                PUBLISHED :: {publish_date}
                \n
            """)

    def scrap_all(self):
        for i in range(1,10):
            self.scrap_page(i)

   


# instance = BsScraper()
# instance.scrap_all()

# sql_util = SQLUtils()
# sql_util.insert(pd.DataFrame(instance.news_list), "sidhakura_news")

# print(f"TOTAL NEWS SCRAPPED {len(instance.news_list)}")