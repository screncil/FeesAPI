import requests
from bs4 import BeautifulSoup as BS




class FeesScraper:

    @property
    def __getBS(self) -> BS:
        r = requests.get("https://vyshybanky.com/")
        return BS(r.content, "lxml")
    

    def __get_donate_link(self, card):
        if card.find("a", {"class": "jars-item__btn--donate"}) is None:
            return None
        
        return card.find("a", {"class": "jars-item__btn--donate"}).get("href").split("?t=")[0]



    
    def getAll(self) -> list:
        lst = []
        all_cards = self.__getBS.find_all('div', {"class": "jars__item"})

        for card in all_cards:
            lst.append({
                "donate_link": self.__get_donate_link(card=card),
                "purpose": card.find("h6", {"class": "jars-item__title"}).text,
                "type": card.find("div", {"class": "jars-item__tag"}).get("title"),
                "details_link": card.find("div", {"class": "jars-item__descr"}).find_next("a").get("href"),
                "fees_creator": card.find("div", {"class": "jars-item__socials"}).find_next("a").get("href"),
                "jar": {
                    "accumulated": int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split())),
                    "goal": int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())),
                    "remains": 0 if (int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())) - int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split()))) < 0 else (int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())) - int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split()))),
                    "percent": card.find("span", {"class": "jars-item__percent"}).text
                }
            })

        return lst
    
    def type(self, type: str):
        lst = []
        all_cards = self.__getBS.find_all('div', {"class": "jars__item"})

        for card in all_cards:
            if card.find("div", {"class": "jars-item__tag"}).get("title") == type:
                lst.append({
                    "donate_link": self.__get_donate_link(card=card),
                    "purpose": card.find("h6", {"class": "jars-item__title"}).text,
                    "type": card.find("div", {"class": "jars-item__tag"}).get("title"),
                    "details_link": card.find("div", {"class": "jars-item__descr"}).find_next("a").get("href"),
                    "fees_creator": card.find("div", {"class": "jars-item__socials"}).find_next("a").get("href"),
                    "jar": {
                        "accumulated": int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split())),
                        "goal": int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())),
                        "remains": 0 if (int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())) - int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split()))) < 0 else (int("".join(card.find_all("div", {"class": "jars-stats__value"})[1].text[:-1].strip().split())) - int("".join(card.find("div", {"class": "jars-stats__value"}).text[:-1].strip().split()))),
                        "percent": card.find("span", {"class": "jars-item__percent"}).text
                    }
                })

        return lst
