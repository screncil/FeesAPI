import requests
from bs4 import BeautifulSoup as BS




class FeesScraper:

    @property
    def __getBS(self) -> BS:
        r = requests.get("https://vyshybanky.com/")
        return BS(r.content, "lxml")
    
    def getAll(self) -> list:
        lst = []
        all_cards = self.__getBS.find_all('div', {"class": "jars__item"})

        for card in all_cards:
            lst.append({
                "donate_link": card.find("a", {"class": "jars-item__btn--donate"}).get("href").split("?t=")[0],
                "purpose": card.find("h6", {"class": "jars-item__title"}).text,
                "type": card.find("div", {"class": "jars-item__tag"}).get("title"),
                "details_link": card.find("div", {"class": "jars-item__descr"}).find_next("a").get("href"),
                "fees_creator": card.find("div", {"class": "jars-item__socials"}).find_next("a").get("href")
            })

        return lst
