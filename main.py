import sys
from ebay_motors_scraper import EBay_Motors_Car_Scraper

def main():
    if len(sys.argv) < 2:
        print("no search term passed")
        return
        
    cars_to_add = set()
    term = sys.argv[1]
    ebay_scraper = EBay_Motors_Car_Scraper()
    ebay_cars = ebay_scraper.search(term)
    #add scraper for autotrader
    car_dao = Car_DAO()
    car_dao.upsert(cars_to_add)



if __name__ == '__main__':
    main()