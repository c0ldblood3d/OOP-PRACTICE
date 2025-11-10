from filial import Filial
from order import Order
from courier import Courier

filial = Filial()
filial.set_name("Филиал №1")
filial.create_list()

courier1 = Courier()
courier1.set_name("Иван")
courier1.init_workday()

courier2 = Courier()
courier2.set_name("Петр")
courier2.init_workday()

filial.add_courier(courier1)
filial.add_courier(courier2)

order1 = Order()
order1.set_order_id(101)
order1.create_positions()
order1.add_item("Маргарита", 500)

order2 = Order()
order2.set_order_id(102)
order2.create_positions()
order2.add_item("Пепперони", 600)

filial.add_order(order1)
filial.add_order(order2)

print("Информация о филиале:")
print(filial)

print("\nСтатусы заказов в филиале:")
print(filial.get_active_orders())

filial.remove_courier(courier2)
print("\nПосле увольнения курьера Петра:")
print(filial)