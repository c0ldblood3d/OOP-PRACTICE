from order import Order
from scooter import Scooter

class Courier:
    def set_name(self, name):
        self.__name = name

    def init_workday(self):
        self.__assigned_orders = []
        self.__delivered_orders = []
        self.__scooter = None

    def assign_order(self, order):
        self.__assigned_orders.append(order)

    def complete_order(self, order):
        if order in self.__assigned_orders:
            self.__assigned_orders.remove(order)
            self.__delivered_orders.append(order)

    def get_delivered_orders(self):
        return [str(order) for order in self.__delivered_orders]

    def assign_scooter(self, scooter):
        self.__scooter = scooter

    def __str__(self):
        return f"Курьер: {self.__name}, Скутер: {'есть' if self.__scooter else 'нет'}, Доставлено: {len(self.__delivered_orders)}"