import bs4
from invalid_url_exception import Invalid_URL_Exception
from typing import Text, Union
from car import Car
import requests
from bs4 import BeautifulSoup
from collections import Set
from car_scraper import Car_Scraper

class EBay_Motors_Car_Scraper(Car_Scraper):
    EBAY_MOTORS_URL = "https://www.ebay.com/sch/6001/i.html?_from=R40&_nkw="

    ATTRIBUTE_LABELS = {
        'year': 1,
        'vin': 2,
        'milage': 3,
        'model': 6,
        'trim': 9,
        'make': 10,
        'title': 11
    }

    def __init__(self) -> None:
        super().__init__()

    def search(self, term) -> Set[Car]:
        url = EBay_Motors_Car_Scraper.EBAY_MOTORS_URL + term.replace(" ", "+")
        car_search = requests.get(url)
        search_soup = BeautifulSoup(car_search.text)
        cars_divs = search_soup.find_all('div', {'class': 's-item__wrapper'})
        print(len(cars_divs))
        for div in cars_divs:
            item_link = div.find('a', {'class': 's-item__link'})
            if item_link == None:
                continue

            url = item_link.get('href')
            try:
                car = self.__scrape_car(url)
                
            except Invalid_URL_Exception:
                continue

            self.cars.add(car)

        return self.cars

    def __scrape_car(self, url) -> Car:
        page = requests.get(url)
        car_soup = BeautifulSoup(page.text)
        info = car_soup.find('div', {'class':'itemAttr'})
            
        if info == None or 'VIN' not in str(info):
            raise Invalid_URL_Exception()

        car = {'url': url}
        props = info.find_all('span')
        for prop, index in EBay_Motors_Car_Scraper.ATTRIBUTE_LABELS.items():
            car[prop] = props[index].text

        car['price'] = car_soup.find('span', {'id':'prcIsum'}).get('content')
        return Car.from_dict(car)

bar = EBay_Motors_Car_Scraper()
bar.search("fiesta st")