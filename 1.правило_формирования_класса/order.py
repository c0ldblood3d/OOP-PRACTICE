class Order:
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def create_positions(self):
        self.__positions = []
        self.__status = "принят"

    def add_item(self, name, price):
        self.__positions.append((name, price))

    def remove_item(self, name):
        self.__positions = [item for item in self.__positions if item[0] != name]

    def total(self):
        return sum(price for _, price in self.__positions)

    def change_status(self, new_status):
        if new_status in ["принят", "готовится", "в пути", "доставлен"]:
            self.__status = new_status

    def get_status(self):
        return self.__status
    
    def __str__(self):
        return f"Заказ #{self.__order_id}, Статус: {self.__status}, Сумма: {self.total()} руб."
