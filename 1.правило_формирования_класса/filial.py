from order import Order
from courier import Courier

class Filial:
    def set_name(self, name):
        self.__name = name

    def create_list(self):
        self.__couriers = []
        self.__active_orders = []

    def add_courier(self, courier):
        self.__couriers.append(courier)

    def remove_courier(self, courier):
        self.__couriers.remove(courier)

    def add_order(self, order):
        self.__active_orders.append(order)

    def get_active_orders(self):
        return [order.get_status() for order in self.__active_orders]
    
    def __str__(self):
        return f"Филиал: {self.__name}, Курьеров: {len(self.__couriers)}, Активных заказов: {len(self.__active_orders)}"