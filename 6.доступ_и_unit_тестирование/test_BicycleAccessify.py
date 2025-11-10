from BicycleAccessify import BicycleAccessify

mybike1 = BicycleAccessify(max_speed=25, capacity=1, luggage_spaces=2)
mybike2 = BicycleAccessify(max_speed=35, capacity=2, luggage_spaces=4)
mybike3 = BicycleAccessify(max_speed=20, capacity=1, luggage_spaces=1)
        
mybike1.set_speed(15)
mybike1.set_distance(100)
mybike1.set_passengers(["Alice"])
mybike1.set_luggage(["backpack"])
        
mybike2.set_speed(25)
mybike2.set_distance(200)
mybike2.set_passengers(["Bob", "Charlie"])
mybike2.set_luggage(["bag1", "bag2", "tent"])
        
mybike3.set_speed(10)
mybike3.set_distance(50)
mybike3.set_passengers(["David"])
mybike3.set_luggage(["small_bag"])
        
print("mybike1:")
print(f"  Скорость: {mybike1.get_speed()}")
print(f"  Пассажиры: {mybike1.get_passengers()}")
print(f"  Багаж: {mybike1.get_luggage()}")
        
print("\nmybike2:")
print(f"  Скорость: {mybike2.get_speed()}")
print(f"  Пассажиры: {mybike2.get_passengers()}")
print(f"  Багаж: {mybike2.get_luggage()}")
        
print("\nmybike3:")
print(f"  Скорость: {mybike3.get_speed()}")
print(f"  Пассажиры: {mybike3.get_passengers()}")
print(f"  Багаж: {mybike3.get_luggage()}")