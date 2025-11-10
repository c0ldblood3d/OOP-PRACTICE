from filial import Filial

class Manager:
    def set_manager_id(self, manager_id):
        self.__manager_id = manager_id

    def set_name(self, name):
        self.__name = name

    def set_filial(self, filial):
        self.__filial = filial

    def set_shift(self, shift):
        self.__shift = shift

    def __str__(self):
        return f"Менеджер {self.__name}, ID: {self.__manager_id}, Смена: {self.__shift}, Филиал: {self.__filial._Filial__name}"