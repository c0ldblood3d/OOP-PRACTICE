from manager import Manager
from filial import Filial

filial = Filial()
filial.set_name("Филиал №2")
filial.create_list()

manager = Manager()
manager.set_manager_id(1)
manager.set_name("Сидоров Иван Петрович")
manager.set_filial(filial)
manager.set_shift("дневная")

print("Информация о менеджере:")
print(manager)