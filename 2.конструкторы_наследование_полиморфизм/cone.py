from math import *

class Cone:
    def __init__(self, radius):
        self.__radius = radius
        self.__height = 10
    
    def calculate_volume(self):
        return 1/3 * pi * (self.__radius)**2 * self.__height
    
    def calculate_lateral_area(self):
        return pi * self.__radius * sqrt((self.__radius)**2 + (self.__height)**2)