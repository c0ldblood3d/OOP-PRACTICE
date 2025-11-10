from accessify import private

class BicycleAccessify:
        
        @private
        def __max_speed(self): pass

        @private  
        def __capacity(self): pass

        @private
        def __fuel_tank(self): pass

        @private
        def __engine_oil_capacity(self): pass

        @private
        def __luggage_spaces(self): pass

        def __init__(self, max_speed=30, capacity=1, fuel_tank=0, engine_oil_capacity=0, luggage_spaces=0):
            self.__set_max_speed(max_speed)
            self.__set_capacity(capacity)
            self.__set_fuel_tank(fuel_tank)
            self.__set_engine_oil_capacity(engine_oil_capacity)
            self.__set_luggage_spaces(luggage_spaces)
            
            self.__speed = 0
            self.__distance = 0
            self.__passengers = []
            self.__empty_seats = capacity
            self.__seats_occupied = 0
            self.__fuel = 0
            self.__engine_oil = 0
            self.__luggage = []

        @private
        def __set_max_speed(self, value):
            self.__max_speed = value

        @private
        def __set_capacity(self, value):
            self.__capacity = value

        @private
        def __set_fuel_tank(self, value):
            self.__fuel_tank = value

        @private
        def __set_engine_oil_capacity(self, value):
            self.__engine_oil_capacity = value

        @private
        def __set_luggage_spaces(self, value):
            self.__luggage_spaces = value

        @private
        def __validate_speed(self, value):
            if not (0 <= value <= self.__max_speed):
                raise ValueError(f"Скорость должна быть между 0 и {self.__max_speed}")

        @private
        def __validate_capacity_related(self, value, field_name):
            if not (0 <= value <= self.__capacity):
                raise ValueError(f"{field_name} должно быть между 0 и {self.__capacity}")

        @private
        def __validate_passengers_count(self, value):
            if len(value) > self.__capacity:
                raise ValueError(f"Количество пассажиров не может превышать {self.__capacity}")

        @private
        def __validate_luggage_count(self, value):
            if len(value) > self.__luggage_spaces:
                raise ValueError(f"Количество единиц багажа не может превышать {self.__luggage_spaces}")

        @private
        def __validate_fuel_related(self, value, capacity, field_name):
            if not (0 <= value <= capacity):
                raise ValueError(f"{field_name} должно быть между 0 и {capacity}")

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
            self.__validate_speed(value)
            self.__speed = value

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
            self.__validate_passengers_count(value)
            self.__passengers = value.copy()
            self.__seats_occupied = len(value)
            self.__empty_seats = self.__capacity - len(value)

        def get_empty_seats(self):
            return self.__empty_seats

        def set_empty_seats(self, value):
            self.__validate_capacity_related(value, "Количество свободных мест")
            self.__empty_seats = value
            self.__seats_occupied = self.__capacity - value

        def get_seats_occupied(self):
            return self.__seats_occupied

        def set_seats_occupied(self, value):
            self.__validate_capacity_related(value, "Количество занятых мест")
            self.__seats_occupied = value
            self.__empty_seats = self.__capacity - value

        def get_fuel(self):
            return self.__fuel

        def set_fuel(self, value):
            self.__validate_fuel_related(value, self.__fuel_tank, "Количество топлива")
            self.__fuel = value

        def get_engine_oil(self):
            return self.__engine_oil

        def set_engine_oil(self, value):
            self.__validate_fuel_related(value, self.__engine_oil_capacity, "Количество масла")
            self.__engine_oil = value

        def get_luggage(self):
            return self.__luggage.copy()

        def set_luggage(self, value):
            self.__validate_luggage_count(value)
            self.__luggage = value.copy()

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