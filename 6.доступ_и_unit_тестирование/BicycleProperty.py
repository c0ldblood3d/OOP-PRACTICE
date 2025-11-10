class BicycleProperty:

    def __init__(self, max_speed=30, capacity=1, fuel_tank=0, engine_oil_capacity=0, luggage_spaces=0):
        self.__max_speed = max_speed
        self.__capacity = capacity
        self.__fuel_tank = fuel_tank
        self.__engine_oil_capacity = engine_oil_capacity
        self.__luggage_spaces = luggage_spaces
        
        self.__speed = 0
        self.__distance = 0
        self.__passengers = []
        self.__empty_seats = capacity
        self.__seats_occupied = 0
        self.__fuel = 0
        self.__engine_oil = 0
        self.__luggage = []

    def get_max_speed(self):
        return self.__max_speed

    def get_capacity(self):
        return self.__capacity

    def get_fuel_tank(self):
        return self.__fuel_tank

    def get_engine_oil_capacity(self):
        return self.__engine_oil_capacity

    def get_luggage_spaces(self):
        return self.__luggage_spaces

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if 0 <= value <= self.__max_speed:
            self.__speed = value
        else:
            raise ValueError(f"Скорость должна быть между 0 и {self.__max_speed}")

    def get_distance(self):
        return self.__distance

    def set_distance(self, value):
        if value >= 0:
            self.__distance = value
        else:
            raise ValueError("Дистанция не может быть отрицательной")

    def get_passengers(self):
        return self.__passengers.copy()

    def set_passengers(self, value):
        if len(value) <= self.__capacity:
            self.__passengers = value.copy()
            self.__seats_occupied = len(value)
            self.__empty_seats = self.__capacity - len(value)
        else:
            raise ValueError(f"Количество пассажиров не может превышать {self.__capacity}")

    def get_empty_seats(self):
        return self.__empty_seats

    def set_empty_seats(self, value):
        if 0 <= value <= self.__capacity:
            self.__empty_seats = value
            self.__seats_occupied = self.__capacity - value
        else:
            raise ValueError(f"Количество свободных мест должно быть между 0 и {self.__capacity}")

    def get_seats_occupied(self):
        return self.__seats_occupied

    def set_seats_occupied(self, value):
        if 0 <= value <= self.__capacity:
            self.__seats_occupied = value
            self.__empty_seats = self.__capacity - value
        else:
            raise ValueError(f"Количество занятых мест должно быть между 0 и {self.__capacity}")

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, value):
        if 0 <= value <= self.__fuel_tank:
            self.__fuel = value
        else:
            raise ValueError(f"Количество топлива должно быть между 0 и {self.__fuel_tank}")

    def get_engine_oil(self):
        return self.__engine_oil

    def set_engine_oil(self, value):
        if 0 <= value <= self.__engine_oil_capacity:
            self.__engine_oil = value
        else:
            raise ValueError(f"Количество масла должно быть между 0 и {self.__engine_oil_capacity}")

    def get_luggage(self):
        return self.__luggage.copy()

    def set_luggage(self, value):
        if len(value) <= self.__luggage_spaces:
            self.__luggage = value.copy()
        else:
            raise ValueError(f"Количество единиц багажа не может превышать {self.__luggage_spaces}")

    max_speed = property(get_max_speed)
    capacity = property(get_capacity)
    fuel_tank = property(get_fuel_tank)
    engine_oil_capacity = property(get_engine_oil_capacity)
    luggage_spaces = property(get_luggage_spaces)
    
    speed = property(get_speed, set_speed)
    distance = property(get_distance, set_distance)
    passengers = property(get_passengers, set_passengers)
    empty_seats = property(get_empty_seats, set_empty_seats)
    seats_occupied = property(get_seats_occupied, set_seats_occupied)
    fuel = property(get_fuel, set_fuel)
    engine_oil = property(get_engine_oil, set_engine_oil)
    luggage = property(get_luggage, set_luggage)

    def display_all(self):
        print(f"Скорость: {self.__speed}")
        print(f"Дистанция: {self.__distance}")
        print(f"Макс. скорость: {self.__max_speed}")
        print(f"Пассажиры: {self.__passengers}")
        print(f"Вместимость: {self.__capacity}")
        print(f"Свободные места: {self.__empty_seats}")
        print(f"Занятые места: {self.__seats_occupied}")
        print(f"Объем бака: {self.__fuel_tank}")
        print(f"Топливо: {self.__fuel}")
        print(f"Объем масла: {self.__engine_oil_capacity}")
        print(f"Масло: {self.__engine_oil}")
        print(f"Багажные места: {self.__luggage_spaces}")
        print(f"Багаж: {self.__luggage}")