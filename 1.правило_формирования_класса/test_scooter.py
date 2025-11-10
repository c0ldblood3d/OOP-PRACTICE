from scooter import Scooter

scooter = Scooter()
scooter.set_scooter_id(10)
scooter.init_state()

print("Начальное состояние скутера:")
print(scooter)

scooter.add_mileage(12.5)
scooter.add_mileage(7.5)
print("\nПосле поездок:")
print(scooter)
print("Текущий пробег:", scooter.get_mileage(), "км")

scooter.send_to_charge()
print("\nСкутер на зарядке:")
print(scooter)

scooter.return_to_service()
print("\nСкутер снова в строю:")
print(scooter)