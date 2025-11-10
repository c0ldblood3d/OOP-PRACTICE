from order import Order

order = Order()
order.set_order_id(201)
order.create_positions()

order.add_item("Маргарита", 500)
order.add_item("Пепперони", 600)
order.add_item("4 Сыра", 550)

print("После добавления позиций:")
print(order)

order.remove_item("Маргарита")
print("\nПосле удаления Маргариты:")
print(order)

print("\nИтоговая сумма заказа:", order.total())

order.change_status("готовится")
print("Статус заказа изменён:", order.get_status())

order.change_status("в пути")
print("Статус заказа изменён:", order.get_status())

order.change_status("доставлен")
print("Статус заказа изменён:", order.get_status())