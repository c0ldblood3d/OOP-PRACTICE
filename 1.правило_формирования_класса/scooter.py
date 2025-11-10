class Scooter:
    def set_scooter_id(self, scooter_id):
        self.__scooter_id = scooter_id

    def init_state(self):
        self.__mileage = 0
        self.__in_service = True

    def send_to_charge(self):
        self.__in_service = False

    def return_to_service(self):
        self.__in_service = True

    def add_mileage(self, km):
        if km > 0:
            self.__mileage += km

    def get_mileage(self):
        return self.__mileage
    
    def __str__(self):
        status = "в строю" if self.__in_service else "на зарядке"
        return f"Скутер #{self.__scooter_id}, Пробег: {self.__mileage} км, Статус: {status}"