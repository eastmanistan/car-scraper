class Car:
    def __init__(self, url="", make="", model="", trim="", price="", location="", year="", milage="", title='') -> None:
        self.url = url
        self.make = make
        self.trim = trim
        self.model = model
        self.price = price
        self.location = location
        self.year = year
        self.milage = milage
        self.title = title
        

    def getUrl(self):
        return self.url

    def setUrl(self, value):
        self.url = value

    def getModel(self):
        return self.model

    def setModel(self, value):
        self.model = value
    
    def getMake(self):
        return self.make

    def setMake(self, value):
        self.make = value
    
    def getPrice(self):
        return self.price

    def setPrice(self, value):
        self.price = value

    def getLocation(self):
        return self.location

    def setLocation(self, value):
        self.location = value

    def getYear(self):
        return self.year

    def setYear(self, value):
        self.year = value

    def getMilage(self):
        return self.milage

    def setMilage(self, value):
        self.milage = value

    def getTrim(self):
        return self.trim

    def setTrim(self, value):
        self.trim = value

    def getTitle(self):
        return self.title

    def setTitle(self, value):
        self.title = value

    def getDistance(self, home="98122"):
        """Get distance from car location to home"""
        pass

    def from_dict(dict):
        car = Car()
        if 'url' in dict:
            car.setUrl(dict['url'])
        
        if 'model' in dict:
            car.setModel(dict['model'])
        
        if 'price' in dict:
            car.setPrice(dict['price'])
        
        if 'location' in dict:
            car.setLocation(dict['location'])
        
        if 'year' in dict:
            car.setYear(dict['year'])
        
        if 'milage' in dict:
            car.setMilage(dict['milage'])
        
        if 'trim' in dict:
            car.setTrim(dict['trim'])

        if 'model' in dict:
            car.setModel(dict['model'])

        if 'title' in dict:
            car.setTitle(dict['title'])

        return car
    