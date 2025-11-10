from courier import Courier
from scooter import Scooter
from order import Order

courier = Courier()
courier.set_name("Алексей")
courier.init_workday()

scooter = Scooter()
scooter.set_scooter_id(1)
scooter.init_state()

courier.assign_scooter(scooter)

order1 = Order()
order1.set_order_id(301)
order1.create_positions()
order1.add_item("Пепперони", 600)

order2 = Order()
order2.set_order_id(302)
order2.create_positions()
order2.add_item("Вегетарианская", 550)

courier.assign_order(order1)
courier.assign_order(order2)

print("Информация о курьере:")
print(courier)

courier.complete_order(order1)
courier.complete_order(order2)

print("\nПосле доставки заказов:")
print(courier)

print("\nСписок доставленных заказов:")
print(courier.get_delivered_orders())