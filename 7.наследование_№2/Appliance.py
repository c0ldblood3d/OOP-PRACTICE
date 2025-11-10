class Appliance:

    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def operate(self):
        return 'Работает'
    
    def __str__(self):
        return f'name: {self.name}, brand: {self.brand}, year: {self.year}'
    
class Blender(Appliance):

    def __init__(self, power, name, brand, year):
        super().__init__(name, brand, year)
        self.power = power

    def operate(self):
        return 'Перемалывает'
    
class Toaster(Appliance):

    def __init__(self, name, brand, year):
        super().__init__(name, brand, year)

    def operate(self):
        return 'Поджаривает'
    
class Kettle(Appliance):

    def __init__(self, name, brand, year):
        super().__init__(name, brand, year)

    def operate(self):
        return 'Кипятит'
    