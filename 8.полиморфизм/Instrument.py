class Instrument:

    def __init__(self, name, brand, price, strings, keys):
        self.name = name
        self.brand = brand
        self.price = price
        self.strings = strings
        self.keys = keys

    def describe(self):
        print(f'{self.name}, {self.brand}, {self.price}, {self.strings}, {self.keys}')
    
    def play_style(self):
        print('Способ игры')
    
    def material(self):
        print('Материал')
    
    def calculate(self):
        volume = self.strings + self.keys
        return volume
    
class Guitar(Instrument):

    def __init__(self, name, brand, price):
        super().__init__(name, brand, price, strings=6, keys=0)

    def play_style(self):
        print('Перебор или боем')
    
    def material(self):
        print('Дерево')
    
    def calculate(self):
        price_string = self.price / self.strings
        return price_string
    
class Piano(Instrument):

    def __init__(self, name, brand, price):
        super().__init__(name, brand, price, strings=0, keys=88)

    def play_style(self):
        print('Клавиши')
    
    def material(self):
        print('Металл и дерево')
    
    def calculate(self):
        octavia = self.keys // 12
        return octavia
    