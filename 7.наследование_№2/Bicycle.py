class Vehicle:

    def __init__(self, make, model, year, type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type

    def Describe(self):
        return f'make: {self.make}, model: {self.model}, year: {self.year}, type: {self.type}'
    
class Bicycle(Vehicle):
    def __init__(self, make, model, year, type, frame_size):
        super().__init__(make, model, year, type)
        self.frame_size = frame_size

    def Describe(self):
        return f'make: {self.make}, model: {self.model}, year: {self.year}, type: {self.type}, frame_size: {self.frame_size}'
